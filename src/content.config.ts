import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// Cada tema = um arquivo Markdown em src/content/temas/NN-slug.md
// Os campos abaixo de `order` são opcionais: quando preenchidos, a página do tema ganha
// as seções correspondentes (síntese, números, destaques, linha do tempo, figuras, vídeo, fontes).
const temas = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/temas' }),
  schema: z.object({
    n: z.string(),            // "01" … "12"
    title: z.string(),        // nome do tema
    short: z.string(),        // rótulo curto (faixa de atalhos)
    line: z.string(),         // frase-síntese exibida na home
    ampla: z.string(),        // /img/temas/NN-...-ampla.jpg
    compacta: z.string(),     // /img/temas/NN-...-compacta.jpg
    alt: z.string(),
    order: z.number(),

    // --- página do tema (opcionais) ---
    resumo: z.string().optional(),                       // parágrafo de abertura ("Em síntese")
    numeros: z.array(z.object({                          // faixa de números
      n: z.string(), l: z.string(), fonte: z.string().optional(),
    })).optional(),
    destaques: z.array(z.object({                        // "O que mais chama a atenção"
      titulo: z.string(), texto: z.string(), fonte: z.string().optional(),
    })).optional(),
    figuras: z.array(z.object({                          // documentos/imagens com legenda
      src: z.string(), alt: z.string(), legenda: z.string(), fonte: z.string().optional(),
    })).optional(),
    video: z.object({ youtubeId: z.string().optional(), titulo: z.string(), nota: z.string().optional() }).optional(),
    linha_do_tempo: z.array(z.object({
      data: z.string(), fato: z.string(), fonte: z.string().optional(),
    })).optional(),
    fontes: z.array(z.object({                           // documentos citados no texto como [doc. NN]
      id: z.string(), desc: z.string(), url: z.string().optional(),
    })).optional(),
    atualizado: z.string().optional(),                   // "30 set 2026"
  }),
});

// Publicações (investigações, peças jurídicas, dados) — um arquivo por texto
const publicacoes = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/publicacoes' }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    tema: z.string(),                       // slug do tema (ex.: "03-saude-publica")
    kind: z.enum(['Investigação', 'Peça jurídica', 'Dados', 'Análise', 'Nota']),
    summary: z.string(),
    author: z.string().optional(),
    draft: z.boolean().default(false),
  }),
});

export const collections = { temas, publicacoes };
