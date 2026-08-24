"""Split the flat pack into 'Learning corpus/' and 'Mock tests/', rewriting every cross-folder link."""
import io, os, re, shutil

ROOT = r"C:\Claude Cowork\Projects\Claude Certified Architect Prep\Claude-Certified-Architect-Foundations_Exam-Prep_v1"
LEARN = "Learning corpus"
MOCK = "Mock tests"

LEARN_FILES = [
    "Exam-Day-Guide.html",
    "CCA-F_Concept-Atlas_v2.html",
    "CCA-F_Trap-Sheet_v1.html",
    "CCA-F_Corpus_v1.html",
    "CCA-F_One-Page-Sheet_v1.html",
]
MOCK_FILES = ["README.md", "README.html", "Dashboard.html", "Test-MR.html"] + \
             ["Test-%d.html" % i for i in range(1, 8)]

HOME = {f: LEARN for f in LEARN_FILES}
HOME.update({f: MOCK for f in MOCK_FILES})

ENC = {LEARN: "Learning%20corpus", MOCK: "Mock%20tests"}


def prefix_for(from_folder, target_file):
    """Relative path prefix to reach target_file from a file living in from_folder."""
    home = HOME[target_file]
    return "" if home == from_folder else "../" + ENC[home] + "/"


def rewrite(text, from_folder, md=False):
    """Repoint every reference to a pack file at its new home."""
    for name in sorted(HOME, key=len, reverse=True):
        pre = prefix_for(from_folder, name)
        if not pre:
            continue
        # already-rewritten guard
        text = text.replace('href="' + pre + name, '\x00KEEP\x00')
        # html attributes and js template literals: href="NAME  /  href="NAME#frag
        text = text.replace('href="' + name, 'href="' + pre + name)
        # js string concatenation:  'NAME#s-'  or  `NAME#s-${...}`
        text = text.replace("'" + name + "#", "'" + pre + name + "#")
        text = text.replace("`" + name + "#", "`" + pre + name + "#")
        if md:
            # markdown links  (NAME)  and  (NAME#frag)
            text = re.sub(r'\((' + re.escape(name) + r')(#[^)]*)?\)',
                          lambda m: '(' + pre + name + (m.group(2) or '') + ')', text)
        text = text.replace('\x00KEEP\x00', 'href="' + pre + name)
    return text


def main():
    os.chdir(ROOT)
    for d in (LEARN, MOCK):
        os.makedirs(d, exist_ok=True)

    moved = []
    for name, home in HOME.items():
        if os.path.exists(name):
            shutil.move(name, os.path.join(home, name))
            moved.append((name, home))
    print('moved %d files' % len(moved))

    changed = 0
    for name, home in HOME.items():
        p = os.path.join(home, name)
        if not os.path.exists(p):
            print('MISSING', p)
            continue
        s = io.open(p, encoding='utf-8').read()
        s2 = rewrite(s, home, md=name.endswith('.md'))
        if s2 != s:
            io.open(p, 'w', encoding='utf-8').write(s2)
            changed += 1
    print('rewrote links in %d files' % changed)


if __name__ == '__main__':
    main()
