<!-- ReadingSubmission.vue -->

<template>
  <div id="app">
    <h1>Reading Submission</h1>

    <!-- Form for submitting a reading -->
    <form @submit.prevent="submitReading">
      <label for="reading">Reading:</label>
      <input type="number" v-model="reading" required>

      <label for="timestamp">Timestamp:</label>
      <input type="datetime-local" v-model="timestamp" required>

      <button type="submit">Submit Reading</button>
    </form>

    <!-- Display factorials ordered by timestamp -->
    <div id="factorials">
      <h2>Factorials</h2>
      <ul>
        <li v-for="factorial_reading in factorials" key=factorial_reading.timestamp >
          {{ factorial_reading.timestamp }} - Reading {{ factorial_reading.reading }}: {{ factorial_reading.factorial }}, 
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      reading: '',
      timestamp: '',
      factorials: {}
    };
  },
  methods: {
    submitReading() {
      // Convert reading to integer
      const reading = parseInt(this.reading);
      if (isNaN(reading)) {
        alert('Please enter a valid reading.');
        return;
      }

      // Send a POST request to the server with the reading and timestamp
      fetch('http://localhost:5000/submit_reading', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ reading, timestamp: this.timestamp })
      })
      .then(response => response.json())
      .then(data => {
        if (data.status === 'success') {
          alert('Reading submitted successfully.');
          // Optionally, update the displayed factorials after submission
          this.getFactorials();
        } else {
          alert('Error submitting reading: ' + data.message);
        }
      })
      .catch(error => console.error('Error:', error));
    },

    getFactorials() {
      // Send a GET request to the server to retrieve factorials
      fetch('http://localhost:5000/get_factorials')
      .then(response => response.json())
      .then(data => {
        if (data.status === 'success') {
          this.factorials = data.factorials.sort((a, b) => {
          // Assuming timestamps are in ISO format, you can use Date objects for comparison
          return new Date(a.timestamp) - new Date(b.timestamp);
        });
          
        } else {
          console.error('Error:', data.message);
        }
      })
      .catch(error => console.error('Error:', error));
    }
  },
  mounted() {
    // Get and display factorials on page load
    this.getFactorials();
  }
};
</script>
