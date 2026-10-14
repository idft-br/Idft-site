import html, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from temas_data import TEMAS, TODOS, IMG, ORDEM, NOMES

OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
WFULL = ' style="width: 100%"'
CARDM = ' style="flex: none; width: 300px; box-sizing: border-box; scroll-snap-align: start"'
E = html.escape

DISP = "'Red Hat Display', 'Segoe UI', Helvetica, sans-serif"
MONO = "'IBM Plex Mono', Menlo, monospace"

CSS = """
body{margin:0}
.pg{background:#FFFFFF;color:#10213F;font-family:'Red Hat Text','Segoe UI',Helvetica,sans-serif;font-size:16px;line-height:1.5}
.pg a{color:#1755C5}
.wrap{max-width:1200px;margin:0 auto;box-sizing:border-box;padding-left:40px;padding-right:40px}
.m .wrap{padding-left:20px;padding-right:20px}
.disp{font-family:'Red Hat Display','Segoe UI',Helvetica,sans-serif}
.lbl{font-family:'IBM Plex Mono',Menlo,monospace;font-size:12px;font-weight:500;letter-spacing:.14em;text-transform:uppercase;color:#1755C5}
.cut{clip-path:polygon(0 0,calc(100% - 12px) 0,100% 12px,100% 100%,0 100%)}
.cut-s{clip-path:polygon(0 0,calc(100% - 8px) 0,100% 8px,100% 100%,0 100%)}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:12px;min-height:52px;box-sizing:border-box;padding:0 28px 0 24px;font-size:16px;font-weight:700;text-decoration:none}
.pg .btn-p{background:#1755C5;color:#FFFFFF}
.pg .btn-s{background:#EEF3FB;color:#0B2A6B}
.chip{align-self:flex-start;display:inline-flex;align-items:center;min-height:32px;box-sizing:border-box;padding:0 16px 0 12px;background:#EEF3FB;color:#0B2A6B;font-size:13px;font-weight:700;letter-spacing:.08em;text-transform:uppercase}
.h2{margin:0;font-family:'Red Hat Display','Segoe UI',Helvetica,sans-serif;font-size:36px;font-weight:800;line-height:1.1;letter-spacing:-.02em}
.m .h2{font-size:28px}
.ref{font-family:'IBM Plex Mono',Menlo,monospace;font-size:11px;font-weight:500;line-height:1.5;color:#0B2A6B;background:#EEF3FB;padding:1px 6px;margin-left:4px;-webkit-box-decoration-break:clone;box-decoration-break:clone}
.fonte{font-family:'IBM Plex Mono',Menlo,monospace;font-size:11px;line-height:1.45;color:#6B7A94}
.meta{display:inline-flex;align-items:center;gap:6px;min-height:30px;box-sizing:border-box;padding:0 10px;background:#F5F8FC;font-family:'IBM Plex Mono',Menlo,monospace;font-size:12px;color:#3D4E6E}
.tchip{flex:none;display:inline-flex;align-items:center;gap:8px;min-height:44px;box-sizing:border-box;padding:0 16px 0 12px;background:#FFFFFF;font-size:14px;font-weight:600;text-decoration:none;white-space:nowrap}
.pg .tchip{color:#10213F}
.tchip b{font-family:'IBM Plex Mono',Menlo,monospace;font-size:12px;font-weight:500;color:#1755C5}
.stat{padding:24px 26px;display:flex;flex-direction:column;gap:6px;border-left:1px solid #E3E9F3;border-top:1px solid #E3E9F3}
.stat-n{font-family:'Red Hat Display','Segoe UI',Helvetica,sans-serif;font-size:38px;font-weight:800;line-height:1.05;letter-spacing:-.02em;color:#1755C5}
.m .stat{padding:18px 16px}
.m .stat-n{font-size:28px}
.stat-l{font-size:14px;line-height:1.4;font-weight:500;color:#33456A}
.dcard{display:flex;flex-direction:column;gap:14px;padding:28px;background:rgba(255,255,255,.04);border-top:1px solid rgba(184,194,211,.35)}
.dcard-n{font-family:'IBM Plex Mono',Menlo,monospace;font-size:13px;font-weight:500;color:#E8F160}
.dcard-t{font-family:'Red Hat Display','Segoe UI',Helvetica,sans-serif;font-size:23px;font-weight:700;line-height:1.2;letter-spacing:-.01em;color:#FFFFFF;text-wrap:balance}
.dcard-x{font-size:16px;line-height:1.55;color:#B8C2D3}
.dcard-f{margin-top:auto;padding-top:12px;font-family:'IBM Plex Mono',Menlo,monospace;font-size:11px;color:#8E9AAF}
.acc{border-top:1px solid #E3E9F3}
.acc-h{width:100%;display:flex;align-items:center;gap:16px;padding:22px 0;background:none;border:0;cursor:pointer;text-align:left;font:inherit;color:#10213F}
.acc-n{flex:none;width:28px;font-family:'IBM Plex Mono',Menlo,monospace;font-size:13px;font-weight:500;color:#1755C5}
.acc-t{flex:1;font-family:'Red Hat Display','Segoe UI',Helvetica,sans-serif;font-size:22px;font-weight:800;line-height:1.22;letter-spacing:-.01em}
.m .acc-t{font-size:19px}
.acc-i{flex:none;width:36px;height:36px;display:inline-flex;align-items:center;justify-content:center;background:#EEF3FB;color:#0B2A6B}
.acc-b{padding:0 0 30px 44px}
.m .acc-b{padding-left:0}
.facts{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:16px}
.facts li{position:relative;padding-left:22px;font-size:17px;line-height:1.62}
.m .facts li{font-size:16px;padding-left:18px}
.facts li::before{content:"";position:absolute;left:0;top:.6em;width:9px;height:9px;background:#1755C5;clip-path:polygon(0 0,100% 0,100% 100%)}
.sig{background:#EEF3FB;padding:30px 32px;display:flex;flex-direction:column;gap:14px;border-left:4px solid #1755C5}
.m .sig{padding:24px 20px}
.sig p{margin:0;font-size:19px;line-height:1.55;color:#10213F;text-wrap:pretty}
.m .sig p{font-size:17px}
.side-card{display:flex;flex-direction:column;gap:12px}
.tl{list-style:none;margin:0;padding:0}
.tl li{display:grid;grid-template-columns:150px 28px 1fr;column-gap:16px}
.m .tl li{grid-template-columns:22px 1fr;column-gap:12px}
.tl-d{font-family:'IBM Plex Mono',Menlo,monospace;font-size:14px;font-weight:500;color:#1755C5;text-align:right;padding-top:1px}
.m .tl-d{text-align:left;font-size:13px;padding-top:0}
.tl-r{position:relative}
.tl-r::before{content:"";position:absolute;left:13px;top:0;bottom:0;width:2px;background:#C9D6EE}
.tl-r::after{content:"";position:absolute;left:8px;top:6px;width:12px;height:12px;background:#1755C5;clip-path:polygon(0 0,100% 0,100% 100%,0 100%)}
.m .tl-r::before{left:6px}
.m .tl-r::after{left:1px}
.tl-c{padding-bottom:28px;display:flex;flex-direction:column;gap:6px}
.tl-c p{margin:0;font-size:16px;line-height:1.55}
.m .tl-c p{font-size:15px}
.tl-gap .tl-r::before{background:repeating-linear-gradient(#C9D6EE 0 4px,transparent 4px 9px)}
.tl-gap .tl-r::after{display:none}
.src{display:grid;grid-template-columns:40px 1fr auto;column-gap:14px;align-items:start;padding:16px 0;border-top:1px solid #E3E9F3}
.src-i{width:40px;height:40px;background:#EEF3FB;color:#0B2A6B;display:flex;align-items:center;justify-content:center}
.src-t{font-weight:700;font-size:15px;line-height:1.35}
.src-d{font-size:14px;line-height:1.45;color:#3D4E6E}
.pill{font-family:'IBM Plex Mono',Menlo,monospace;font-size:11px;letter-spacing:.06em;text-transform:uppercase;padding:4px 8px;background:#F5F8FC;color:#6B7A94;white-space:nowrap}
.pg .openl{font-size:14px;font-weight:700;color:#1755C5;white-space:nowrap;text-decoration:none}
.tab{flex:none;display:inline-flex;align-items:center;min-height:40px;box-sizing:border-box;padding:0 14px;font-size:14px;font-weight:600;text-decoration:none;white-space:nowrap;background:#FFFFFF;border:1px solid #DCE8FB}
.pg .tab{color:#10213F}
.pg .tab.on{background:#10213F;color:#FFFFFF;border-color:#10213F}
"""

