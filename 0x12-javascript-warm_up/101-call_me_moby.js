exports.callMeMoby = (x, theFunction) => {
  while (x) {
    theFunction();
    x -= 1;
  }
};
