import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// Cada tema = um arquivo Markdown em src/content/temas/NN-slug.md
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
