
<style>

.pill {
    display: flex;
    padding: 0.5rem 1rem;
    gap: 0.5rem;
    color: var(--accent-text-over);
    border: 1px solid var(--accent-regular);
    background-color: var(--accent-regular);
    border-radius: 999rem;
    font-size: var(--text-md);
    line-height: 1.35;
    white-space: nowrap;
}
.roles {
  margin-top: 0.5rem;
  display: flex;
  max-width: 75vw;
  gap: 0.5rem;
  flex-wrap: wrap;
}
</style>

<template>
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
          repeatCount="indefinite" />
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
          repeatCount="indefinite" />
    </path>
    </svg>
  </div>

  <div class="roles">
    <div v-for="keyword in response" class="pill">
      <a class="dark:text-white text-white" :href="`https://news.google.com/search?q=${keyword['keyword']}&hl=en-GB&gl=GB&ceid=GB:en`" :title="keyword" target="_blank">
      {{ keyword['keyword'] }}
      </a>
    </div>
  </div>

</template>

<script>
console.log('trending-now.vue')
export default {
  name: 'TrendingNow',
  data() {
    return {
      loading: true,
      response: [],
      display_errors: false,
      errors: '',
    }
  },
  methods: {
    getReport() {
      // Show loading icon
      this.loading = true;
      // Make API call
      fetch(`http://localhost:12001/google/trending`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      })
          .then(response => response.json())
          .then(response => {
            console.log(response.data);
            this.loading = false;
            this.render_report = true;
            this.response = response.data;

          })
          .catch(error => {
            console.log(error);
            this.display_errors = true;
            this.errors = error;
            this.loading = false;
          });
    },
  },
  created() {
    console.log('Component mounted.')
    this.getReport();
  },
}

</script>
