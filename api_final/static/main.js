const { createApp } = Vue;
const TaskApp = {
  data() {
    return {
      message: "Render vue",
      searchResults: [],
    };
  },
  methods: {
    async searchTerm() {
      const term = document.getElementById("searchInput").value;
      const response = await fetch(`/search/${term}`);
      const data = await response.json();
      this.searchResults = data;
    },
    newSearch() {
      // Reset the search input field and hide the search results section
      document.getElementById("searchInput").value = "";
      document.getElementById("registrosFiltrados").style.display = "none";
    },
  },
  delimiters: ["{", "}"],
};

createApp(TaskApp).mount("#app");
