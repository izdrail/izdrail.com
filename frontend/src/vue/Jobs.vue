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
      <div v-if="jobs.length">
        <h2>Job Results</h2>
        <ul>
          <li v-for="job in jobs" :key="job.job_url" :class="{ 'applied': job.applied }">
            <h3>{{ job.title }} at {{ job.company }}</h3>
            <p>Location: {{ job.location }}</p>
            <p>Date Posted: {{ new Date(job.date_posted).toLocaleDateString() }}</p>
            <p>Salary: {{ job.min_amount }} - {{ job.max_amount }} {{ job.currency }}</p>
            <a :href="job.job_url" target="_blank" @click.prevent="markAsApplied(job)">View Job</a>
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

.applied {
  background-color: #d1fae5; /* Light green background for applied jobs */
  color: #064e3b; /* Darker color for applied jobs */
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
        this.loadAppliedStatus(); // Load applied status from local storage
        this.loading = false;
        console.log("Loaded from cache:", this.jobs);
        return; // Exit early to use cached data
      }

      // Make API call if no cached data is found
      fetch(`http://localhost:12001/jobs`, {
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
            this.loadAppliedStatus(); // Load applied status
            console.log("Fetched from API:", this.jobs);

            this.loading = false;
          })
          .catch(error => {
            console.log(error);
            this.loading = false;
            // TODO: show error
          });
    },
    markAsApplied(job) {
      // Mark the job as applied
      job.applied = true;

      // Save the applied status to local storage
      const appliedJobs = JSON.parse(localStorage.getItem('appliedJobs')) || [];
      appliedJobs.push(job.job_url);
      localStorage.setItem('appliedJobs', JSON.stringify(appliedJobs));
    },
    loadAppliedStatus() {
      // Load applied jobs from local storage
      const appliedJobs = JSON.parse(localStorage.getItem('appliedJobs')) || [];
      this.jobs.forEach(job => {
        job.applied = appliedJobs.includes(job.job_url); // Set applied status
      });
    },
  },
  mounted() {
    console.log('Component mounted.');
    window.loadingSpeed = 35;
  },
}
</script>
