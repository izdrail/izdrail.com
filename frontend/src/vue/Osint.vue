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
          <span>Your scan target may be one of the following. Our system will automatically detect the target type:</span>
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
      const options = {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
          'User-Agent': 'insomnia/10.0.0'
        },
        body: new URLSearchParams({
          scanname: `Scan for - ${this.query}`,
          scantarget: `${this.query}`,
          usecase: 'all',
          modulelist: '',  // Placeholder for future modules
          typelist: ''
        }),
        redirect: 'manual'
      };

      try {
        const response = await fetch('https://osint.izdrail.com/startscan', options);
        console.log(response);
        // Handle redirection
        if ([301, 303].includes(response.status)) {
          const redirectUrl = response.headers.get('Location');
          if (!redirectUrl) throw new Error('Redirect URL not found.');
          return { redirectUrl };
        }

        // Parse HTML response for scan ID
        if (response.ok) {
          const htmlContent = await response.text();
          const match = htmlContent.match(/downloadLogs\("([A-Za-z0-9]+)"\)/);

          if (!match || !match[1]) throw new Error('Scan ID not found in HTML content.');

          const extractedId = match[1];

          // Retrieve and update scan list
          const { value } = await Preferences.get({ key: 'scans' });
          const scans = value ? JSON.parse(value) : [];

          scans.push({ scanID: extractedId, name: domain });

          await Preferences.set({
            key: localdb ?? 'scans',
            value: JSON.stringify(scans)
          });

          return { extractedId };
        }

        throw new Error(`HTTP error: ${response.status}`);
      } catch (err) {
        console.error('Error during performScan:', err);
        throw new Error('An error occurred while performing the scan.');
      }
      },
  }
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
