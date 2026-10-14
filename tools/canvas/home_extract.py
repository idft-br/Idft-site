# Extrai os textos da Home V3 (canvas, HomeV3B.dc.html) para src/data/home.json do site.
import sys, json, re
from bs4 import BeautifulSoup, NavigableString, Tag

src, out = sys.argv[1], sys.argv[2]
soup = BeautifulSoup(open(src, encoding="utf-8").read(), "html.parser")
root = soup.find("x-dc").find("div", recursive=False)

BLOB = {
    "c8f07b5220c2842b9c7a7f33526732b2": "01-visao-geral", "30b491b66c6a29891f7679d2eab435f8": "02-atuacao-no-campo",
    "03c3f39afac8537f540008ccffb682c2": "03-saneamento", "a0bf0e14befec4c62a8d2041f68c096c": "04-bora-belem",
    "1d4f8960f8de8a09b67cb5f9f5124a77": "05-master-banpara", "76c0354c307f64a20a99f6adb2d2032d": "06-seduc",
    "442bd12c2a625d77152a18cdcc28e76e": "07-transparencia", "94ecb83c833010854438094069c71e23": "08-saude",
    "77a8d6d667cc257c5da37e6a5504f73c": "09-municipios", "16dbe405c5a3abcd5ba16fb3c807751c": "10-organizacao-central",
    "76502df02a34b79ba4ff5ee2a4d7fc59": "11-juridico", "2686f0ced8ad0a5ef53a20c29a53b1b9": "12-impunidade",
    "7ef09799fcb508e8f7a22cacbe6f9fca": "iniciativa-1", "a5d872189b2ce15ee1380e24e226b3c5": "iniciativa-2",
    "406ca4b3d873bac1276f91a50ccd44f5": "iniciativa-3",
}

def img(tag):
    i = tag.find("img")
    return BLOB[re.search(r"[0-9a-f]{32}", i["src"]).group(0)]

def clean(tag):
    """HTML interno sem svg, sem atributos de estilo; destaque verde-limão vira <mark>."""
    t = BeautifulSoup(str(tag), "html.parser")
    for s in t.find_all("svg"):
        s.decompose()
    for s in t.find_all(True):
        st = s.get("style", "")
        if s.name == "span" and "E8F160" in st:
            s.name = "mark"
        for a in list(s.attrs):
            del s.attrs[a]
    first = next(iter(t.contents))
    h = "".join(str(c) for c in first.contents) if isinstance(first, Tag) else str(first)
    h = h.replace("\xa0", "&nbsp;") if False else h
    h = re.sub(r"<span>(.*?)</span>", r"\1", h, flags=re.S)
    h = re.sub(r"\s+", " ", h).strip()
    h = re.sub(r"(&nbsp;|\xa0)+$", "", h).strip()
    return h

def txt(tag):
    return re.sub(r"\s+", " ", tag.get_text(" ", strip=True)).replace("\xa0", " ").strip()

S = root.find_all("section", recursive=False)
hero, diag, temas, videos, inic, canal, dados, bol = S[:8]
foot = root.find("footer")
D = {}

# Hero
D["hero"] = dict(chip=txt(hero.find("span")), titulo=clean(hero.find("h1")), texto=clean(hero.find("p")),
                 botao=txt(hero.find("a")))

# Projeto Diagonal
blocks = diag.find_all("div", recursive=False)
top = blocks[0]
statsgrid = blocks[1].find("div")
stats = []
upd = ""
for cell in statsgrid.find_all("div", recursive=False):
    kids = cell.find_all("div", recursive=False)
    if len(kids) >= 2:
        stats.append(dict(n=txt(kids[0]), l=clean(kids[1])))
    elif kids:
        upd = txt(kids[0])
D["diagonal"] = dict(chip=txt(top.find("span")), titulo=clean(top.find("h2")), texto=clean(top.find("p")),
                     botoes=[txt(a) for a in top.find_all("a")], numeros=stats, atualizado=upd)

