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

Cloudflare Pages conectada a este repositório: comando de build `npm run build`, pasta de saída `dist`. Cada push na branch `main` publica em idft.com.br; outras branches ganham endereços de pré-visualização.

Arquivos grandes (PDFs, bases) não entram no repositório: vão para o bucket R2 (`arquivos.idft.com.br`) e são referenciados por link.
