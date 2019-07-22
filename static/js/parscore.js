Array.prototype.has=function(v){
	for (i=0; i<this.length; i++){
		if (this[i]==v) return true;
	}
	return false;
}

function getBackgroundColor(isValid) {
	if (isValid) {
		return "#ffffff";
	} else {
		return "#ff0000";
	}
}

function checkEnteredValue(fld, questionNumber) {
	fld.style.background = getBackgroundColor(['', ' ', '0', '1', '2', '3', '4'].has(fld.value));
}

function validateTestForm(frm) {
	var allOkay = 1;
	for (key in frm.elements) {
		var element = frm.elements[key];
		//console.log(element);
		//alert(element);
		if (element != null) {
			if (element.name != null) {
				//alert(element.name + ": " + typeof(element.name));
				if (typeof(element.name) == "string" && element.name.substr(0, 1) == 'q') {
					var v = element.value;
					
					isValid = ['', ' ', '0', '1', '2', '3', '4'].has(fld.value)
					element.style.background = getBackgroundColor(isValid);
					if (!isValid) {
						allOkay = 0;
					}
				}
			}
		}
	}
	if (allOkay == 0) {
		alert ('Please correct the scores for the colored items.');
		return false;
	}

	return true;
}

function checkThreePQEnteredValue(fld, questionNumber) {
	fld.style.background = getBackgroundColor(['', ' ', '0', '1', '2', '3', '4', '5'].has(fld.value));
}

function validateThreePQForm(fld) {
	var allOkay = 1;
	for (key in frm.elements) {
		var element = frm.elements[key];
		//console.log(element);
		//alert(element);
		if (element != null) {
			if (element.name != null) {
				//alert(element.name + ": " + typeof(element.name));
				if (typeof(element.name) == "string" && element.name.substr(0, 1) == 'q') {
					var v = element.value;
					
					isValid = ['', ' ', '0', '1', '2', '3', '4', '5'].has(element.value);
					element.style.background = getBackgroundColor(isValid);
					alert("value=(' + element.value + ')");
					if (!isValid) {
						allOkay = 0;
					}
				}
			}
		}
	}
	if (allOkay == 0) {
		alert ('Please correct the scores for the colored items.');
		return false;
	}

	return true;
}

function checkSUQEnteredValue(fld, questionNumber) {
	var isValid = false;
	if (questionNumber == 1) {
		isValid = ['', ' ', '0', '1', '2', '3', '4', '5', '6'].has(fld.value);
		fld.style.background = getBackgroundColor(isValid);
	} else {
		isValid = ['0', '1', '2', '3'].has(fld.value);
		fld.style.background = getBackgroundColor(isValid);
	}
	return isValid;
}

function validateSUQForm(frm) {
	var allOkay = true;
	for (var questionNumber = 1; questionNumber <= 5; questionNumber++) {
		var fld = document.getElementById('q' + questionNumber);
		if (allOkay) {
			allOkay = checkSUQEnteredValue(fld, questionNumber);
		} else {
			checkSUQEnteredValue(fld, questionNumber);
		}
	}

	if (allOkay == false) {
		alert ('Please correct the scores for the colored items.');
		return false;
	}

	return true;
}

function checkPPQEnteredValue(fld, questionNumber) {
	var isValid = false;
	if (questionNumber == 1) {
		// Do nothing for first question...shouldn't even be called
	} else if (questionNumber == 2) {
		isValid = ['', ' ', '0', '1', '2', '3', '4', '5'].has(fld.value);
		fld.style.background = getBackgroundColor(isValid);
	} else {
		isValid = ['', ' ', '0', '1', '2', '3', '4'].has(fld.value);
		fld.style.background = getBackgroundColor(isValid);
	}
	return isValid;
}

function validatePPQForm(frm) {
	var allOkay = true;
	for (var questionNumber = 2; questionNumber <= 23; questionNumber++) {
		var fld = document.getElementById('q' + questionNumber);
		if (allOkay) {
			allOkay = checkPPQEnteredValue(fld, questionNumber);
		} else {
			checkPPQEnteredValue(fld, questionNumber);
		}
	}

	if (allOkay == false) {
		alert ('Please correct the scores for the colored items.');
		return false;
	}

	return true;
}

function togglePPQNever() {
	var cb = document.getElementById('q1');
	for (var questionNumber = 2; questionNumber <= 27; questionNumber++) {
		var fld = document.getElementById('q' + questionNumber);
		fld.disabled = cb.checked;
	}
}

function toggleParentPPQNever() {
	var cb = document.getElementById('q5');
	for (var questionNumber = 6; questionNumber <= 31; questionNumber++) {
		var fld = document.getElementById('q' + questionNumber);
		fld.disabled = cb.checked;
	}
}

function checkParentPPQEnteredValue(fld, questionNumber) {
	var isValid = false;
	if (questionNumber < 6) {
		// Do nothing for first question...shouldn't even be called
	} else if (questionNumber == 6) {
		isValid = ['', ' ', '0', '1', '2', '3', '4', '5'].has(fld.value);
		fld.style.background = getBackgroundColor(isValid);
	} else {
		isValid = ['', ' ', '0', '1', '2', '3', '4'].has(fld.value);
		fld.style.background = getBackgroundColor(isValid);
	}
	return isValid;
}

function validateParentPPQForm(frm) {
	var allOkay = true;
	for (var questionNumber = 6; questionNumber <= 27; questionNumber++) {
		var fld = document.getElementById('q' + questionNumber);
		if (allOkay) {
			allOkay = checkParentPPQEnteredValue(fld, questionNumber);
		} else {
			checkParentPPQEnteredValue(fld, questionNumber);
		}
	}

	if (allOkay == false) {
		alert ('Please correct the scores for the colored items.');
		return false;
	}

	return true;
}

