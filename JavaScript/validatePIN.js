/*
 * Match pin of 4 or 6 length.
 */
function validatePIN (pin) {
	  var nums = pin.match(/[0-9]/g);
	  return nums != null && nums.length === pin.length
	    && (pin.length === 6 || pin.length === 4);
}

