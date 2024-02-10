const { createApp } = Vue;
const TaskApp = {
  data() {
    return {
      message: "Render vue",
    };
  },
  delimiters: ["{", "}"],
};

createApp(TaskApp).mount("#app");
