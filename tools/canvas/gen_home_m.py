import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen_temas import CSS, header, boletim, footer, poster, ARROW, OUTL, SHIELD, MONO, E

OUT = sys.argv[1]

BIRD_PTS = ["32,25 113.5,58.5 82.5,115", "113.5,58.5 155.5,134 82.5,115", "128.9,86.2 159.5,60.5 155.5,134",
            "159.5,60.5 195.5,80.3 159,98", "82.5,115 155.5,134 113.5,176.5", "82.5,115 113.5,176.5 66.5,224.5"]
BIRD_PAL = ["#4B86E6", "#1755C5", "#0B2A6B", "#4B86E6", "#8FB4F0", "#1755C5"]
PLANE_PTS = ["650,35 143,260 410,210", "143,260 410,210 285,312", "410,210 285,312 305,412 378,335", "410,210 378,335 482,442",
             "410,210 445,236 482,442", "650,35 410,210 445,236", "650,35 445,236 482,442"]
PLANE_PAL = ["#4B86E6", "#BBD2F6", "#1755C5", "#DCE8FB", "#8FB4F0", "#DCE8FB", "#6FA0EC"]

def polys(pts, pal):
    return "".join(f'<polygon points="{p}" fill="{c}"></polygon>' for p, c in zip(pts, pal))

TEMAS = [
    ("01", "Visão geral", "Arrecadação excepcional, abandono idem: a tragédia os comuns.", "c8f07b5220c2842b9c7a7f33526732b2"),
    ("02", "Atuação no campo", "Incêndios de barracos, desmatamento, trabalho escravo e milícias em ação nos “presentes” dados pelo estado.", "30b491b66c6a29891f7679d2eab435f8"),
    ("03", "Saneamento", "A tragédia do saneamento aprofundada sem qualquer pudor em termos escancarados.", "03c3f39afac8537f540008ccffb682c2"),
    ("04", "Bora Belém e a fome", "A agressão dolosamente inconstitucional, cruel e covarde à renda de 80 mil pessoas pobres.", "a0bf0e14befec4c62a8d2041f68c096c"),
    ("05", "Ocultação bilionária, Master e o Banpará", "Ocultação bilionária nas estruturas do Master, controle do Banpará e riscos.", "1d4f8960f8de8a09b67cb5f9f5124a77"),
    ("06", "Seduc, a&nbsp;<i>nova Sespa</i>", "Desprezo pela educação e o cassetete cassetete como ritual de batismo na \"Nova Sespa\" de contratos bilionários.", "76c0354c307f64a20a99f6adb2d2032d"),
    ("07", "Transparência", "A opacidade como elemento fundamental do modelo.", "442bd12c2a625d77152a18cdcc28e76e"),
    ("08", "Saúde e pandemia", "A apropriação bilionária de verbas da saúde como base de lançamento da expansão.", "94ecb83c833010854438094069c71e23"),
    ("09", "Municípios vassalos", "O poder excessivo no estado como ferramenta de coação e imposição de custos aos municípios.", "77a8d6d667cc257c5da37e6a5504f73c"),
    ("10", "A organização central", "Ordenador, beneficiário e controle no mesmo endereço, em voracidade ímpar e sem freios.", "16dbe405c5a3abcd5ba16fb3c807751c"),
    ("11", "Jurídico", "A atuação de quem não tem voto esvaziando a importância do eleitor.", "76502df02a34b79ba4ff5ee2a4d7fc59"),
    ("12", "Impunidade e caminhos", "A armadilha é profunda, não há caminho simples e a mobilização social é o primeiro passo.", "2686f0ced8ad0a5ef53a20c29a53b1b9"),
]

