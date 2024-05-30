const htmlElement = document.querySelector("html");
const themeColor = localStorage.getItem("themeColor");
// To loading the data from the localstorage
if(themeColor === "light"){
    htmlElement.dataset.bsTheme = "light";
} else {
    htmlElement.dataset.bsTheme = "dark";
}