document.addEventListener("DOMContentLoaded", function () {
  const navLinks = document.querySelectorAll(".nav-link");
  const contentDiv = document.getElementById("main-content");

  navLinks.forEach((link) => {
    link.addEventListener("click", function (e) {
      e.preventDefault(); // prevent full page reload

      const page = this.getAttribute("data-page");

      // Update active class
      navLinks.forEach((l) => l.classList.remove("active"));
      this.classList.add("active");

      // Fetch partial content
      fetch(`/load_page/${page}/`)
        .then((response) => response.text())
        .then((html) => {
          contentDiv.innerHTML = html;

          // Update URL
          window.history.pushState({ page: page }, "", "/" + page + "/");

          // Update document title
          document.title = page.charAt(0).toUpperCase() + page.slice(1);
        })
        .catch((err) => console.error(err));
    });
  });

  // Handle browser back/forward
  window.addEventListener("popstate", function (e) {
    const page = e.state ? e.state.page : "home";
    fetch(`/load_page/${page}/`)
      .then((res) => res.text())
      .then((html) => (contentDiv.innerHTML = html))
      .catch((err) => console.error(err));
  });
});