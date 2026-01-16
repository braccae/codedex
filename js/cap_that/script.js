const memeArray = [
  "img/bSi4xLb.jpeg",
  "img/6y0G7N0.jpeg",
  "img/LXnRao1.jpeg",
  "img/Qqoxh1N.jpeg"
];

const captionsArray = [
    "dank",
    "That time when you did the thing",
    "Poo poo pee pee time",
    "Its morbin time",
    "I do not do beef; I do the whole board of charcuterie"
]

let randomMeme = document.getElementById("random-meme");
let randomCaption = document.getElementById("random-caption");
let genButton = document.getElementById("generator-button");

genButton.addEventListener("click", function() {
    let randomNumMeme = Math.floor(Math.random() * memeArray.length);
    console.log(randomNumMeme)
    let randomNumCaption = Math.floor(Math.random() * captionsArray.length);
    randomMeme.src = memeArray[randomNumMeme];
    randomCaption.innerText = captionsArray[randomNumCaption];
})