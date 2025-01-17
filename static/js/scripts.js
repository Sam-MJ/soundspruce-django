/*!
* Start Bootstrap - Business Frontpage v5.0.9 (https://startbootstrap.com/template/business-frontpage)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-business-frontpage/blob/master/LICENSE)
*/

// Navbar, currently active page
document.querySelectorAll(".nav-link").forEach((link) => {
    if (link.href === window.location.href) {
        link.classList.add("active");
    }
});

// Counter animation, start at text content number, go up to data-val in random increments after a random amount of time

function animatedCounter(element) {
    // add a random amount at a random duration
    let startValue = Number(element.textContent);
    let maxValue = parseInt(element.getAttribute("data-val"));
    let delay;

    function randomCounterDelay() {
        delay = getRandomNumBetween(4000, 30000);
        setTimeout(() => {
            addOne();
        }, delay);
    }

    function addOne() {
        // generate a number to add to the counter and a duration based on that number.
        // repeatedly update the counter until it has added all its numbers or has gone over the max value.
        // if it is still below the max value, call the delay
        let addValue = getRandomNumBetween(30, 200);
        let endValue = startValue + addValue;
        let duration = Math.floor(interval / addValue);

        let counter = setInterval(() => {
            startValue += 1;
            element.textContent = startValue;
            if (startValue >= endValue) {
                clearInterval(counter);
                if (startValue < maxValue) {
                    randomCounterDelay();
                }
            }
        }, duration);
    }
    addOne();
};

let valueDisplays = document.querySelectorAll(".spinner-number");
let interval = 2500;

function getRandomNumBetween(min, max) {
    return Math.random() * (max - min) + min;
}

valueDisplays.forEach((valueDisplay) => {
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animatedCounter(valueDisplay);
                // Stop observing after the element is visible to avoid multiple triggers
                observer.unobserve(valueDisplay);
            }
        });
    });
    observer.observe(valueDisplay);
});