ARROW = '<svg viewBox="0 0 16 16" style="width: 16px; height: 16px; flex: none" fill="none" stroke="{c}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4"></path></svg>'
ARROW_L = '<svg viewBox="0 0 16 16" style="width: 16px; height: 16px; flex: none" fill="none" stroke="{c}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M13 8H3M7 4L3 8l4 4"></path></svg>'
OUTL = '<svg viewBox="0 0 24 24" style="width: 14px; height: 14px; flex: none" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M7 17L17 7M9 7H17V15"></path></svg>'
PLAY = '<svg viewBox="0 0 24 24" style="width: 14px; height: 14px" fill="currentColor" aria-hidden="true"><path d="M7 4L20 12L7 20Z"></path></svg>'
PLUS = '<svg viewBox="0 0 16 16" style="width: 14px; height: 14px" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M8 3v10M3 8h10"></path></svg>'
MINUS = '<svg viewBox="0 0 16 16" style="width: 14px; height: 14px" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M3 8h10"></path></svg>'
DOC = '<svg viewBox="0 0 24 24" style="width: 18px; height: 18px" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true"><path d="M6 3h8l4 4v14H6z"></path><path d="M14 3v4h4M9 12h6M9 16h6"></path></svg>'
LINK = '<svg viewBox="0 0 24 24" style="width: 18px; height: 18px" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"></path><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"></path></svg>'
SEARCH = '<svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="#10213F" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="7.5" cy="7.5" r="5"></circle><path d="M11.5 11.5 16 16"></path></svg>'
MENU = '<svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M3 6h14M3 10h14M3 14h14"></path></svg>'
SHIELD = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l8 3v6c0 4.5-3.2 8.2-8 9-4.8-.8-8-4.5-8-9V6l8-3z"></path><path d="M9 12l2 2 4-4"></path></svg>'

