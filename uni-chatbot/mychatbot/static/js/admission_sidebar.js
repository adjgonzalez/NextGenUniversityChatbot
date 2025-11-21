document.addEventListener("DOMContentLoaded", function () {
  const sidebarLinks = document.querySelectorAll(".list-group-item[data-page]");
  const contentDiv = document.getElementById("content");
  const breadcrumb = document.getElementById("admissions-breadcrumb");

  function formatPageName(page) {
    return page.replace(/_/g, " ").replace(/\b\w/g, (c) => c.toUpperCase());
  }

  function setActiveSidebar(page) {
    sidebarLinks.forEach((link) =>
      link.classList.toggle("active", link.dataset.page === page)
    );
  }

  function updateBreadcrumb(page) {
    if (!breadcrumb) return;
    breadcrumb.innerHTML = `
      <li class="breadcrumb-item"><a href="/">Home</a></li>
      <li class="breadcrumb-item"><a href="/admissions/">Admissions</a></li>
      <li class="breadcrumb-item active" aria-current="page">${formatPageName(page)}</li>
    `;
  }

  function loadSidebarPage(page, pushState = true) {
    fetch(`/admissions/load/${page}/`)
      .then((res) => res.json())
      .then((data) => {
        contentDiv.innerHTML = data.html;
        if (pushState) history.pushState({ page }, "", `/admissions/${page}/`);
        document.title = "Undergraduate | " + formatPageName(page);
        setActiveSidebar(page);
        updateBreadcrumb(page);
        window.scrollTo({ top: 0, behavior: "smooth" });
      })
      .catch((err) => console.error(err));
  }

  // Default load for Undergraduate
  const currentPath = window.location.pathname;
  if (currentPath === "/admissions/" || currentPath === "/admissions") {
    loadSidebarPage("undergraduate", false);
  }

  sidebarLinks.forEach((link) => {
    link.addEventListener("click", (e) => {
      e.preventDefault();
      loadSidebarPage(link.dataset.page);
    });
  });

  window.addEventListener("popstate", (e) => {
    if (e.state?.page) loadSidebarPage(e.state.page, false);
  });
});
