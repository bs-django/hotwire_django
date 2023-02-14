import "../styles/main.scss";

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


document.addEventListener('turbo:submit-start', (target) => {
    console.log('turbo:submit-start');
    console.log(target);
    // here we can write JS to improve form submission experience
    // for example: disabling form submit button
    // or displaying spinner icon
});