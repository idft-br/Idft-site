// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://idft.com.br',
  trailingSlash: 'never',
  build: { format: 'file' },
  integrations: [sitemap()],
});
