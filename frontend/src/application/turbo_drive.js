import "../styles/turbo_drive.scss";

import "@hotwired/turbo";

window.document.addEventListener("DOMContentLoaded", function () {
    window.console.log("dom ready 1");
});

document.addEventListener("turbo:load", function () {
    console.log("turbo:load");
});

document.addEventListener('turbo:before-render', () => {
    document.querySelector("#weatherwidget-io-js").remove();
});