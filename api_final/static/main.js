const { createApp } = Vue;
const TaskApp = {
  data() {
    return {
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
      document.getElementById("searchInput").value = "";
      document.getElementById("registrosFiltrados").style.display = "none";
    },
  },
  delimiters: ["{", "}"],
};

createApp(TaskApp).mount("#app");
