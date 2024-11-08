<template>
  <div class="container mx-auto p-6 ">

    <!-- Form -->
    <form @submit.prevent="startScan" class="space-y-6">
      <!-- Scan Target Input -->
      <div class="grid grid-cols-1 gap-6">
        <div>
          <label for="scantarget" class="block text-sm ">Scan Target</label>
          <input
              v-model="query"
              id="scantarget"
              name="scantarget"
              type="text"
              placeholder="Enter the target to scan"
              class="mt-2 block w-full border border-gray-300 rounded-lg shadow-sm p-3 focus:outline-none focus:ring-2 focus:ring-blue-500"
              :class="{'border-red-500': errorMessage}"
          />
        </div>
      </div>

      <!-- Information Panel -->
      <div class="bg-gray-100 p-6 rounded-lg shadow-lg text-sm text-gray-700">
        <div class="flex items-center mb-4">
          <i class="fas fa-question-circle mr-2 text-gray-500"></i>
          <span>Your scan target may be one of the following. SpiderFoot will automatically detect the target type:</span>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <b>Domain Name</b>: e.g., <i>example.com</i><br />
            <b>IPv4 Address</b>: e.g., <i>1.2.3.4</i><br />
            <b>IPv6 Address</b>: e.g., <i>2606:4700:4700::1111</i><br />
            <b>Hostname/Sub-domain</b>: e.g., <i>abc.example.com</i><br />
            <b>Subnet</b>: e.g., <i>1.2.3.0/24</i><br />
            <b>Bitcoin Address</b>: e.g., <i>1HesYJSP1QqcyPEjnQ9vzBL1wujruNGe7R</i>
          </div>
          <div>
            <b>E-mail address</b>: e.g., <i>bob@example.com</i><br />
            <b>Phone Number</b>: e.g., <i>+12345678901</i> (E.164 format)<br />
            <b>Human Name</b>: e.g., <i>"John Smith"</i><br />
            <b>Username</b>: e.g., <i>"jsmith2000"</i><br />
            <b>Network ASN</b>: e.g., <i>1234</i>
          </div>
        </div>
      </div>

      <!-- Error Message Display -->
      <transition name="fade">
        <div v-if="errorMessage" class="text-red-500 text-sm p-4 rounded-lg bg-red-100">
          <strong>Error: </strong>{{ errorMessage }}
        </div>
      </transition>

      <!-- Submit Button -->
      <button
          type="submit"
          :disabled="loading"
          class="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2.5 rounded-lg shadow-md transition-colors duration-200"
      >
        <span v-if="loading" class="animate-spin mr-2">🔄</span>
        Start Scan
      </button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Osint',
  data() {
    return {
      loading: false,
      query: '',
      errorMessage: null,  // For handling error messages
    };
  },
  methods: {
    async startScan() {
      try {
        this.loading = true;
        this.errorMessage = null;  // Clear any previous errors

        // Generate a default scan name based on the query value
        const scanname = `Scan for ${this.query || 'target'}`;

        // Use axios to send a POST request with both scanname and query
        const response = await axios.post('https://osint.izdrail.com/startscan', {
          scanname,
          keyword: this.query,
        });

        console.log('Scan started:', response.data); // Handling the response data
      } catch (error) {
        console.error('API request failed:', error);
        this.errorMessage = error.response?.data?.message || 'An unexpected error occurred. Please try again later.';
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<style scoped>
/* Transition animation for error message */
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>