def hero():
    bird = f'<svg viewBox="26 19 176 212" style="display: block; width: 190px; height: auto; aspect-ratio: 176 / 212; margin: 4px auto 0 auto" stroke="#EEF3FB" stroke-width="1.6" stroke-linejoin="round" role="img" aria-label="Pássaro de origami do IDFT em facetas azuis">{polys(BIRD_PTS, BIRD_PAL)}</svg>'
    return f'''<section style="position: relative; overflow: hidden; background: #EEF3FB">
<svg viewBox="0 0 100 100" preserveAspectRatio="none" style="position: absolute; right: 0; bottom: 0; width: 100%; height: 42%" aria-hidden="true"><polygon points="100,0 100,100 0,100" fill="#DCE8FB"></polygon></svg>
<div class="wrap" style="position: relative; padding-top: 32px; padding-bottom: 36px; display: flex; flex-direction: column; gap: 18px">
<span class="cut" style="align-self: flex-start; display: inline-flex; align-items: center; box-sizing: border-box; padding: 6px 16px 6px 12px; background: #FFFFFF; color: #0B2A6B; font-size: 11px; line-height: 1.35; font-weight: 700; letter-spacing: 0.07em; text-transform: uppercase">Instituto pelo Desenvolvimento Fiscal e Transparência</span>
<h1 class="disp" style="margin: 0; font-size: 36px; font-weight: 800; line-height: 1.04; letter-spacing: -0.025em; text-wrap: balance">Entender o que o Estado arrecada e gasta é o passo 01 de um futuro digno</h1>
<p style="margin: 0; font-size: 17px; line-height: 1.55; color: #33456A; text-wrap: pretty">Sem informação o debate público se perde em afirmações vazias, afastando o interesse na melhoria de vida do eleitor como base da conquista do voto.</p>
<a href="#diagonal" class="btn btn-p cut" style="width: 100%; justify-content: space-between">Conheça nossa atuação{ARROW.format(c="#FFFFFF")}</a>
{bird}
</div></section>'''

def diagonal():
    art = f'''<svg viewBox="0 0 720 560" role="img" aria-label="Pássaro de origami do IDFT e o avião de papel do Projeto Diagonal subindo juntos a mesma faixa diagonal" style="display: block; width: 100%; height: auto; aspect-ratio: 720 / 560">
<polygon points="61.2,376.6 540.4,15.5 654.7,167.2 175.5,528.3" fill="#EEF3FB"></polygon>
<path d="M130.4 443.4 L533.7 139.5" fill="none" stroke="#8FB4F0" stroke-width="3" stroke-linecap="round" stroke-dasharray="2 11"></path>
<g transform="translate(61.52 206.74) scale(1.5)" stroke="#FFFFFF" stroke-width="1.4" stroke-linejoin="round">{polys(BIRD_PTS, BIRD_PAL)}</g>
<g transform="translate(328.41 23.64) scale(0.48)" stroke="#FFFFFF" stroke-width="4.4" stroke-linejoin="round">{polys(PLANE_PTS, PLANE_PAL)}</g>
</svg>'''
    stats = [("+ de 100%", "Aumento <b>real</b> da arrecadação"),
             ("[+ de 150%]", "Aumento do valor pago às OSS entre 2018-21, de 0,6 para 1,7bi"),
             ("[0]", "Nenhum aumento no volume de serviços nem melhora em rankings")]
    rows = "".join(f'<div style="display: grid; grid-template-columns: 128px 1fr; gap: 14px; align-items: center; padding: 16px 18px; border-top: {"0" if i == 0 else "1px solid #E3E9F3"}"><span class="disp" style="font-size: 26px; font-weight: 800; line-height: 1.05; letter-spacing: -0.02em; color: #1755C5">{n}</span><span style="font-size: 14px; line-height: 1.4; font-weight: 500; color: #3D4E6E">{l}</span></div>' for i, (n, l) in enumerate(stats))
    return f'''<section id="diagonal" style="background: #FFFFFF; border-bottom: 1px solid #E3E9F3">
<div class="wrap" style="padding-top: 44px; padding-bottom: 40px; display: flex; flex-direction: column; gap: 18px">
<span class="chip cut">[ Projeto Diagonal ]</span>
<h2 class="disp" style="margin: 0; font-size: 33px; font-weight: 800; line-height: 1.05; letter-spacing: -0.025em; text-wrap: balance"><i>Dinheiro na mão é vendaval?</i> o preço social do <i>controle sobre os controles</i></h2>
<p style="margin: 0; font-size: 17px; line-height: 1.55; color: #33456A"><b>Um estado em perspectiva</b>: opacidade e um universo jurídico contaminado transformando o dobro de recursos em um problema à coletividade no Pará.</p>
<div style="display: flex; flex-direction: column; gap: 10px; padding-top: 4px">
<a href="#iniciativas" class="btn btn-p cut" style="width: 100%">Conheça nossas iniciativas</a>
<a href="#dados" class="btn btn-s cut" style="width: 100%">Visualize e baixe os dados</a></div>
<div style="padding-top: 8px">{art}</div>
<div style="background: #FFFFFF; box-shadow: 0 1px 2px rgba(16, 33, 63, 0.06), 0 12px 32px rgba(16, 33, 63, 0.08)">{rows}
<div style="padding: 12px 18px; background: #F5F8FC; font-size: 13px; font-weight: 500; color: #3D4E6E">Atualizado em 06.10.26</div></div>
</div></section>'''

