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
    short_name: 'izdrail',
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
  buildOptions: {
    outdir: 'dist',
    emptyOutDir: true,
    sourcemap: false,
    minify: true,
    rollupOptions: {
      plugins: [
        vue(),
        tailwind(),
      ],
    },
  },
  vite: {
    logLevel: 'info',
    ssr: {
      noExternal: [
        '@astrojs/vue',
        'astro-component-lib',
      ]
    },
    optimizeDeps: {
      include: [
        '@kangc/v-md-editor',
      ],
    },
    define: {
      __DATE__: `'${new Date().toISOString()}'`,
    },
    server: {
      fs: {
        // Allow serving files from hoisted root node_modules
        allow: ['../..']
      }
    },
  }
});