# Temas
cards = []
for a in temas.find_all("a"):
    spans = a.find_all("span", recursive=False)
    head = spans[0].find_all("span", recursive=False)
    cards.append(dict(n=txt(head[0]), titulo=clean(head[1]), linha=clean(spans[1]), img=img(a)))
D["temas"] = dict(titulo=txt(temas.find("h2")), texto=clean(temas.find("p")), cards=cards)

# Vídeos
w = videos.find("div")
parts = w.find_all("div", recursive=False)
headrow = parts[0]
feat_grid = parts[1]
small_grid = parts[3]
feat_a = feat_grid.find("a")
feat_spans = feat_a.find_all("span", recursive=False)
overlay = [clean(s) for s in feat_spans[2].find_all("span", recursive=False)]
topo = [txt(s) for s in feat_spans[1].find_all("span", recursive=False) if txt(s)]
base_capa = txt(feat_spans[3])
right = feat_grid.find_all("div", recursive=False)[0]
smalls = []
for a in small_grid.find_all("a", recursive=False):
    box = a.find("span")
    ov = box.find_all("span", recursive=False)[2]
    lines = [clean(s) for s in ov.find_all("span", recursive=False)]
    rest = a.find_all("span", recursive=False)[1:]
    smalls.append(dict(img=img(a), capa=lines, rotulo=txt(rest[0]), titulo=clean(rest[1])))
D["videos"] = dict(rotulo=txt(headrow.find("span")), titulo=txt(headrow.find("h2")), serie=txt(headrow.find("a")),
                   destaque=dict(img=img(feat_a), capa=overlay, topo=topo, base=base_capa, aria=feat_a.get("aria-label", ""),
                                 rotulo=txt(right.find("span")), titulo=clean(right.find("h3")), texto=clean(right.find("p")),
                                 botao=txt(right.find("a"))),
                   outros=smalls, nota=txt(w.find_all("p")[-1]))

# Iniciativas
hd = inic.find("div")
items = []
for a in inic.find_all("div", recursive=False)[1].find_all("a", recursive=False):
    sp = a.find_all("span", recursive=False)
    items.append(dict(img=img(a), rotulo=txt(sp[0]), titulo=clean(sp[1]), texto=clean(sp[2])))
D["iniciativas"] = dict(rotulo=txt(hd.find("span")), titulo=txt(hd.find("h2")), link=txt(hd.find("a")), itens=items)

# Canal seguro
g = canal.find("div").find_all("div", recursive=False)
left, rightc = g[0], g[1]
feats = [txt(s) for s in left.find_all("div", recursive=False)[0].find_all("span", recursive=False)]
D["canal"] = dict(rotulo=txt(left.find("span")), titulo=txt(left.find("h2")), texto=clean(left.find("p")),
                  marcas=feats, botoes=[txt(a) for a in rightc.find_all("a")])

# Dados
hd = dados.find("div")
D["dados"] = dict(rotulo=txt(hd.find("div").find("span")), titulo=txt(hd.find("h2")),
                  nota=txt(hd.find_all("span", recursive=False)[-1]), paineis=[txt(a) for a in dados.find_all("a")])

# Boletim
sp = bol.find("div").find("div").find_all("span", recursive=False)
D["boletim"] = dict(titulo=txt(sp[0]), texto=txt(sp[1]), botao=txt(bol.find("button")),
                    placeholder=bol.find("input").get("placeholder", ""))

# Rodapé
cols = foot.find("div").find("div").find_all("div", recursive=False)
D["rodape"] = dict(instituto=txt(cols[0].find_all("span")[-1]),
                   colunas=[dict(titulo=txt(c.find("span")), links=[txt(a) for a in c.find_all("a")]) for c in cols[1:]],
                   base=[txt(s) for s in foot.find("div").find_all("div", recursive=False)[1].find_all("span")])
D["_fonte"] = "Gerado de HomeV3B.dc.html (canvas de design). Não editar à mão: rode a extração de novo."
json.dump(D, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps({k:D[k] for k in ["videos","canal","dados","boletim","rodape"]}, ensure_ascii=False, indent=1)[:5000])