def temas():
    rows = "".join(f'''<a href="#" style="display: grid; grid-template-columns: 108px 1fr; gap: 14px; align-items: start; padding: 14px 0; border-top: 1px solid #E3E9F3; text-decoration: none; color: #10213F">
<img src="/_blob/{b}" alt="" style="display: block; width: 108px; height: 72px; object-fit: cover">
<span style="display: flex; flex-direction: column; gap: 4px; min-width: 0"><span style="display: flex; align-items: baseline; gap: 8px"><span style="flex: none; font-size: 12px; font-weight: 700; letter-spacing: 0.1em; color: #1755C5">{n}</span><span class="disp" style="font-size: 18px; font-weight: 800; line-height: 1.15; letter-spacing: -0.01em">{t}</span></span>
<span style="font-size: 14px; line-height: 1.35; color: #33456A">{l}</span></span></a>''' for n, t, l, b in TEMAS)
    return f'''<section id="temas" class="wrap" style="padding-top: 44px; padding-bottom: 44px; display: flex; flex-direction: column; gap: 8px">
<h2 class="h2">Temas</h2>
<p style="margin: 0 0 12px 0; font-size: 15px; color: #3D4E6E">Temas disponibilizados semanalmente, com videos para debate</p>
<div>{rows}</div></section>'''

def videos():
    feat = f'''<a href="#" aria-label="Assistir: O dinheiro é público. O interesse também." style="position: relative; display: block; aspect-ratio: 16 / 9; overflow: hidden; background: #2A3240; text-decoration: none; color: #FFFFFF">
<img src="/_blob/c8f07b5220c2842b9c7a7f33526732b2" alt="" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; filter: saturate(0.3) brightness(0.55) contrast(1.12)">
<span style="position: absolute; inset: 0; background: rgba(12, 22, 38, 0.18)"></span>
<span style="position: absolute; left: 5%; top: 8%; right: 5%; display: flex; align-items: center; gap: 10px"><span class="disp" style="font-size: 15px; font-weight: 800; letter-spacing: -0.02em">IDFT</span><span style="font-family: {MONO}; font-size: 8px; letter-spacing: 0.16em; color: #C9D0DA; white-space: nowrap">PROJETO DIAGONAL</span><span style="flex: 1; height: 1px; background: rgba(255, 255, 255, 0.45)"></span></span>
<span class="disp" style="position: absolute; left: 5%; top: 34%; display: flex; flex-direction: column; align-items: flex-start; gap: 3px; font-size: 22px; font-weight: 700; line-height: 1.15; letter-spacing: -0.015em"><span>O dinheiro é público.</span><span style="background: #E8F160; color: #13233B; padding: 0 5px">O interesse também.</span></span>
<span style="position: absolute; right: 5%; bottom: 8%; width: 40px; height: 40px; border: 2px solid #FFFFFF; border-radius: 50%; box-sizing: border-box; display: flex; align-items: center; justify-content: center"><svg viewBox="0 0 24 24" style="width: 16px; height: 16px; margin-left: 3px" fill="#FFFFFF" aria-hidden="true"><path d="M7 4L20 12L7 20Z"></path></svg></span></a>'''
    small = [("442bd12c2a625d77152a18cdcc28e76e", "O que não", "se pode ver.", "TRANSPARÊNCIA · PROJETO DIAGONAL", "O acelerado esvaziamento da&nbsp; informação publicamente disponível, na contramão do movimento nacional"),
             ("94ecb83c833010854438094069c71e23", "Do contrato", "ao cuidado.", "SAÚDE PÚBLICA · PROJETO DIAGONAL", "Com o mundo jurídico como aliado,&nbsp; as OSS na saúde saem de 0,6 para 1,7 bi em 3 anos - e entregando menos"),
             ("03c3f39afac8537f540008ccffb682c2", "O direito que", "não chega.", "SANEAMENTO BÁSICO · PROJETO DIAGONAL", "No estado de pior saneamento, uma atuação sem qualquer resquício de interesse público agrava o cenário")]
    cards = "".join(f'''<a href="#" style="flex: none; width: 272px; scroll-snap-align: start; display: flex; flex-direction: column; gap: 12px; text-decoration: none; color: #FFFFFF">{poster("/_blob/" + b, l1, l2, True, False)}
<span style="font-family: {MONO}; font-size: 10px; font-weight: 500; letter-spacing: 0.14em; color: #B8C2D3">{lb}</span><span style="font-size: 16px; font-weight: 600; line-height: 1.32">{tt}</span></a>''' for b, l1, l2, lb, tt in small)
    return f'''<section id="videos" style="background: #13233B; color: #FFFFFF; padding: 44px 0 40px 0">
<div class="wrap" style="display: flex; flex-direction: column; gap: 18px">
<span style="font-family: {MONO}; font-size: 11px; font-weight: 500; letter-spacing: 0.14em; color: #B8C2D3">VER. COMPREENDER. ACOMPANHAR.</span>
<h2 class="disp" style="margin: 0; font-size: 30px; font-weight: 700; line-height: 1.1; letter-spacing: -0.015em">Investigações em vídeo.</h2>
{feat}
<span style="font-family: {MONO}; font-size: 11px; font-weight: 500; letter-spacing: 0.14em; color: #B8C2D3">VISÃO GERAL · PROJETO DIAGONAL</span>
<h3 class="disp" style="margin: 0; font-size: 25px; font-weight: 700; line-height: 1.15; letter-spacing: -0.015em">Para onde vai o dinheiro público no Pará?</h3>
<p style="margin: 0; font-size: 16px; line-height: 1.5; color: #B8C2D3">Como uma arrecadação excepcional pode entregar resultados piores? um raio-X das receitas e gastos que diz muito sobre a importância do debate público informado.</p>
<a href="#" class="cut" style="display: inline-flex; align-items: center; justify-content: space-between; min-height: 52px; box-sizing: border-box; padding: 0 22px; background: #E8F160; color: #13233B; font-size: 15px; font-weight: 700; text-decoration: none">Ver prévia da capa<svg viewBox="0 0 24 24" style="width: 16px; height: 16px" fill="none" stroke="#13233B" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M7 17L17 7M9 7H17V15"></path></svg></a>
<div style="height: 1px; background: rgba(184, 194, 211, 0.25); margin: 10px 0 4px 0"></div>
<div style="display: flex; align-items: center; justify-content: space-between"><span style="font-size: 15px; font-weight: 600">Mais vídeos</span><a href="#" style="display: inline-flex; align-items: center; gap: 8px; min-height: 44px; color: #FFFFFF; font-size: 14px; font-weight: 500; text-decoration: none; border-bottom: 1px solid #B8C2D3">Explore a série{OUTL}</a></div>
</div>
<div style="display: flex; gap: 14px; overflow-x: auto; scroll-snap-type: x mandatory; padding: 4px 20px 0 20px">{cards}</div>
<p class="wrap" style="margin: 18px 0 0 0; font-family: {MONO}; font-size: 11px; color: #8E9AAF">Estudo da apresentação da série: capas e títulos demonstrativos.</p>
</section>'''

