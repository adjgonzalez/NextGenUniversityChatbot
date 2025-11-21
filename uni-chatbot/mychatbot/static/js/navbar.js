document.addEventListener("DOMContentLoaded", function () {
  const navLinks = document.querySelectorAll(".nav-link[data-page]");
  const contentDiv = document.getElementById("content");

  function formatPageName(page) {
    return page.replace(/_/g, " ").replace(/\b\w/g, (c) => c.toUpperCase());
  }

  function loadNavbarPage(page, pushState = true) {
    fetch(`/admissions/load/${page}/`)
      .then((res) => res.json())
      .then((data) => {
        contentDiv.innerHTML = data.html;
        if (pushState) history.pushState({ page }, "", `/admissions/${page}/`);
        document.title = "Admissions | " + formatPageName(page);
        window.scrollTo({ top: 0, behavior: "smooth" });
      })
      .catch((err) => console.error(err));
  }

  navLinks.forEach((link) => {
    link.addEventListener("click", (e) => {
      e.preventDefault();
      const page = link.dataset.page || "undergraduate"; // default to undergraduate
      loadNavbarPage(page);
    });
  });

  // Load undergraduate page by default if no page is specified
  const currentPath = window.location.pathname;
  if (currentPath.includes("/admissions/")) {
    const defaultPage = "undergraduate";
    loadNavbarPage(defaultPage, false);
  }

  // Handle back/forward for navbar
  window.addEventListener("popstate", (e) => {
    if (e.state?.page) loadNavbarPage(e.state.page, false);
  });
});