def bird(w, h, stroke="#FFFFFF", sw=4, pal=("#4B86E6", "#1755C5", "#0B2A6B", "#4B86E6", "#8FB4F0", "#1755C5")):
    pts = ["32,25 113.5,58.5 82.5,115", "113.5,58.5 155.5,134 82.5,115", "128.9,86.2 159.5,60.5 155.5,134",
           "159.5,60.5 195.5,80.3 159,98", "82.5,115 155.5,134 113.5,176.5", "82.5,115 113.5,176.5 66.5,224.5"]
    polys = "".join(f'<polygon points="{p}" fill="{c}"></polygon>' for p, c in zip(pts, pal))
    return f'<svg viewBox="26 19 176 212" style="width: {w}px; height: {h}px; flex: none" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round" aria-hidden="true">{polys}</svg>'

def header(m):
    logo = f'<a href="HomeV3B.dc.html" style="display: flex; align-items: center; gap: 10px; text-decoration: none; color: #10213F" aria-label="IDFT — página inicial">{bird(28 if m else 34, 34 if m else 41)}<span class="disp" style="font-size: {24 if m else 28}px; font-weight: 800; letter-spacing: -0.02em">IDFT</span></a>'
    if m:
        return f'''<header style="background: #FFFFFF; border-bottom: 1px solid #E3E9F3">
<div class="wrap" style="display: flex; align-items: center; justify-content: space-between; gap: 12px; min-height: 64px">{logo}
<div style="display: flex; gap: 8px"><button type="button" aria-label="Buscar" style="width: 44px; height: 44px; border: 1.5px solid #10213F; background: transparent; display: inline-flex; align-items: center; justify-content: center">{SEARCH}</button><button type="button" aria-label="Abrir o menu" style="width: 44px; height: 44px; border: 0; background: #1755C5; display: inline-flex; align-items: center; justify-content: center">{MENU}</button></div>
</div></header>'''
    nav = "".join(f'<a href="#" style="color: #10213F; text-decoration: none; padding: 12px 0{"; box-shadow: inset 0 -3px 0 #1755C5" if t == "Temas" else ""}">{t}</a>' for t in ["Projeto Diagonal", "Temas", "Dados", "Vídeos", "Sobre"])
    return f'''<header style="background: #FFFFFF; border-bottom: 1px solid #E3E9F3">
<div class="wrap" style="padding-top: 16px; padding-bottom: 16px; display: flex; align-items: center; justify-content: space-between; gap: 12px 32px">{logo}
<nav style="display: flex; align-items: center; gap: 4px 26px; font-size: 15px; font-weight: 600" aria-label="Seções do site">{nav}
<a href="#" class="cut" style="display: inline-flex; align-items: center; min-height: 44px; box-sizing: border-box; padding: 0 22px 0 18px; background: #1755C5; color: #FFFFFF; font-weight: 700; text-decoration: none">Iniciativas</a>
<button type="button" aria-label="Buscar" style="width: 44px; height: 44px; border: 1.5px solid #10213F; background: transparent; display: inline-flex; align-items: center; justify-content: center">{SEARCH}</button>
</nav></div></header>'''

def hero(t, m):
    nf = t.get("fontes_total", len(t["fontes"]))
    upd = "Rascunho em revisão" if t["atualizado"] == "rascunho" else f'Atualizado em {t["atualizado"]}'
    metas = f'<span class="meta">{upd}</span><span class="meta">{len(t["destaques"])} destaques</span><span class="meta">{nf} documentos citados</span>'
    crumb = f'<nav aria-label="Você está em" class="lbl" style="color: #6B7A94; display: flex; gap: 8px; flex-wrap: wrap"><a href="HomeV3B.dc.html" style="color: #6B7A94; text-decoration: none">Início</a><span>/</span><a href="#" style="color: #6B7A94; text-decoration: none">Temas</a><span>/</span><span style="color: #1755C5">{t["n"]}</span></nav>'
    has_video = any(v[2] for v in t["videos"])
    b1 = f'<a href="#video" class="btn btn-p cut"{WFULL if m else ""}>{"Assistir ao vídeo" if has_video else "Ver os destaques"}{ARROW.format(c="#FFFFFF")}</a>'
    b2 = f'<a href="#fontes" class="btn btn-s cut"{WFULL if m else ""}>Ver os documentos</a>'
    img = f'<img src="{t["img"]}" alt="{E(t["alt"])}" style="display: block; width: 100%; height: auto; aspect-ratio: 3 / 2; object-fit: cover">'
    if m:
        return f'''<section style="background: #FFFFFF">
<div class="wrap" style="padding-top: 18px; padding-bottom: 28px; display: flex; flex-direction: column; gap: 18px">
{crumb}
<span class="chip cut">Tema {t["n"]} · de 12</span>
<h1 class="disp" style="margin: 0; font-size: 38px; font-weight: 800; line-height: 1.02; letter-spacing: -0.025em; text-wrap: balance">{t["title"]}</h1>
<p style="margin: 0; font-size: 18px; line-height: 1.5; color: #33456A; text-wrap: pretty">{t["line"]}</p>
</div>
<div style="padding: 0 0 4px 0">{img}</div>
<div class="wrap" style="padding-top: 20px; padding-bottom: 32px; display: flex; flex-direction: column; gap: 18px">
<div style="display: flex; flex-wrap: wrap; gap: 8px">{metas}</div>
<div style="display: flex; flex-direction: column; gap: 10px">{b1}{b2}</div>
</div></section>'''
    return f'''<section style="background: #FFFFFF; position: relative; overflow: hidden">
<div class="wrap" style="padding-top: 28px; padding-bottom: 64px">
{crumb}
<div style="display: grid; grid-template-columns: 1fr 1.08fr; gap: 56px; align-items: center; margin-top: 24px">
<div style="display: flex; flex-direction: column; gap: 22px">
<span class="chip cut">Tema {t["n"]} · de 12</span>
<h1 class="disp" style="margin: 0; font-size: {56 if len(t["title"]) > 24 else 66}px; font-weight: 800; line-height: 1.0; letter-spacing: -0.03em; text-wrap: balance">{t["title"]}</h1>
<p style="margin: 0; font-size: 21px; line-height: 1.5; color: #33456A; max-width: 34rem; text-wrap: pretty">{t["line"]}</p>
<div style="display: flex; flex-wrap: wrap; gap: 8px">{metas}</div>
<div style="display: flex; flex-wrap: wrap; gap: 12px 14px; padding-top: 6px">{b1}{b2}</div>
</div>
<div>{img}</div>
</div></div></section>'''

