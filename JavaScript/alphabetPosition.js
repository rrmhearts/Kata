/*
 *In this kata you are required to, given a string, replace every letter with its position in the alphabet.

 If anything in the text isn't a letter, ignore it and don't return it.

 "a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)
 *
 */

function alphabetPosition(text) {
	  var position = "";
	  [...text].forEach(c => position += 
		      (c >= 'a' && c <= 'z' ? 
			            Number(c.charCodeAt(0)-96) + " " : 
			            (c >= 'A' && c <= 'Z' ?
					            Number(c.charCodeAt(0) - 64) + " " : ""
					          ) 
			          )
		    );
	  position = position.slice(0,-1);
	  return position;
}

testStr = "Hello World";
console.log(alphabetPosition(testStr));

function alphabetPositionBetter(text) {
	  return text
	    .toUpperCase()
	    .match(/[a-z]/gi)
	    .map( (c) => c.charCodeAt() - 64)
	    .join(' ');
}
