import { defineConfig } from 'astro/config';
import tailwind from "@astrojs/tailwind";
import vue from "@astrojs/vue";
import mdx from "@astrojs/mdx";
import AstroPWA from '@vite-pwa/astro'
import config from "tailwindcss/defaultConfig.js";
import mdx from '@astrojs/mdx';

config.pwa = {
  mode: 'production',
  base: '/',
  scope: '/',
  includeAssets: ['assets/logo.svg'],
  registerType: 'autoUpdate',
  manifest: {
    name: 'Developer',
    short_name: 'developer',
    theme_color: '#333',
    icons: [
      {
        src: 'assets/logo.svg',
        sizes: '192x192',
        type: 'image/svg',
      },
      {
        src: 'assets/logo.svg',
        sizes: '512x512',
        type: 'image/svg',
      },
      {
        src: 'assets/logo.svg',
        sizes: '512x512',
        type: 'image/svg',
        purpose: 'any maskable',
      },
    ],
  },
  workbox: {
    navigateFallback: '/',
    globPatterns: ['**/*.{css,js,html,svg,png,ico,txt,md,mdx,json,jpg,pdf}'],
  },
  devOptions: {
    enabled: true,
    navigateFallbackAllowlist: [/^\//],
  },
  experimental: {
    directoryAndTrailingSlashHandler: true,
  }
};


export default defineConfig({
  integrations: [ tailwind(),vue(), AstroPWA(config.pwa)],
  server: {
    allowedHosts: ['localhost', 'izdrail.com'],
    proxy: {
      '/backend': {
        target: 'http//127.0.0.1:12001/',
        secure: false,
        autoRewrite: true,
        changeOrigin: true,
        rewrite: (path)  => path.replace(/^\/backend/,  ''),
      },
    }
  },
  buildOptions: {
    outdir: 'dist',
    emptyOutDir: true,
    sourcemap: true,
    minify: true,
    compressHTML: false,
    minifyCSS: true,
    rollupOptions: {
      plugins: [
        vue(),
        tailwind(),
        mdx(),
      ],
    },
  },
  experimental: {
    contentLayer: true,
  },

});