def strip(t, m):
    chips = "".join(f'<a href="#" class="tchip cut-s"><b>{n}</b>{nm}</a>' for n, nm in TODOS if n != t["n"])
    if m:
        return f'''<nav aria-label="Outros temas" style="background: #EEF3FB; padding: 14px 0 16px 0">
<div class="wrap lbl" style="color: #0B2A6B; padding-bottom: 10px">Outros temas</div>
<div style="display: flex; gap: 8px; overflow-x: auto; padding: 0 20px">{chips}</div></nav>'''
    return f'''<nav aria-label="Outros temas" style="background: #EEF3FB">
<div class="wrap" style="display: flex; align-items: center; gap: 18px; min-height: 80px">
<span class="lbl" style="color: #0B2A6B; flex: none">Outros temas</span>
<div style="flex: 1; min-width: 0; display: flex; gap: 8px; overflow: hidden; -webkit-mask-image: linear-gradient(90deg, #000 88%, transparent); mask-image: linear-gradient(90deg, #000 88%, transparent)">{chips}</div>
<button type="button" aria-label="Mais temas" style="flex: none; width: 44px; height: 44px; border: 0; background: #FFFFFF; display: inline-flex; align-items: center; justify-content: center; cursor: pointer">{ARROW.format(c="#1755C5")}</button>
</div></nav>'''

def tabs():
    items = [("Síntese", "#sintese"), ("Destaques", "#destaques"), ("Os fatos", "#fatos"), ("Linha do tempo", "#linha"), ("Fontes", "#fontes")]
    a = "".join(f'<a href="{h}" class="tab{" on" if i == 0 else ""}">{n}</a>' for i, (n, h) in enumerate(items))
    return f'''<nav aria-label="Neste tema" style="position: sticky; top: 0; z-index: 2; background: #FFFFFF; border-bottom: 1px solid #E3E9F3; padding: 10px 0">
<div style="display: flex; gap: 8px; overflow-x: auto; padding: 0 20px">{a}</div></nav>'''

def sintese(t, m):
    k = len(t["numeros"])
    cols = 2 if m else (3 if k in (3, 6) else k)
    stats = "".join(f'<div class="stat"><div class="stat-n">{n}</div><div class="stat-l">{l}</div><div class="fonte">Fonte: {f}</div></div>' for n, l, f in t["numeros"])
    grid = f'<div style="display: grid; grid-template-columns: repeat({cols}, 1fr); background: #FFFFFF; box-shadow: 0 1px 2px rgba(16, 33, 63, 0.06), 0 12px 32px rgba(16, 33, 63, 0.08); margin: 0 0 0 -1px; clip-path: inset(1px 0 0 1px)">{stats}</div>'
    if m:
        return f'''<section id="sintese" class="wrap" style="padding-top: 40px; padding-bottom: 44px; display: flex; flex-direction: column; gap: 18px">
<span class="lbl">Em síntese</span>
<p style="margin: 0; font-size: 17px; line-height: 1.6; text-wrap: pretty">{t["resumo"]}</p>
<div style="padding-top: 8px">{grid}</div></section>'''
    return f'''<section id="sintese" class="wrap" style="padding-top: 72px; padding-bottom: 72px; display: flex; flex-direction: column; gap: 40px">
<div style="display: grid; grid-template-columns: 260px 1fr; gap: 56px; align-items: start">
<div style="display: flex; flex-direction: column; gap: 10px"><span class="lbl">Em síntese</span><h2 class="h2">O caso, em um parágrafo</h2></div>
<p style="margin: 0; font-size: 20px; line-height: 1.6; max-width: 46rem; text-wrap: pretty">{t["resumo"]}</p>
</div>{grid}</section>'''