def iniciativas():
    it = [("7ef09799fcb508e8f7a22cacbe6f9fca", "A primeira ação popular, em 2020", "A primeira Ação Popular", "Conheça a ação que poderia ter evitado o dano coletivo, e as razões pelas quais o segue negado o levantamento do sigilo."),
          ("a5d872189b2ce15ee1380e24e226b3c5", "Iniciativa 2 · [nome]", "A ORCRIM exposta em 2022, na base da <i>Operação Fratria</i>", "Um retrato minucioso e profundo de uma atuação cuja continuidade inviabiliza qualquer expectativa de um futuro melhor."),
          ("406ca4b3d873bac1276f91a50ccd44f5", "Iniciativa 3 · [nome]", "As Notas Técnicas da CGU", "Veja as 6 Notas Técnicas da CGU, que confirmam todas as ilegalidades apontadas na denúncia, deixando absolutamente clara a atuação de órgãos estaduais.")]
    cards = "".join(f'''<a href="#" style="display: flex; flex-direction: column; gap: 10px; padding: 20px; background: #F5F8FC; border-top: 4px solid #1755C5; text-decoration: none; color: #10213F">
<span style="display: flex; gap: 14px; align-items: center"><img src="/_blob/{b}" alt="" style="width: 64px; height: 64px; object-fit: cover; display: block; flex: none"><span style="font-size: 11px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; color: #1755C5">{lb}</span></span>
<span class="disp" style="font-size: 20px; font-weight: 800; line-height: 1.18; letter-spacing: -0.01em">{t}</span>
<span style="font-size: 14px; line-height: 1.45; color: #33456A">{x}</span></a>''' for b, lb, t, x in it)
    return f'''<section id="iniciativas" class="wrap" style="padding-top: 44px; padding-bottom: 44px; display: flex; flex-direction: column; gap: 18px">
<div style="display: flex; flex-direction: column; gap: 8px"><span class="lbl">Da análise à atuação</span><h2 class="h2">Iniciativas</h2></div>
{cards}
<a href="#" style="display: inline-flex; align-items: center; gap: 10px; min-height: 44px; font-size: 15px; font-weight: 700; color: #1755C5; text-decoration: underline; text-underline-offset: 5px">Ver as 10 iniciativas{ARROW.format(c="#1755C5")}</a>
</section>'''

