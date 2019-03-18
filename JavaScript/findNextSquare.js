function findNextSquare(sq) {
  // Return the next square if sq if a perfect square, -1 otherwise
  var root = Math.floor(Math.sqrt(sq));
  return root*root == sq ? (root+1)*(root+1) : -1;
}
