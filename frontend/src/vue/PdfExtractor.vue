<template>
  <section>
    <div class="container px-6 py-6 mx-auto text-center">
      <div class="max-w-lg mx-auto">
        <div
            class="w-full max-w-sm mx-auto mt-6 bg-transparent border rounded-md dark:border-gray-700 focus-within:border-blue-400 focus-within:ring focus-within:ring-blue-300 dark:focus-within:border-blue-300 focus-within:ring-opacity-40">
          <form @submit.prevent="extractArticle" class="p-6 flex flex-col md:flex-row" enctype="multipart/form-data">
            <div class="flex flex-col">
              <label for="file" class="hidden">Upload PDF</label>
              <input @change="handleFileUpload" type="file" accept="application/pdf" name="file" id="file"
                     class="flex-1 h-10 px-4 py-2 m-1 text-gray-700 placeholder-gray-400 bg-transparent border-none appearance-none dark:text-white focus:outline-none focus:placeholder-transparent focus:ring-0"
                     required>
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
    <!-- loading animation paths here -->
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
      <!-- Display extracted article details -->
      <div v-if="content.markdown" class="mb-10">
        <label for="title" class="block text-2xl mb-2">Content</label>
        <v-md-editor v-model="content.markdown" height="75vh" class="w-full h-full gap-10 text-black text-2xl mb-10"></v-md-editor>
      </div>
    </div>
  </section>
</template>

<script>
import VMdEditor from '@kangc/v-md-editor';
import '@kangc/v-md-editor/lib/style/base-editor.css';
import vuepressTheme from '@kangc/v-md-editor/lib/theme/vuepress.js';
import '@kangc/v-md-editor/lib/theme/style/vuepress.css';

// Prism for syntax highlighting
import Prism from 'prismjs';
import 'prismjs/components/prism-json';

VMdEditor.use(vuepressTheme, {
  Prism,
});

export default {
  name: 'PdfExtractor',
  components: {
    VMdEditor,
  },
  data() {
    return {
      loading: false,
      file: null,
      content: {
        markdown: '',
      },
    };
  },
  methods: {
    handleFileUpload(event) {
      this.file = event.target.files[0];
    },
    extractArticle() {
      if (!this.file) {
        alert("Please upload a PDF file.");
        return;
      }

      // Show loading spinner
      this.loading = true;

      // Prepare form data
      const formData = new FormData();
      formData.append("file", this.file);

      // Make API call to FastAPI backend
      fetch(`http://localhost:12001/testing/pdf-reader/`, {
        method: 'POST',
        body: formData,
      })
          .then(response => response.json())
          .then(data => {

            console.log(data);
            this.content.markdown = data.markdown;
            this.loading = false;
          })
          .catch(error => {
            console.error(error);
            this.loading = false;
            // Handle errors
            alert("Error processing the PDF file.");
          });
    }
  }
};
</script>
