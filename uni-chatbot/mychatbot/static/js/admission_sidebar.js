document.addEventListener("DOMContentLoaded", function () {
  const sidebarLinks = document.querySelectorAll(".list-group-item");
  const contentArea = document.getElementById("content");

  // Breadcrumb container
  const breadcrumb = document.getElementById("admissions-breadcrumb");

  // Format page name
  function formatPageName(page) {
    return page.replace(/_/g, " ").replace(/\b\w/g, (c) => c.toUpperCase());
  }

  // Highlight active sidebar link
  function setActiveSidebar(page) {
    sidebarLinks.forEach((l) =>
      l.dataset.page === page
        ? l.classList.add("active")
        : l.classList.remove("active")
    );
  }

  // Update breadcrumb
  function updateBreadcrumb(page) {
    if (!breadcrumb) return; // skip if breadcrumb container doesn't exist
    breadcrumb.innerHTML = `
      <li class="breadcrumb-item"><a href="/">Home</a></li>
      <li class="breadcrumb-item"><a href="/admissions/">Admissions</a></li>
      <li class="breadcrumb-item active" aria-current="page">${formatPageName(
        page
      )}</li>
    `;
  }

  // Load page content dynamically
  function loadPage(page, pushState = true) {
    fetch(`/admissions/load/${page}/`)
      .then((res) => res.json())
      .then((data) => {
        contentArea.innerHTML = data.html;

        if (pushState) history.pushState({ page }, "", `/admissions/${page}/`);

        // Update tab title
        document.title = "Admissions | " + formatPageName(page);

        // Update sidebar and breadcrumb
        setActiveSidebar(page);
        updateBreadcrumb(page);

        // Scroll to top
        window.scrollTo({ top: 0, behavior: "smooth" });
      })
      .catch((err) => console.error(err));
  }

  // Determine initial page from URL
  const pathParts = window.location.pathname.split("/").filter(Boolean); // ["admissions", "graduate"]
  let currentPage = "undergraduate"; // default
  if (pathParts[0] === "admissions" && pathParts[1]) {
    currentPage = pathParts[1];
  }

  // Update URL and tab title on initial load without AJAX reload
  history.replaceState(
    { page: currentPage },
    "",
    `/admissions/${currentPage}/`
  );
  document.title = "Admissions | " + formatPageName(currentPage);
  setActiveSidebar(currentPage);

  // Click events
  sidebarLinks.forEach((link) => {
    link.addEventListener("click", (e) => {
      e.preventDefault();
      const page = link.dataset.page;
      loadPage(page);
    });
  });

  // Handle back/forward buttons
  window.addEventListener("popstate", (e) => {
    if (e.state?.page) {
      loadPage(e.state.page, false);
    }
  });
});