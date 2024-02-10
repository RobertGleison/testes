const { createApp } = Vue;

const TaskApp = {
  data() {
    return {
      term: "", // Initialize 'term' as an empty string
    };
  },
  methods: {
    searchTerm(term) {
      // Use 'term' passed from the button click to perform the search
      axios
        .get(`http://localhost:9001/search/${term}`)
        .then(() => {
          console.log("Request to endpoint was successful");
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    },
    submitForm() {
      // Call searchTerm method when form is submitted
      this.searchTerm(this.term);
    },
  },
  delimiters: ["{", "}"],
};

createApp(TaskApp).mount("#app");
