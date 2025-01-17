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

let animatedCounter = (function() {
    //closure to ensure runCounter is only called once.
    let running = false;
    return function runCounter(element) {
        if (running) {
            return;
        }
        running = true;

        let startValue = Number(element.textContent);
        let maxValue = parseInt(element.getAttribute("data-val"));
        let delay;

        // add a random ammount at a random duration

        function randomCounterDelay() {
            let addValue = getRandomNumBetween(30, 200);
            let endValue = startValue + addValue;
            let duration = Math.floor(interval / addValue);
            delay = getRandomNumBetween(4000, 15000);
            setTimeout(() => {
                addOne(endValue, duration);
            }, delay);
        }

        function addOne(endValue, duration) {
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

        randomCounterDelay();
    };
})();


let valueDisplays = document.querySelectorAll(".spinner-number");
let interval = 3000

function getRandomNumBetween(min, max) {
    return Math.random() * (max - min) + min;
}

valueDisplays.forEach((valueDisplay) => {
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animatedCounter(valueDisplay);
                console.log("visible!");
                // Stop observing after the element is visible to avoid multiple triggers
                observer.unobserve(valueDisplay);
            }
        });
    });
    observer.observe(valueDisplay);
});
