// Paste into the Chrome javascript_tool while the built course is open over localhost (not file://).
// Checks every WRITTEN page's figures in both themes: SVG text outside its viewBox, text too tight in or overflowing its box,
// overlapping text, and SVG text contrast below 4.5:1. Then checks horizontal overflow at the current window width.
// Returns only failures. Set window.__ids = ['o1.1', ...] first to limit the pages; default is every written objective page.
(function () {
  var C = window.__course; if (!C) return 'open the built course first (window.__course missing)';
  function rgb(s) { var m = s.match(/rgba?\(([^)]+)\)/); if (!m) return null; var p = m[1].split(',').map(parseFloat); return { r: p[0], g: p[1], b: p[2] }; }
  function lum(c) { var f = function (v) { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); }; return 0.2126 * f(c.r) + 0.7152 * f(c.g) + 0.0722 * f(c.b); }
  function cr(a, b) { var x = lum(a), y = lum(b); return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05); }
  function geometry() {
    var out = [];
    document.querySelectorAll('.page.on svg.sv').forEach(function (svg, si) {
      var vb = svg.viewBox.baseVal, texts = [].slice.call(svg.querySelectorAll('text')), rects = [].slice.call(svg.querySelectorAll('rect.bx,rect.bb,rect.br,rect.by,rect.fl'));
      texts.forEach(function (t) {
        var b = t.getBBox(), cx = b.x + b.width / 2, cy = b.y + b.height / 2;
        if (b.x < 0 || b.x + b.width > vb.width || b.y < 0 || b.y + b.height > vb.height) out.push({ fig: si, issue: 'outside viewBox', text: t.textContent.slice(0, 30) });
        var host = rects.filter(function (r) { var rb = r.getBBox(); return cx > rb.x && cx < rb.x + rb.width && cy > rb.y && cy < rb.y + rb.height; }).sort(function (a, c) { return a.getBBox().width * a.getBBox().height - c.getBBox().width * c.getBBox().height; })[0];
        if (host) { var rb = host.getBBox(); if (b.x < rb.x + 3 || b.x + b.width > rb.x + rb.width - 3) out.push({ fig: si, issue: 'tight or overflows box', text: t.textContent.slice(0, 30), tw: Math.round(b.width), bw: Math.round(rb.width) }); }
      });
      for (var i = 0; i < texts.length; i++) for (var j = i + 1; j < texts.length; j++) {
        var a = texts[i].getBBox(), b2 = texts[j].getBBox();
        if (a.x < b2.x + b2.width - 1 && b2.x < a.x + a.width - 1 && a.y < b2.y + b2.height - 1 && b2.y < a.y + a.height - 1) out.push({ fig: si, issue: 'text overlap', a: texts[i].textContent.slice(0, 25), b: texts[j].textContent.slice(0, 25) });
      }
    });
    return out;
  }
  function contrast() {
    var bad = [];
    document.querySelectorAll('.page.on svg.sv').forEach(function (svg, si) {
      var rects = [].slice.call(svg.querySelectorAll('rect.bx,rect.bb,rect.br,rect.by,rect.fl,rect.pl')), figBg = rgb(getComputedStyle(svg.closest('figure')).backgroundColor);
      svg.querySelectorAll('text').forEach(function (t) {
        var b = t.getBBox(), cx = b.x + b.width / 2, cy = b.y + b.height / 2;
        var host = rects.filter(function (r) { var rb = r.getBBox(); return cx > rb.x && cx < rb.x + rb.width && cy > rb.y && cy < rb.y + rb.height; }).sort(function (a, c) { return a.getBBox().width * a.getBBox().height - c.getBBox().width * c.getBBox().height; })[0];
        var ratio = cr(rgb(getComputedStyle(t).fill), host ? rgb(getComputedStyle(host).fill) : figBg);
        if (ratio < 4.5) bad.push({ fig: si, text: t.textContent.slice(0, 28), ratio: Math.round(ratio * 100) / 100 });
      });
    });
    return bad;
  }
  var ids = window.__ids || C.order.filter(function (id) { return /^o\d/.test(id) && C.meta[id].written; });
  var res = { pages: ids.length, failures: [] }, keep = document.documentElement.getAttribute('data-theme');
  ids.forEach(function (id) {
    C.show(id);
    ['light', 'dark'].forEach(function (th) {
      document.documentElement.setAttribute('data-theme', th);
      var g = th === 'light' ? geometry() : [], c = contrast();
      if (g.length || c.length) res.failures.push({ id: id, theme: th, geometry: g, contrast: c });
    });
    var cw = document.documentElement.clientWidth, over = [];
    document.querySelectorAll('.page.on *').forEach(function (e) { if (e.closest('.scroll') || e.closest('svg')) return; var r = e.getBoundingClientRect(); if (r.width > 0 && r.right > cw + 1) over.push(e.tagName + '.' + String(e.className).slice(0, 20)); });
    if (document.documentElement.scrollWidth > cw || over.length) res.failures.push({ id: id, overflow: over.slice(0, 4) });
  });
  if (keep) document.documentElement.setAttribute('data-theme', keep); else document.documentElement.removeAttribute('data-theme');
  C.show('start');
  return JSON.stringify(res);
})();
