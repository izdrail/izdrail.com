import { defineConfig } from 'astro/config';
import tailwind from "@astrojs/tailwind";
import vue from "@astrojs/vue";
import AstroPWA from '@vite-pwa/astro'
import config from "tailwindcss/defaultConfig.js";

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
    globPatterns: ['**/*.{css,js,html,svg,png,ico,txt,md,json,jpg,pdf}'],
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
    proxy: {
      '/backend': {
        target: 'http://127.0.0.1:12001/',
        secure: false,
        autoRewrite: true,
        changeOrigin: true,
        rewrite: (path)  => path.replace(/^\/backend/,  'v1_0/security'),
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
      ],
    },
  },
  markdown: {
    shikiConfig: {
      // Choose from Shiki's built-in themes (or add your own)
      // https://shiki.style/themes
      theme: 'dracula',
      // Alternatively, provide multiple themes
      // See note below for using dual light/dark themes
      themes: {
        light: 'github-light',
        dark: 'github-dark',
      },
      // Disable the default colors
      // https://shiki.style/guide/dual-themes#without-default-color
      // (Added in v4.12.0)
      defaultColor: false,
      // Add custom languages
      // Note: Shiki has countless langs built-in, including .astro!
      // https://shiki.style/languages
      langs: [],
      // Add custom aliases for languages
      // Map an alias to a Shiki language ID: https://shiki.style/languages#bundled-languages
      // https://shiki.style/guide/load-lang#custom-language-aliases
      langAlias: {
        cjs: "javascript"
      },
      // Enable word wrap to prevent horizontal scrolling
      wrap: true,
      // Add custom transformers: https://shiki.style/guide/transformers
      // Find common transformers: https://shiki.style/packages/transformers
      transformers: [],
    },
  },
  });
