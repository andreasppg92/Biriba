function getCardPath(n) {
	filename = STATIC_URL + "cards/";

	value = n % 13;
	if (n >= 52) {
		filename += ["red", "black"][value] + "_joker.svg";
		return filename;
	} else if (value >= 0 && value < 9) {
		filename += value + 2
	} else if (value >= 9 && value < 13) {
		filename += ["jack", "queen", "king", "ace"][value - 9];
	}

	filename += "_of_";
	filename += ["spades", "hearts",  "clubs", "diamonds"][Math.floor(n / 13)];
	filename += ".svg";

	return filename;
}

function getCardObject(n, left) {
	var object = document.createElement("object");

	object.setAttribute("type", "image/svg+xml");
	object.setAttribute("data", getCardPath(n));
	object.setAttribute("id", "card" + n);
	object.setAttribute("class", "card");
	object.setAttribute("onmouseenter", "cardMouseIn(this)");
	object.setAttribute("onmouseleave", "cardMouseOut(this)");

	object.style.left = left + "px";
	object.style.top = "0px"; // Needed for moving

	return object;
}


var CARD_RATIO = 211/305;
function fillHand(cardNumbers) {
	var hand = document.getElementById("hand");
	var cardWidth = hand.offsetHeight * CARD_RATIO;
	var numOfCards = cardNumbers.length;
	var maximumCardWidth = 10;

	// Set hand width and get left
	var width;
	var left;
	if (numOfCards >= 0 && numOfCards <= maximumCardWidth) {
		width = (numOfCards + 1) * (cardWidth/2)
		left = cardWidth/2;
	} else {
		width = (maximumCardWidth + 1) * (cardWidth/2);
		left = (cardWidth/2) / (numOfCards/maximumCardWidth);
	}
	hand.style.width = width + "px";

	// Add cards
	for (i in cardNumbers) {
		var cardNumber = cardNumbers[i];
		var card = getCardObject(cardNumber, i * left);
		hand.appendChild(card);
	}
}

function loadScreen() {
    $.ajax({
		url: "?command=getPlayersHand",
		context: document.body
	}).done(function(cards) {
		var hand = JSON.parse(cards);
		fillHand(hand);
	});
}