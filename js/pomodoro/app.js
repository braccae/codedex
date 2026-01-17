const bells = new Audio("src/bell.wav");
const startBtn = document.querySelector(".btn-start");
const pauseBtn = document.querySelector(".btn-pause");
const resetBtn = document.querySelector(".btn-reset");
const session = document.querySelector(".minutes");
const minuteDiv = document.querySelector(".minutes");
const secondDiv = document.querySelector(".seconds");
let myInterval;
let state = true;
let totalSeconds;
let paused = false;

const updateSeconds = () => {
    // code
    // const minuteDiv = document.querySelector(".minutes");
    // const secondDiv = document.querySelector(".seconds");

    totalSeconds--

    let minutesLeft = Math.floor(totalSeconds / 60);
    let secondsLeft = totalSeconds % 60;

    if (secondsLeft < 10) {
        secondDiv.textContent = "0" + secondsLeft;
    } else {
        secondDiv.textContent = secondsLeft;
    }
    minuteDiv.textContent = `${minutesLeft}`;

    if (minutesLeft === 0 && secondsLeft === 0) {
        bells.play();
        clearInterval(myInterval);
    }
};

const appTimer = () => {
    const sessionAmount = Number.parseInt(session.textContent);

    if (state) {
        state = false;
        totalSeconds = sessionAmount * 60;

        myInterval = setInterval(updateSeconds, 1000);
    } else {
        alert("Session has already started.")
    }
}

const timerPause = () => {
    if (paused === false) {
        clearInterval(myInterval);
        paused = true;
        pauseBtn.textContent = "resume";
    } else {
        myInterval = setInterval(updateSeconds, 1000);
        pauseBtn.textContent = "pause";
        paused = false;
    }
}

const timerReset = () => {
    clearInterval(myInterval);
    state = true;
    paused = false;
    pauseBtn.textContent = "pause";
    minuteDiv.textContent = "25";
    secondDiv.textContent = "00";
}

startBtn.addEventListener("click", appTimer);
pauseBtn.addEventListener("click", timerPause);
resetBtn.addEventListener("click", timerReset);
