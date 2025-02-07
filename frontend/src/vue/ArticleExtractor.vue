<template>
  <section>
    <div class="container px-6 py-6 mx-auto text-center">
      <div class="max-w-lg mx-auto">
        <div
            class="w-full max-w-sm mx-auto mt-6 bg-transparent border rounded-md dark:border-gray-700 focus-within:border-blue-400 focus-within:ring focus-within:ring-blue-300 dark:focus-within:border-blue-300 focus-within:ring-opacity-40">
          <form @submit.prevent="extractArticle" class="p-6 flex flex-col md:flex-row">
            <div class="flex flex-col">
              <label for="link" class="hidden">Article Url</label>
              <input v-model="link" type="url" name="link" id="link" placeholder="https://"
                     class="flex-1 h-10 px-4 py-2 m-1 text-gray-700 placeholder-gray-400 bg-transparent border-none appearance-none dark:text-white focus:outline-none focus:placeholder-transparent focus:ring-0">
            </div>
            <button type="submit"
                    class="h-10 px-4 py-2 m-1 text-white transition-colors duration-300 transform bg-blue-500 rounded-md hover:bg-blue-400 focus:outline-none focus:bg-blue-400">
                    <span v-if="loading">
                      Loading...
                    </span>
              <span v-else>
                      Submit
                    </span>
            </button>
          </form>
        </div>
      </div>
    </div>
      <!-- THE Errors!-->
      <div class="w-full max-w-sm mx-auto mt-6">
        <div v-if="display_errors" class="flex w-full max-w-sm overflow-hidden bg-white rounded-lg shadow-md dark:bg-gray-800">
              <div class="flex items-center justify-center w-12 bg-red-500">
                  <svg class="w-6 h-6 text-white fill-current" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg">
                      <path d="M20 3.36667C10.8167 3.36667 3.3667 10.8167 3.3667 20C3.3667 29.1833 10.8167 36.6333 20 36.6333C29.1834 36.6333 36.6334 29.1833 36.6334 20C36.6334 10.8167 29.1834 3.36667 20 3.36667ZM19.1334 33.3333V22.9H13.3334L21.6667 6.66667V17.1H27.25L19.1334 33.3333Z" />
                  </svg>
              </div>

              <div class="px-4 py-2 -mx-3">
                  <div class="mx-3">
                      <span class="font-semibold text-red-500 dark:text-red-400">Error</span>
                      <p class="text-sm text-gray-600 dark:text-gray-200">
                          {{ errors }}
                      </p>
                  </div>
              </div>
          </div>
    </div>

    <div v-if="loading" class="loading">
      <svg
          version="1.1"
          id="dc-spinner"
          xmlns="http://www.w3.org/2000/svg"
          x="0px" y="0px"
          viewBox="0 0 38 38"
          preserveAspectRatio="xMinYMin meet"
      >
        <text x="14" y="21" font-family="Monaco" font-size="2px" style="letter-spacing:0.6" fill="grey">LOADING
          <animate
              attributeName="opacity"
              values="0;1;0" dur="1.8s"
              repeatCount="indefinite"/>
        </text>
        <path fill="#373a42" d="M20,35c-8.271,0-15-6.729-15-15S11.729,5,20,5s15,6.729,15,15S28.271,35,20,35z M20,5.203
    C11.841,5.203,5.203,11.841,5.203,20c0,8.159,6.638,14.797,14.797,14.797S34.797,28.159,34.797,20
    C34.797,11.841,28.159,5.203,20,5.203z">
        </path>

        <path fill="#373a42" d="M20,33.125c-7.237,0-13.125-5.888-13.125-13.125S12.763,6.875,20,6.875S33.125,12.763,33.125,20
    S27.237,33.125,20,33.125z M20,7.078C12.875,7.078,7.078,12.875,7.078,20c0,7.125,5.797,12.922,12.922,12.922
    S32.922,27.125,32.922,20C32.922,12.875,27.125,7.078,20,7.078z">
        </path>

        <path fill="#2AA198" stroke="#2AA198" stroke-width="0.6027" stroke-miterlimit="10" d="M5.203,20
			c0-8.159,6.638-14.797,14.797-14.797V5C11.729,5,5,11.729,5,20s6.729,15,15,15v-0.203C11.841,34.797,5.203,28.159,5.203,20z">
          <animateTransform
              attributeName="transform"
              type="rotate"
              from="0 20 20"
              to="360 20 20"
              calcMode="spline"
              keySplines="0.4, 0, 0.2, 1"
              keyTimes="0;1"
              dur="2s"
              repeatCount="indefinite"/>
        </path>

        <path fill="#859900" stroke="#859900" stroke-width="0.2027" stroke-miterlimit="10" d="M7.078,20
  c0-7.125,5.797-12.922,12.922-12.922V6.875C12.763,6.875,6.875,12.763,6.875,20S12.763,33.125,20,33.125v-0.203
  C12.875,32.922,7.078,27.125,7.078,20z">
          <animateTransform
              attributeName="transform"
              type="rotate"
              from="0 20 20"
              to="360 20 20"
              dur="1.8s"
              repeatCount="indefinite"/>
        </path>
      </svg>
    </div>

    <div v-else class="container px-6 mx-auto mb-3">
      <div v-if="showWorkflow" class="mb-10">
        <label for="title" class="block text-2xl mb-2">Workflow</label>
        <input type="text" v-model="workflow" class="w-full h-full gap-10 text-2xl text-black ">
      </div>
      <div v-if="article.title" class="mb-10">
        <label for="title" class="block text-2xl mb-2">Title</label>
        <input type="text" v-model="article.title" class="w-full h-full gap-10 text-2xl text-black ">
      </div>
      <div v-if="article.link" class="mb-10">
        <label for="title" class="block text-2xl mb-2">Source</label>
        <input type="url" v-model="article.link" class="w-full h-full gap-10 text-2xl text-black ">
      </div>
      <div v-if="article.banner" class="mb-10">
        <label for="title" class="block text-2xl mb-2">Banner</label>
        <img :src="article.banner" class="w-full h-full gap-10 text-black " alt="image">
      </div>
      <div v-if="article.banner" class="mb-10">
        <label for="title" class="block text-2xl mb-2">Banner</label>
        <input type="text" v-model="article.banner" class="w-full h-full gap-10 text-2xl text-black ">
      </div>

      <div v-if="article.markdown" class="mb-10">
       <label for="title" class="block text-2xl mb-2">Original Article</label>
       <v-md-editor v-model="article.markdown" height="400px" class="w-full h-full gap-10 text-black text-2xl mb-10"></v-md-editor>
     </div>
      <div v-if="article.tags" class="mb-10">
        <label for="title" class="block text-2xl mb-2">Tags</label>
        <input type="text" v-model="article.tags" class="w-full h-full gap-10 text-2xl text-black ">
      </div>
      <div v-if="article.title" class="mb-10 cta">
        <a type="button" class="h-10 px-4 py-2 m-1 text-white transition-colors duration-300 transform bg-blue-500 rounded-md hover:bg-blue-400 focus:outline-none focus:bg-blue-400" >Publish</a>
      </div>
    </div>
  </section>
