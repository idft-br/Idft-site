# Ferramentas do canvas de design

Scripts usados para ligar o canvas de design (artefato "IDFT — layout v2 e sistema de imagens") ao site.

- `home_extract.py` — extrai os textos do artboard **Home v3 · layout B++** (`HomeV3B.dc.html`, baixado do canvas) para `src/data/home.json`, que alimenta `src/pages/index.astro`. Uso: `python3 tools/canvas/home_extract.py caminho/HomeV3B.dc.html src/data/home.json`. Depois de rodar, conferir o diff do JSON e fazer o build.
- `gen_temas.py` + `temas_data.py` — geram os esboços das páginas-tema (desktop e celular) que foram publicados no canvas (`Tema02Campo`, `Tema03Saneamento`, `Tema04BoraBelem`, `Tema05Banpara`). Servem de referência para levar o layout B++ às páginas de tema do site.
- `gen_home_m.py` — gera o esboço da Home para celular (`HomeV3BMobile.dc.html`).

Os scripts dependem de Python 3 e BeautifulSoup (`pip install beautifulsoup4`).
