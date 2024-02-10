const { createApp } = Vue;
const TaskApp = {
  data() {
    return {
      message: "Render vue",
    };
  },
  methods: {
    searchTerm() {
      const term = document.getElementById("searchInput").value;
      // Redirect to the search route with the term
      window.location.href = `/search/${term}`;
    },
  },
  delimiters: ["{", "}"],
};

createApp(TaskApp).mount("#app");