def destaques(t, m):
    cards = "".join(f'<article class="dcard"{CARDM if m else ""}><span class="dcard-n">{i+1:02d}</span><h3 class="dcard-t" style="margin: 0">{ti}</h3><p class="dcard-x" style="margin: 0">{tx}</p><span class="dcard-f">Fonte: {f}</span></article>' for i, (ti, tx, f) in enumerate(t["destaques"]))
    head = f'<div style="display: flex; flex-direction: column; gap: 10px"><span class="lbl" style="color: #E8F160">Destaques</span><h2 class="h2" style="color: #FFFFFF">O que mais chama a atenção</h2></div>'
    if m:
        return f'''<section id="destaques" style="background: #13233B; color: #FFFFFF; padding: 44px 0 40px 0; display: flex; flex-direction: column; gap: 22px">
<div class="wrap">{head}</div>
<div style="display: flex; gap: 12px; overflow-x: auto; scroll-snap-type: x mandatory; padding: 0 20px">{cards}</div>
<div class="wrap" style="display: flex; align-items: center; justify-content: space-between"><span style="font-family: {MONO}; font-size: 12px; color: #B8C2D3">1 / {len(t["destaques"])} · deslize para ver os outros</span><span style="display: flex; gap: 6px">{"".join(f'<span style="width: {18 if i == 0 else 8}px; height: 4px; background: {"#E8F160" if i == 0 else "rgba(184,194,211,.4)"}"></span>' for i in range(len(t["destaques"])))}</span></div>
</section>'''
    return f'''<section id="destaques" style="background: #13233B; color: #FFFFFF">
<div class="wrap" style="padding-top: 72px; padding-bottom: 80px; display: flex; flex-direction: column; gap: 36px">{head}
<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px">{cards}</div>
</div></section>'''

def poster(img, l1, l2, play, big):
    fs = 28 if big else 20
    corner = (f'<span style="position: absolute; right: 5%; bottom: 8%; width: {44 if big else 36}px; height: {44 if big else 36}px; border: 2px solid #FFFFFF; border-radius: 50%; box-sizing: border-box; display: flex; align-items: center; justify-content: center; color: #FFFFFF; padding-left: 2px">{PLAY}</span>'
              if play else '<span style="position: absolute; right: 5%; bottom: 8%; font-family: ' + MONO + '; font-size: 10px; letter-spacing: 0.14em; color: #E8F160">EM PRODUÇÃO</span>')
    return f'''<span style="position: relative; display: block; aspect-ratio: 16 / 9; overflow: hidden; background: #2A3240">
<img src="{img}" alt="" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; filter: saturate(0.3) brightness(0.55) contrast(1.12)">
<span style="position: absolute; inset: 0; background: rgba(12, 22, 38, 0.18)"></span>
<span class="disp" style="position: absolute; left: 6%; top: 9%; font-size: 14px; font-weight: 800; letter-spacing: -0.02em; color: #FFFFFF">IDFT</span>
<span class="disp" style="position: absolute; left: 6%; top: 34%; display: flex; flex-direction: column; align-items: flex-start; gap: 2px; font-size: {fs}px; font-weight: 700; line-height: 1.15; letter-spacing: -0.015em; color: #FFFFFF"><span>{l1}</span><span style="background: #E8F160; color: #13233B; padding: 0 5px">{l2}</span></span>
{corner}</span>'''

def videos_block(t, m):
    out = []
    for i, (ti, nota, play, (l1, l2)) in enumerate(t["videos"]):
        big = i == 0
        if i == 0:
            out.append(f'<a href="#" id="video" style="display: flex; flex-direction: column; gap: 10px; text-decoration: none; color: #10213F">{poster(t["img"], l1, l2, play, True)}<span style="font-size: 16px; font-weight: 700; line-height: 1.35">{ti}</span><span style="font-size: 14px; line-height: 1.45; color: #3D4E6E">{nota}</span></a>')
        else:
            out.append(f'<a href="#" style="display: grid; grid-template-columns: 120px 1fr; gap: 12px; align-items: start; text-decoration: none; color: #10213F">{poster(t["img"], l1, l2, play, False).replace("font-size: 20px", "font-size: 11px").replace("font-size: 14px; font-weight: 800", "font-size: 9px; font-weight: 800")}<span style="display: flex; flex-direction: column; gap: 4px"><span style="font-size: 14px; font-weight: 700; line-height: 1.35">{ti}</span><span style="font-size: 13px; line-height: 1.4; color: #3D4E6E">{nota}</span></span></a>')
    return f'<div class="side-card"><span class="lbl">{"Vídeos" if len(t["videos"]) > 1 else "Vídeo"}</span>{"".join(out)}</div>'

def figura_block(fig):
    src, alt, leg, fonte = fig
    return f'''<figure class="side-card" style="margin: 0"><span class="lbl">Documento</span>
<a href="#" style="display: block; border: 1px solid #E3E9F3; background: #FFFFFF"><img src="{src}" alt="{E(alt)}" style="display: block; width: 100%; height: auto"></a>
<figcaption style="font-size: 14px; line-height: 1.5; color: #33456A">{leg}<span class="ref">{fonte}</span></figcaption></figure>'''