def canal():
    feats = ["Criptografia de ponta a ponta", "Sem registro de IP", "Proteção à fonte"]
    f = "".join(f'<span style="display: inline-flex; align-items: center; gap: 6px; min-height: 30px; padding: 0 10px; background: rgba(255,255,255,.08)">{x}</span>' for x in feats)
    return f'''<section id="canal" style="position: relative; overflow: hidden; background: #0B2A6B; color: #FFFFFF">
<svg viewBox="0 0 100 100" preserveAspectRatio="none" style="position: absolute; right: 0; bottom: 0; width: 100%; height: 30%" aria-hidden="true"><polygon points="100,0 100,100 0,100" fill="#13233B"></polygon></svg>
<div class="wrap" style="position: relative; padding-top: 44px; padding-bottom: 44px; display: flex; flex-direction: column; gap: 16px">
<span style="display: inline-flex; align-items: center; gap: 10px; font-family: {MONO}; font-size: 11px; font-weight: 500; letter-spacing: 0.14em; color: #E8F160">{SHIELD}CANAL SEGURO DE INFORMAÇÕES</span>
<h2 class="disp" style="margin: 0; font-size: 30px; font-weight: 800; line-height: 1.1; letter-spacing: -0.02em; text-wrap: balance">Você tem provas de desvios e ilicitudes no Pará?</h2>
<p style="margin: 0; font-size: 16px; line-height: 1.55; color: #C9D6EE">Um canal seguro criptografado para envio de informações e documentos importantes.</p>
<div style="display: flex; flex-wrap: wrap; gap: 8px; font-size: 12px; font-weight: 600; color: #C9D6EE">{f}</div>
<a href="#" class="cut" style="display: inline-flex; align-items: center; justify-content: space-between; gap: 16px; min-height: 56px; box-sizing: border-box; padding: 0 20px; margin-top: 6px; background: #E8F160; color: #13233B; font-size: 15px; font-weight: 700; text-decoration: none"><span>Enviar informação com segurança [Breve]</span>{ARROW.format(c="#13233B")}</a>
<a href="#" style="display: inline-flex; align-items: center; justify-content: center; min-height: 52px; box-sizing: border-box; padding: 0 20px; border: 1.5px solid rgba(255, 255, 255, 0.55); color: #FFFFFF; font-size: 15px; font-weight: 700; text-decoration: none; text-align: center">Saiba mais sobre o funcionamento do sistema</a>
</div></section>'''

def dados():
    tiles = "".join(f'<a href="#" class="cut" style="display: flex; align-items: center; justify-content: space-between; gap: 8px; min-height: 72px; box-sizing: border-box; padding: 0 16px; background: #EEF3FB; color: #0B2A6B; font-family: \'Red Hat Display\', \'Segoe UI\', Helvetica, sans-serif; font-size: 18px; font-weight: 800; letter-spacing: -0.01em; text-decoration: none">{x}{ARROW.format(c="#1755C5")}</a>' for x in ["Arrecadação", "Despesas", "Dados sociais", "Outros"])
    return f'''<section id="dados" class="wrap" style="padding-top: 44px; padding-bottom: 48px; display: flex; flex-direction: column; gap: 16px">
<div style="display: flex; flex-direction: column; gap: 8px"><span class="lbl">Dados</span><h2 class="h2" style="font-size: 26px">Painéis e bases para consulta [Breve]</h2><span style="font-size: 14px; color: #3D4E6E">Em preparação · exportação em CSV e Excel</span></div>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px">{tiles}</div></section>'''

body = "\n".join([header(True), hero(), diagonal(), temas(), videos(), iniciativas(), canal(), dados(), boletim(True), footer(True)])
doc = f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>IDFT — Home v3 no layout B++ (celular)</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Red+Hat+Display:wght@300..900&amp;family=Red+Hat+Text:wght@300..700&amp;family=IBM+Plex+Mono:wght@400;500&amp;display=swap">
<style>{CSS}</style>
</helmet>
<div class="pg m" style="width: 390px; overflow: hidden">
{body}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":390,"height":7000}}}}'>
class Component extends DCLogic {{
renderVals() {{
return {{}};
}}
}}
</script>
</body>
</html>
'''
with open(os.path.join(OUT, "HomeV3BMobile.dc.html"), "w", encoding="utf-8") as fh:
    fh.write(doc)
print("HomeV3BMobile.dc.html")
