"""Verify every link in the split pack resolves, including fragments."""
import io, os, re, sys, urllib.parse

ROOT = sys.argv[1] if len(sys.argv) > 1 else r"C:\Claude Cowork\Projects\Claude Certified Architect Prep\Claude-Certified-Architect-Foundations_Exam-Prep_v1"
os.chdir(ROOT)

files = []
for d, _, fs in os.walk('.'):
    for f in fs:
        if f.endswith(('.html', '.md')):
            p = os.path.join(d, f).replace(os.sep, '/')
            files.append(p[2:] if p.startswith('./') else p)

fileset = set(files)
anchors = {}
for f in files:
    if f.endswith('.html'):
        anchors[f] = set(re.findall(r'id="([^"]+)"', io.open(f, encoding='utf-8').read()))

JS = re.compile(r'\$\{')
bad_file, bad_frag = [], []

for f in files:
    base = os.path.dirname(f)
    s = io.open(f, encoding='utf-8').read()
    hrefs = set(re.findall(r'href="([^"]+)"', s))
    if f.endswith('.md'):
        hrefs |= set(re.findall(r'\]\(([^)]+)\)', s))
    for h in sorted(hrefs):
        if not h or h.startswith(('http', 'data:', '#', 'mailto:')) or JS.search(h):
            continue
        path, _, frag = h.partition('#')
        tgt = urllib.parse.unquote(path)
        tgt = os.path.normpath(os.path.join(base, tgt)).replace(os.sep, '/')
        if tgt not in fileset:
            bad_file.append((f, h, tgt))
            continue
        if frag and tgt.endswith('.html'):
            a = anchors.get(tgt, set())
            if frag not in a and ('p-' + frag) not in a:
                bad_frag.append((f, h))

print('files scanned      :', len(files))
print('broken file links  :', bad_file if bad_file else 'none')
print('broken fragments   :', bad_frag if bad_frag else 'none')

# citation resolution across the folder boundary
corpus = 'Learning corpus/CCA-F_Corpus_v1.html'
if os.path.exists(corpus):
    ca = set(re.findall(r'id="(s-\d+-\d+)"', io.open(corpus, encoding='utf-8').read()))
    tot = unres = 0
    for f in files:
        if not (re.search(r'Test-.*\.html$', f) or f.endswith('Trap-Sheet_v1.html')):
            continue
        s = io.open(f, encoding='utf-8').read()
        refs = {'s-%s-%s' % (m.group(1), m.group(2)) for m in re.finditer(r'\u00a7\s*(\d+)\.(\d+)', s)}
        tot += len(refs)
        unres += len([r for r in refs if r not in ca])
    print('section citations  :', tot, '| unresolved:', unres)
