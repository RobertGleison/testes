const { createApp } = Vue;

const TaskApp = {
  data() {
    return {};
  },
  methods: {
    newSearch() {
      // Reset the search input field and hide the search results section
      document.getElementById("searchInput").value = "";
      document.getElementById("registrosFiltrados").style.display = "none";
    },
  },
  delimiters: ["{", "}"],
};

createApp(TaskApp).mount("#app");
