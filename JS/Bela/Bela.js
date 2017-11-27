console.log("Hello");
let line = readline();
let input = [];
while (line) {
    input.push(line);
}
let trumpScores = {
    "A" : 11,
    "K" : 4,
    "Q" : 3,
    "J" : 20,
    "T" : 10,
    "9" : 14,
    "8" : 0,
    "7" : 0};
let averageScores = {
    "A" : 11,
    "K" : 4,
    "Q" : 3,
    "J" : 2,
    "T" : 10,
    "9" : 0,
    "8" : 0,
    "7" : 0};
let cards = input.replace(/\s+$/, '').split("\n");
let conditions = cards.shift();
const trumpSuit = conditions.split(" ")[1];

function getCardType(card) {
    return card.charAt(0);
}
function checkForTrumpSuit(card) {
    return card.charAt(1) === trumpSuit;
}
function scoreCard(card) {
    let cardType = getCardType(card);
    if (checkForTrumpSuit(card)) {
        return trumpScores[cardType];
    }
    return averageScores[cardType];
}
function getScore(cards) {
    return cards.map(card => (scoreCard(card))).reduce((total, score) => (total + score));
}
print(getScore(cards));