</template>


<style>
.page-header {
  display: none;
}
</style>

<script>
console.log('seo-analyzer.vue')
import VMdEditor from '@kangc/v-md-editor';
import '@kangc/v-md-editor/lib/style/base-editor.css';
import vuepressTheme from '@kangc/v-md-editor/lib/theme/vuepress.js';
import '@kangc/v-md-editor/lib/theme/style/vuepress.css';

// Prism
import Prism from 'prismjs';
// highlight code
import 'prismjs/components/prism-json';

VMdEditor.use(vuepressTheme, {
  Prism,
});

export default {
  name: 'ArticleExtractor',
  components: {
    VMdEditor,
  },
  data() {
    return {
      title: 'SEO Analyzer',
      subtitle: 'Get a more detail SEO report for your website by contacting me directly or setup a meeting.',
      loading: false,
      display_errors: false,
      errors: '',
      link: '',
      workflow: '',
      showWorkflow: false,
      article: {
        title: '',
        link: '',
        banner: '',
        summary: '',
        markdown: '',
      },
    }
  },
  methods: {
    extractArticle() {

      this.loading = true;
      // Make API call
          fetch(`http://localhost:12001/nlp/article`, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              link: this.link,
            }),
          })
          .then(response => response.json())
          .then(response => {
            this.article.title = response.data.title;
            this.article.markdown = response.data.markdown;
            this.loading = false;
            this.display_errors=false;
          })
          .catch(error => {
            console.log(error);
            this.loading = false;
            //todo show error
            this.display_errors=true;
            this.errors = (error);
          })
    },

  },
  mounted() {
    console.log('Component mounted.')
    window.loadingSpeed = 35;
  },
}
</script>
