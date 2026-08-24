"""Rename the pack root, lift the README to the top level, and rebuild every link and pack bar."""
import io, os, re, shutil

PROJ = r"C:\Claude Cowork\Projects\Claude Certified Architect Prep"
OLD_ROOT = os.path.join(PROJ, "mock exams")
NEW_NAME = "Claude-Certified-Architect-Foundations_Exam-Prep_v1"
NEW_ROOT = os.path.join(PROJ, NEW_NAME)

LEARN, MOCK, ROOT = "Learning corpus", "Mock tests", ""
ENC = {LEARN: "Learning%20corpus/", MOCK: "Mock%20tests/", ROOT: ""}

LEARN_FILES = ["Exam-Day-Guide.html", "CCA-F_Concept-Atlas_v2.html", "CCA-F_Trap-Sheet_v1.html",
               "CCA-F_Corpus_v1.html", "CCA-F_One-Page-Sheet_v1.html"]
MOCK_FILES = ["Dashboard.html", "Test-MR.html"] + ["Test-%d.html" % i for i in range(1, 8)]
ROOT_FILES = ["README.md", "README.html"]

HOME = {f: LEARN for f in LEARN_FILES}
HOME.update({f: MOCK for f in MOCK_FILES})
HOME.update({f: ROOT for f in ROOT_FILES})

# pack bar, in display order
BAR = [("README.html", "Start here"),
       ("Exam-Day-Guide.html", "Exam Day Guide"),
       ("CCA-F_Concept-Atlas_v2.html", "Concept Atlas"),
       ("CCA-F_Trap-Sheet_v1.html", "Trap Sheet"),
       ("CCA-F_Corpus_v1.html", "Corpus"),
       ("CCA-F_One-Page-Sheet_v1.html", "One-page sheet"),
       ("Test-1.html", "Practice tests"),
       ("Test-MR.html", "MR drill"),
       ("Dashboard.html", "Dashboard")]


def rel(from_folder, target):
    """Relative href from a file living in from_folder to target."""
    home = HOME[target]
    if home == from_folder:
        return target
    up = "" if from_folder == ROOT else "../"
    return up + ENC[home] + target


def packbar(from_folder, current_file):
    out = ['<nav class="packbar" aria-label="CCA-F prep pack"><span class="pb-lab">CCA-F prep pack</span>']
    for name, label in BAR:
        cur = ' aria-current="page"' if name == current_file else ''
        out.append('<a href="%s"%s>%s</a>' % (rel(from_folder, name), cur, label))
    out.append('</nav>')
    return ''.join(out)


RX_BAR = re.compile(r'<nav class="packbar".*?</nav>', re.S)


def fix_body_links(text, from_folder, md=False):
    """Repoint every in-body reference at the target's new relative location."""
    for name in sorted(HOME, key=len, reverse=True):
        want = rel(from_folder, name)
        # normalise any existing prefix form back to the bare name first
        for stale in ('../Learning%20corpus/' + name, '../Mock%20tests/' + name,
                      'Learning%20corpus/' + name, 'Mock%20tests/' + name,
                      '../' + name):
            text = text.replace('href="' + stale, 'href="\x00' + name)
            text = text.replace("'" + stale + "#", "'\x00" + name + "#")
            text = text.replace("`" + stale + "#", "`\x00" + name + "#")
            if md:
                text = text.replace('(' + stale, '(\x00' + name)
        text = text.replace('href="' + name, 'href="\x00' + name)
        text = text.replace("'" + name + "#", "'\x00" + name + "#")
        text = text.replace("`" + name + "#", "`\x00" + name + "#")
        if md:
            text = re.sub(r'\((' + re.escape(name) + r')([#)])',
                          lambda m: '(\x00' + name + m.group(2), text)
        text = text.replace('\x00' + name, want)
    return text


def main():
    if os.path.exists(OLD_ROOT) and not os.path.exists(NEW_ROOT):
        shutil.move(OLD_ROOT, NEW_ROOT)
        print('renamed  mock exams  ->  %s' % NEW_NAME)
    os.chdir(NEW_ROOT)

    for f in ROOT_FILES:
        src = os.path.join(MOCK, f)
        if os.path.exists(src):
            shutil.move(src, f)
            print('lifted   %s  ->  root' % f)

    changed = 0
    for name, home in HOME.items():
        p = os.path.join(home, name) if home else name
        if not os.path.exists(p):
            print('MISSING', p)
            continue
        s = io.open(p, encoding='utf-8').read()
        orig = s
        s = fix_body_links(s, home, md=name.endswith('.md'))
        if name.endswith('.html'):
            s = RX_BAR.sub(lambda m: packbar(home, name), s, count=1)
        if s != orig:
            io.open(p, 'w', encoding='utf-8').write(s)
            changed += 1
    print('rewrote %d files' % changed)


if __name__ == '__main__':
    main()
