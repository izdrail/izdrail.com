<template>
  <section>
    <div class="container px-6 py-6 mx-auto text-center">
      <div class="max-w-lg mx-auto">
        <div
            class="w-full max-w-sm mx-auto mt-6 bg-transparent border rounded-md dark:border-gray-700 focus-within:border-blue-400 focus-within:ring focus-within:ring-blue-300 dark:focus-within:border-blue-300 focus-within:ring-opacity-40">
          <form @submit.prevent="extractJobs" class="p-6 flex flex-col md:flex-row">
            <div class="flex flex-col">
              <label for="link" class="hidden">Keyword</label>
              <input v-model="keyword" type="text" name="keyword" id="link" placeholder="laravel"
                     class="flex-1 h-10 px-4 py-2 m-1 text-gray-700 placeholder-gray-400 bg-transparent border-none appearance-none dark:text-white focus:outline-none focus:placeholder-transparent focus:ring-0">
            </div>
            <button type="submit"
                    class="h-10 px-4 py-2 m-1 text-white transition-colors duration-300 transform bg-blue-500 rounded-md hover:bg-blue-400 focus:outline-none focus:bg-blue-400">
              <span v-if="loading">Loading...</span>
              <span v-else>Submit</span>
            </button>
          </form>
        </div>
      </div>
    </div>

    <div v-if="loading" class="loading">
      <svg version="1.1" id="dc-spinner" xmlns="http://www.w3.org/2000/svg" x="0px" y="0px"
           viewBox="0 0 38 38" preserveAspectRatio="xMinYMin meet">
        <!-- SVG content for loading spinner -->
      </svg>
    </div>

    <div v-else class="container px-6 mx-auto mb-3">
      <div v-if="jobs.length">
        <h2>Job Results</h2>
        <ul>
          <li v-for="job in jobs" :key="job.job_url">
            <h3>{{ job.title }} at {{ job.company }}</h3>
            <p>Location: {{ job.location }}</p>
            <p>Date Posted: {{ new Date(job.date_posted).toLocaleDateString() }}</p>
            <p>Salary: {{ job.min_amount }} - {{ job.max_amount }} {{ job.currency }}</p>
            <a :href="job.job_url" target="_blank">View Job</a>
          </li>
        </ul>
      </div>
      <div v-else>No jobs found for "{{ keyword }}".</div>
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
import 'prismjs/components/prism-json';

VMdEditor.use(vuepressTheme, {
  Prism,
});

export default {
  name: 'Jobs',
  components: {
    VMdEditor,
  },
  data() {
    return {
      title: 'Jobs',
      subtitle: 'Find the latest jobs to apply for',
      loading: false,
      keyword: 'laravel',
      jobs: [],
    }
  },
  methods: {
    extractJobs() {
      // Show loading icon
      this.loading = true;

      // Check if jobs are cached for the current keyword
      const cachedJobs = localStorage.getItem(this.keyword);
      if (cachedJobs) {
        // If cached data exists, parse and use it
        this.jobs = JSON.parse(cachedJobs);
        this.loading = false;
        console.log("Loaded from cache:", this.jobs);
        return; // Exit early to use cached data
      }

      // Make API call if no cached data is found
      fetch(`https://intel.izdrail.com/jobs`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({keyword: this.keyword}),
      })
          .then(response => response.json())
          .then(response => {
            this.jobs = response.data;

            // Cache the response data
            localStorage.setItem(this.keyword, JSON.stringify(this.jobs));
            console.log("Fetched from API:", this.jobs);

            this.loading = false;
          })
          .catch(error => {
            console.log(error);
            this.loading = false;
            // TODO: show error
          });
    },
  },
  mounted() {
    console.log('Component mounted.');
    window.loadingSpeed = 35;
  },
}
</script>