def figura_corpo(fig):
    src, alt, leg, fonte = fig
    return f'''<figure style="margin: 24px 0 0 0; display: flex; flex-direction: column; gap: 10px">
<a href="#" style="display: block; border: 1px solid #E3E9F3; background: #FFFFFF"><img src="{src}" alt="{E(alt)}" style="display: block; width: 100%; height: auto"></a>
<figcaption style="font-size: 14px; line-height: 1.5; color: #33456A">{leg}<span class="ref">{fonte}</span></figcaption></figure>'''

def canal(m):
    return f'''<div style="background: #0B2A6B; color: #FFFFFF; padding: 24px; display: flex; flex-direction: column; gap: 12px">
<span style="display: inline-flex; align-items: center; gap: 8px; font-family: {MONO}; font-size: 11px; letter-spacing: 0.14em; color: #E8F160">{SHIELD}CANAL SEGURO</span>
<span class="disp" style="font-size: 21px; font-weight: 800; line-height: 1.2">Tem documentos sobre este tema?</span>
<span style="font-size: 14px; line-height: 1.5; color: #C9D6EE">Envio criptografado, sem registro de IP e com proteção à fonte.</span>
<a href="#" class="cut" style="display: inline-flex; align-items: center; justify-content: space-between; gap: 12px; min-height: 48px; box-sizing: border-box; padding: 0 18px; background: #E8F160; color: #13233B; font-size: 15px; font-weight: 700; text-decoration: none">Enviar com segurança{ARROW.format(c="#13233B")}</a></div>'''

def indice():
    items = [("01", "Em síntese"), ("02", "O que mais chama a atenção"), ("03", "O que aconteceu"), ("04", "Linha do tempo"), ("05", "Fontes e documentos")]
    li = "".join(f'<a href="#" style="display: flex; gap: 12px; align-items: baseline; padding: 9px 0; border-top: 1px solid #E3E9F3; text-decoration: none; color: {"#1755C5" if i == 2 else "#10213F"}; font-size: 15px; font-weight: {"700" if i == 2 else "500"}"><span style="font-family: {MONO}; font-size: 12px; color: #1755C5">{n}</span>{s}</a>' for i, (n, s) in enumerate(items))
    return f'<nav aria-label="Neste tema" class="side-card" style="gap: 6px"><span class="lbl" style="padding-bottom: 4px">Neste tema</span>{li}</nav>'

def fatos(t, m):
    accs = []
    for i, b in enumerate(t["blocos"]):
        if i == t["aberto"]:
            fig = figura_corpo(t["figura_corpo"]) if t.get("figura_corpo") else ""
            items = "".join(f"<li>{x}</li>" for x in t["itens"])
            accs.append(f'<div class="acc"><button type="button" class="acc-h" aria-expanded="true"><span class="acc-n">{i+1:02d}</span><span class="acc-t">{b}</span><span class="acc-i">{MINUS}</span></button><div class="acc-b"><ul class="facts">{items}</ul>{fig}</div></div>')
        else:
            accs.append(f'<div class="acc"><button type="button" class="acc-h" aria-expanded="false"><span class="acc-n">{i+1:02d}</span><span class="acc-t">{b}</span><span class="acc-i">{PLUS}</span></button></div>')
    sig = "".join(f"<p>{p}</p>" for p in t["significa"])
    main = f'''<div style="display: flex; flex-direction: column; gap: 0; min-width: 0">
<div style="display: flex; flex-direction: column; gap: 10px; padding-bottom: 22px"><span class="lbl">Os fatos</span><h2 class="h2">O que aconteceu</h2></div>
{"".join(accs)}
<div style="border-top: 1px solid #E3E9F3; padding-top: {28 if m else 36}px"><div class="sig"><span class="lbl">O que isso significa</span>{sig}</div></div>
</div>'''
    side_parts = []
    if not m:
        side_parts.append(indice())
    if t.get("figura") and not m:
        side_parts.append(figura_block(t["figura"]))
    if not m:
        side_parts.append(videos_block(t, m))
        side_parts.append(canal(m))
    if m:
        extra = []
        if t.get("figura"):
            extra.append(figura_block(t["figura"]))
        return f'''<section class="wrap" style="padding-top: 40px; padding-bottom: 8px; display: flex; flex-direction: column; gap: 28px">{videos_block(t, m)}</section>
<section id="fatos" class="wrap" style="padding-top: 32px; padding-bottom: 48px; display: flex; flex-direction: column; gap: 32px">{main}{"".join(extra)}{canal(m)}</section>'''
    return f'''<section id="fatos" class="wrap" style="padding-top: 80px; padding-bottom: 88px; display: grid; grid-template-columns: minmax(0, 1fr) 360px; gap: 72px; align-items: start">
{main}
<aside style="position: sticky; top: 24px; display: flex; flex-direction: column; gap: 32px">{"".join(side_parts)}</aside>
</section>'''

