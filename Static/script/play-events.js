CARD_MOVE_LEFT_OFFSET = 10;
CARD_MOVE_TOP_OFFSET = 10;

// Binding in constructino
function cardMouseIn(card) {
	var left = card.style.left;
	var top = card.style.top;

	left = parseInt(left.slice(0, -2));
	left -= CARD_MOVE_LEFT_OFFSET;
	left += "px";

	top = parseInt(top.slice(0, -2));
	top -= CARD_MOVE_TOP_OFFSET;
	top += "px";

	card.style.left = left;
	card.style.top = top;
}

function cardMouseOut(card) {
	var left = card.style.left;
	var top = card.style.top;


	left = parseInt(left.slice(0, -2));
	left += CARD_MOVE_LEFT_OFFSET;
	left += "px";

	top = parseInt(top.slice(0, -2));
	top += CARD_MOVE_TOP_OFFSET;
	top += "px";

	card.style.left = left;
	card.style.top = top;
}