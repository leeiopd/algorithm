const NUM_TO_ALPHABET = {
  0: "a",
  1: "b",
  2: "c",
  3: "d",
  4: "e",
  5: "f",
  6: "g",
  7: "h",
  8: "i",
  9: "j",
};

function solution(age) {
  return age
    .toString()
    .split("")
    .map((item) => NUM_TO_ALPHABET[item])
    .join("");
}