def linha(t, m):
    L = t["linha"]
    first, last = (3, 1) if m else (4, 2)
    if len(L) <= first + last + 1:
        show = [(x, False) for x in L]
        hidden = 0
    else:
        show = [(x, False) for x in L[:first]] + [(None, True)] + [(x, False) for x in L[-last:]]
        hidden = len(L) - first - last
    rows = []
    for x, gap in show:
        if gap:
            btn = f'<button type="button" style="align-self: flex-start; display: inline-flex; align-items: center; gap: 10px; min-height: 44px; box-sizing: border-box; padding: 0 16px; border: 1.5px dashed #8FB4F0; background: #FFFFFF; color: #0B2A6B; font: inherit; font-size: 14px; font-weight: 700; cursor: pointer">{PLUS}Mostrar mais {hidden} marcos</button>'
            if m:
                rows.append(f'<li class="tl-gap"><span class="tl-r"></span><div class="tl-c">{btn}</div></li>')
            else:
                rows.append(f'<li class="tl-gap"><span></span><span class="tl-r"></span><div class="tl-c">{btn}</div></li>')
            continue
        d, f, fo = x
        if m:
            rows.append(f'<li><span class="tl-r"></span><div class="tl-c"><span class="tl-d">{d}</span><p>{f}</p><span class="fonte">Fonte: {fo}</span></div></li>')
        else:
            rows.append(f'<li><span class="tl-d">{d}</span><span class="tl-r"></span><div class="tl-c"><p>{f}</p><span class="fonte">Fonte: {fo}</span></div></li>')
    head = f'<div style="display: flex; flex-direction: column; gap: 10px"><span class="lbl">{len(L)} marcos</span><h2 class="h2">Linha do tempo</h2></div>'
    pad = "40px 0 24px 0" if m else "72px 0 56px 0"
    return f'''<section id="linha" style="background: #F5F8FC; padding: {pad}">
<div class="wrap" style="display: {"flex; flex-direction: column; gap: 24px" if m else "grid; grid-template-columns: 260px 1fr; gap: 56px; align-items: start"}">{head}
<ol class="tl" style="max-width: 760px">{"".join(rows)}</ol></div></section>'''

def fontes(t, m):
    F = t["fontes"]
    total = t.get("fontes_total", len(F))
    showN = 5 if m else min(len(F), 12)
    rows = []
    for fid, desc, url in F[:showN]:
        icon = LINK if url else DOC
        right = f'<a href="#" class="openl" style="display: inline-flex; align-items: center; gap: 6px">Abrir{OUTL}</a>' if url else '<span class="pill">Em breve</span>'
        rows.append(f'<div class="src"><span class="src-i">{icon}</span><span style="display: flex; flex-direction: column; gap: 2px; min-width: 0"><span class="src-t">{fid}</span><span class="src-d">{desc}</span></span>{right}</div>')
    more = ""
    if total > showN:
        more = f'<a href="#" class="btn btn-s cut" style="align-self: flex-start; margin-top: 8px{"; width: 100%" if m else ""}">Ver as {total} fontes{ARROW.format(c="#0B2A6B")}</a>'
    head = f'<div style="display: flex; flex-direction: column; gap: 10px"><span class="lbl">Fontes e documentos</span><h2 class="h2">Cada fato, um documento</h2><p style="margin: 0; font-size: 15px; line-height: 1.5; color: #3D4E6E; max-width: 30rem">As etiquetas azuis no texto remetem a esta lista. Os documentos públicos ficam disponíveis para baixar.</p></div>'
    if m:
        return f'''<section id="fontes" class="wrap" style="padding-top: 40px; padding-bottom: 44px; display: flex; flex-direction: column; gap: 20px">{head}<div>{"".join(rows)}</div>{more}</section>'''
    return f'''<section id="fontes" class="wrap" style="padding-top: 72px; padding-bottom: 72px; display: grid; grid-template-columns: 260px 1fr; gap: 56px; align-items: start">{head}
<div style="display: flex; flex-direction: column"><div style="display: grid; grid-template-columns: 1fr 1fr; column-gap: 40px">{"".join(rows)}</div>{more}</div></section>'''

def prevnext(t, m):
    i = ORDEM.index(t["n"])
    p, n = ORDEM[i - 1], ORDEM[i + 1]
    def card(code, label, right):
        thumb = f'<img src="{IMG[code]}" alt="" style="display: block; width: {96 if m else 132}px; height: {64 if m else 88}px; object-fit: cover; flex: none">'
        txt = f'<span style="display: flex; flex-direction: column; gap: 4px; {"align-items: flex-end; text-align: right" if right else ""}"><span style="display: inline-flex; align-items: center; gap: 8px; font-family: {MONO}; font-size: 12px; letter-spacing: 0.1em; text-transform: uppercase; color: #1755C5">{"" if right else ARROW_L.format(c="#1755C5")}{label}{ARROW.format(c="#1755C5") if right else ""}</span><span class="disp" style="font-size: {18 if m else 22}px; font-weight: 800; line-height: 1.2; letter-spacing: -0.01em; color: #10213F">{code} · {NOMES[code]}</span></span>'
        inner = (txt + thumb) if right else (thumb + txt)
        return f'<a href="#" class="cut" style="display: flex; align-items: center; justify-content: {"flex-end" if right else "flex-start"}; gap: 18px; padding: 18px; background: #EEF3FB; text-decoration: none">{inner}</a>'
    return f'''<nav aria-label="Outros temas" class="wrap" style="padding-top: {8 if m else 16}px; padding-bottom: {48 if m else 88}px; display: grid; grid-template-columns: {"1fr" if m else "1fr 1fr"}; gap: {12 if m else 24}px">{card(p, "Tema anterior", False)}{card(n, "Próximo tema", True)}</nav>'''

