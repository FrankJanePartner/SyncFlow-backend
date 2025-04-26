function opentab(selector) {
  const elements = document.querySelectorAll(selector);

  elements.forEach(el => {
    if (el.style.display === "none" || getComputedStyle(el).display === "none") {
      el.style.display = "block";
    } else {
      el.style.display = "none";
    }
  });
}
