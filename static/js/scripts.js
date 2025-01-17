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
            return
        }
        running = true

        let startValue = Number(element.textContent);
        let maxValue = parseInt(element.getAttribute("data-val"))
        let delay = getRandomBetween(4000, 30000)
        console.log(delay)

        // how to change set interval to a new delay each time it runs?
        let totalCounter = setInterval(() => {
            // if the final max total has been reached exit
            if (startValue > maxValue) {
                clearInterval(totalCounter)
            }

            // add an ammount between 10 and 200 to the counter at random duration between 4 and 30 seconds.
            let addValue = getRandomBetween(10, 200)
            let endValue = startValue + addValue
            let duration = Math.floor(interval / addValue)

            let counter = setInterval(() => {
                startValue += 1
                element.textContent = startValue;
                if (startValue > endValue){
                    clearInterval(counter)
                }
            }, duration);
        }, delay);
    }
})();

let valueDisplays = document.querySelectorAll(".spinner-number");
let interval = 3000

function getRandomBetween(min, max) {
    return Math.random() * (max - min) + min;
}

valueDisplays.forEach((valueDisplay) => {
    const observer = new IntersectionObserver(entries => {
        if (entries[0].target.checkVisibility()) {
            animatedCounter(valueDisplay)
            console.log("visible!")
        }
    });
    observer.observe(valueDisplay)
});