def boletim(m):
    return f'''<section style="background: #E8F160; color: #13233B">
<div class="wrap" style="padding-top: {36 if m else 48}px; padding-bottom: {36 if m else 48}px; display: grid; grid-template-columns: {"1fr" if m else "1fr 1fr"}; gap: 20px 48px; align-items: center">
<div style="display: flex; flex-direction: column; gap: 8px"><span class="disp" style="font-size: {26 if m else 32}px; font-weight: 800; line-height: 1.1; letter-spacing: -0.02em; text-wrap: balance">Um olhar independente e rigoroso, na sua caixa de entrada.</span><span style="font-size: 16px; color: #2A3A57">Semanalmente, novas informações, iniciativas e dados em seu e-mail.</span></div>
<form action="#" style="display: flex; flex-wrap: wrap; gap: 10px"><label style="position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0)">Seu e-mail</label>
<input type="email" placeholder="seu@email.com" style="flex: 1 1 220px; min-height: 52px; box-sizing: border-box; border: 1.5px solid #13233B; padding: 0 18px; font-size: 16px; font-family: inherit; background: #FFFFFF; color: #13233B">
<button type="submit" class="cut" style="{"width: 100%; " if m else ""}min-height: 52px; padding: 0 30px 0 26px; border: none; background: #13233B; color: #FFFFFF; font-weight: 700; font-size: 16px; font-family: inherit; cursor: pointer">Assinar</button></form>
</div></section>'''

def footer(m):
    cols = [("PROJETO DIAGONAL", ["Os 12 temas", "Iniciativas", "Dados"]), ("INSTITUTO", ["Sobre", "Equipe e conselho", "Transparência do IDFT", "Apoie"]), ("CONTATO", ["contato", "Denuncie com segurança", "Imprensa"])]
    c = "".join(f'<div style="display: flex; flex-direction: column; gap: 10px; font-size: 14px"><span style="font-family: {MONO}; font-size: 12px; font-weight: 500; letter-spacing: 0.14em; color: #E8F160">{h}</span>' + "".join(f'<a href="#" style="color: #FFFFFF; text-decoration: none">{x}</a>' for x in xs) + '</div>' for h, xs in cols)
    logo = f'<div style="display: flex; flex-direction: column; gap: 14px{"; grid-column: 1 / -1" if m else ""}"><a href="#" style="display: flex; align-items: center; gap: 10px; text-decoration: none; color: #FFFFFF">{bird(30, 36, "#10213F", 4, ("#8FB4F0", "#4B86E6", "#1755C5", "#8FB4F0", "#DCE8FB", "#4B86E6"))}<span class="disp" style="font-size: 26px; font-weight: 800; letter-spacing: -0.02em">IDFT</span></a><span style="font-size: 14px; line-height: 1.5; color: #B8C2D3; max-width: 18rem">Instituto pelo Desenvolvimento Fiscal e Transparência</span></div>'
    return f'''<footer style="background: #10213F; color: #B8C2D3">
<div class="wrap" style="padding-top: {40 if m else 56}px; padding-bottom: 32px; display: flex; flex-direction: column; gap: 32px">
<div style="display: grid; grid-template-columns: {"1fr 1fr" if m else "repeat(4, 1fr)"}; gap: 28px 40px">{logo}{c}</div>
<div style="display: flex; flex-wrap: wrap; justify-content: space-between; gap: 8px 24px; border-top: 1px solid #2A3A57; padding-top: 20px; font-size: 13px"><span>© 2026 IDFT · Conteúdo sob licença CC BY 4.0, salvo indicação</span><span>Política de privacidade · Acessibilidade</span></div>
</div></footer>'''

def page(t, m):
    W, H = (390, 9000) if m else (1440, 6000)
    body = [header(m), hero(t, m)]
    if m:
        body.append(tabs())
    body += [strip(t, m), sintese(t, m), destaques(t, m), fatos(t, m), linha(t, m), fontes(t, m), prevnext(t, m), boletim(m), footer(m)]
    root_style = "width: 390px; " if m else ""
    title = f'IDFT — Tema {t["n"]}: {t["title"]} ({"celular" if m else "desktop"})'
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>{E(title)}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Red+Hat+Display:wght@300..900&amp;family=Red+Hat+Text:wght@300..700&amp;family=IBM+Plex+Mono:wght@400;500&amp;display=swap">
<style>{CSS}</style>
</helmet>
<div class="pg {"m" if m else "d"}" style="{root_style}overflow: hidden">
{chr(10).join(body)}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{W},"height":{H}}}}}'>
class Component extends DCLogic {{
renderVals() {{
return {{}};
}}
}}
</script>
</body>
</html>
'''

if __name__ == "__main__":
  FN = {"02": "Tema02Campo", "03": "Tema03Saneamento", "04": "Tema04BoraBelem", "05": "Tema05Banpara"}
  for t in TEMAS:
    for m in (False, True):
        name = f'{FN[t["n"]]}{"Mobile" if m else ""}.dc.html'
        with open(os.path.join(OUT, name), "w", encoding="utf-8") as fh:
            fh.write(page(t, m))
        print(name)
