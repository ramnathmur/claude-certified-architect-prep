"""Markdown -> HTML block renderer for the CCA-F corpus. Guarded against non-advancing loops."""
import re, html as H

RE_FENCE = re.compile(r'^```')
RE_HR = re.compile(r'^---+\s*$')
RE_H = re.compile(r'^(#{1,6})\s+(.*)$')
RE_SEP = re.compile(r'^\|[\s\-:|]+\|?\s*$')
RE_UL = re.compile(r'^(\s*)[-*]\s+(.*)$')
RE_OL = re.compile(r'^(\s*)\d+\.\s+(.*)$')
RE_SECNUM = re.compile(r'^(\d+\.\d+)\s+(.*)$')


def inline(t):
    t = H.escape(t, quote=False)
    out, i, n = [], 0, len(t)
    while i < n:
        if t[i] == '`':
            j = t.find('`', i + 1)
            if j > 0:
                out.append('<code>' + t[i + 1:j] + '</code>')
                i = j + 1
                continue
        out.append(t[i])
        i += 1
    t = ''.join(out)
    parts = re.split(r'(<code>.*?</code>)', t, flags=re.S)
    for k, p in enumerate(parts):
        if p.startswith('<code>'):
            continue
        p = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', p)
        p = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', p)
        p = re.sub(r'(?<![\w*])\*(?!\s)([^*]+?)(?<!\s)\*(?![\w*])', r'<em>\1</em>', p)
        p = re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)', r'<a href="\2">\1</a>', p)
        parts[k] = p
    return ''.join(parts)


def _indent(s):
    return len(s) - len(s.lstrip())


def _list(lines, i, ordered):
    """Consume one list at the indent of lines[i]. Always advances at least one line."""
    n = len(lines)
    lvl = _indent(lines[i])
    tag = 'ol' if ordered else 'ul'
    out = ['<%s>' % tag]
    while i < n:
        m = RE_OL.match(lines[i]) if ordered else RE_UL.match(lines[i])
        if not m:
            other = RE_UL.match(lines[i]) if ordered else RE_OL.match(lines[i])
            if other and _indent(lines[i]) > lvl:
                sub, i = _list(lines, i, not ordered)
                out.append(sub)
                continue
            if lines[i].strip() == '' and i + 1 < n and (RE_UL.match(lines[i + 1]) or RE_OL.match(lines[i + 1])) \
               and _indent(lines[i + 1]) >= lvl:
                i += 1
                continue
            break
        ind = _indent(lines[i])
        if ind < lvl:
            break
        if ind > lvl:
            sub, ni = _list(lines, i, ordered)
            out.append(sub)
            if ni == i:      # safety: never stall
                ni = i + 1
            i = ni
            continue
        out.append('<li>' + inline(m.group(2)))
        i += 1
        # nested list directly under this item
        if i < n:
            nxt_u, nxt_o = RE_UL.match(lines[i]), RE_OL.match(lines[i])
            if (nxt_u or nxt_o) and _indent(lines[i]) > lvl:
                sub, ni = _list(lines, i, bool(nxt_o))
                out.append(sub)
                i = ni if ni > i else i + 1
        out.append('</li>')
    out.append('</%s>' % tag)
    return ''.join(out), i


def render(md):
    lines = md.split('\n')
    out, i, n = [], 0, len(lines)
    sections = []
    while i < n:
        prev = i
        ln = lines[i]

        if RE_FENCE.match(ln):
            lang = ln[3:].strip()
            i += 1
            buf = []
            while i < n and not RE_FENCE.match(lines[i]):
                buf.append(lines[i])
                i += 1
            i += 1
            cls = ' class="lang-%s"' % H.escape(lang) if lang else ''
            out.append('<pre><code%s>%s</code></pre>' % (cls, H.escape('\n'.join(buf))))

        elif RE_HR.match(ln):
            out.append('<hr/>')
            i += 1

        elif RE_H.match(ln):
            m = RE_H.match(ln)
            lv, txt = len(m.group(1)), m.group(2).strip()
            sm = RE_SECNUM.match(txt)
            if lv == 2 and sm:
                num, title = sm.group(1), sm.group(2)
                sid = 's-' + num.replace('.', '-')
                sections.append((sid, num, title))
                out.append('<h2 id="%s" class="sec"><a class="anchor" href="#%s">&sect;%s</a> %s</h2>'
                           % (sid, sid, num, inline(title)))
            elif lv == 1:
                out.append('<h1 class="doc-h1">%s</h1>' % inline(txt))
            else:
                out.append('<h%d>%s</h%d>' % (min(lv, 6), inline(txt), min(lv, 6)))
            i += 1

        elif ln.startswith('|') and i + 1 < n and RE_SEP.match(lines[i + 1]):
            head = [c.strip() for c in ln.strip().strip('|').split('|')]
            i += 2
            rows = []
            while i < n and lines[i].startswith('|') and not RE_SEP.match(lines[i]):
                rows.append([c.strip() for c in lines[i].strip().strip('|').split('|')])
                i += 1
            t = ['<div class="tw"><table><thead><tr>']
            t += ['<th>%s</th>' % inline(c) for c in head]
            t.append('</tr></thead><tbody>')
            for r in rows:
                t.append('<tr>' + ''.join('<td>%s</td>' % inline(c) for c in r) + '</tr>')
            t.append('</tbody></table></div>')
            out.append(''.join(t))

        elif ln.startswith('>'):
            buf = []
            while i < n and (lines[i].startswith('>') or
                             (lines[i].strip() == '' and i + 1 < n and lines[i + 1].startswith('>'))):
                buf.append(lines[i][1:].lstrip(' ') if lines[i].startswith('>') else '')
                i += 1
            inner, _ = render("\n".join(buf))
            out.append('<blockquote>%s</blockquote>' % inner)

        elif RE_UL.match(ln):
            frag, i = _list(lines, i, False)
            out.append(frag)

        elif RE_OL.match(ln):
            frag, i = _list(lines, i, True)
            out.append(frag)

        elif ln.strip() == '':
            i += 1

        else:
            buf = [ln.strip()]
            i += 1
            while i < n and lines[i].strip() and not (
                RE_H.match(lines[i]) or RE_FENCE.match(lines[i]) or lines[i].startswith('|')
                or lines[i].startswith('>') or RE_UL.match(lines[i]) or RE_OL.match(lines[i])
                or RE_HR.match(lines[i])
            ):
                buf.append(lines[i].strip())
                i += 1
            out.append('<p>%s</p>' % inline(' '.join(buf)))

        if i <= prev:
            raise RuntimeError('renderer made no progress at line %d: %r' % (prev + 1, lines[prev]))

    return '\n'.join(out), sections
