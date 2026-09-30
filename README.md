# Site do IDFT — idft.com.br

Site estático construído com [Astro](https://astro.build). Conteúdo em Markdown, publicação automática pela Cloudflare Pages a cada alteração enviada ao repositório.

## Como editar o conteúdo

- **Temas** — um arquivo por tema em `src/content/temas/NN-slug.md`. Os campos do cabeçalho (`title`, `short`, `line`, imagens) alimentam a home, a faixa de atalhos e a página do tema; o texto abaixo do cabeçalho é o corpo da página do tema.
- **Publicações** — um arquivo por texto em `src/content/publicacoes/AAAA-MM-DD-titulo.md` (modelo em `LEIA-ME.md`). O campo `tema` liga a publicação ao tema; `draft: true` mantém o texto fora do site.
- **Páginas fixas** — `src/pages/*.astro` (sobre, iniciativas, dados, canal seguro…).
- **Imagens** — `public/img/`. As 24 colagens dos temas estão em `public/img/temas/`.
- **Vídeo da home** — em `src/pages/index.astro`, troque `<VideoPlaceholder />` por `<VideoPlaceholder youtubeId="ID_DO_VIDEO" />`.

## Rodar localmente

```bash
npm install
npm run dev      # http://localhost:4321
npm run build    # gera a pasta dist/
```

## Publicação

Projeto **idft-site** na Cloudflare Pages (conta idft.br@proton.me), conectado a este repositório (`idft-br/Idft-site`):

- endereço provisório: https://idft-site.pages.dev (o domínio idft.com.br é ligado em *Custom domains*);
- build: `npm run build`, saída `dist`, Node 22 (`.node-version`), sem variáveis de ambiente;
- cada push na branch `main` publica em ~1 minuto; outras branches ganham endereços de pré-visualização (`<branch>.idft-site.pages.dev`);
- cabeçalhos de segurança (CSP, HSTS, etc.) e cache ficam em `public/_headers`.

Arquivos grandes (PDFs, bases) não entram no repositório: vão para o bucket R2 (`arquivos.idft.com.br`) e são referenciados por link.
