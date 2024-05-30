// Toggling the theme using button
const modeButton = document.getElementById("modeButton");

modeButton.addEventListener("click", () => {
    if (htmlElement.dataset.bsTheme === "light") {
        htmlElement.dataset.bsTheme = "dark";       // htmlElement already declared in theme.js
        localStorage.setItem("themeColor", "dark"); // localStorage already declared in theme.js
    } else {
        htmlElement.dataset.bsTheme = "light";
        localStorage.setItem("themeColor", "light");
    }
});

//Adding accurate padding
const navElement = document.querySelector("nav"); 
const ignoreNavbarDiv = document.getElementById("ignoreNavbar");
const navHeight = navElement.offsetHeight;
ignoreNavbarDiv.style.marginTop = `${navHeight + 15}px`;
