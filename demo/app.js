const widget = document.querySelector(".repo-pulse");
const themeButtons = document.querySelectorAll(
  ".repo-pulse__swatch[data-theme]",
);

if (widget) {
  themeButtons.forEach((button) => {
    button.addEventListener("click", () => {
      widget.dataset.theme = button.dataset.theme;

      themeButtons.forEach((themeButton) => {
        const isSelected = themeButton === button;
        themeButton.setAttribute("aria-pressed", isSelected);
      });
    });
  });
}
