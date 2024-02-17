function solution(elements) {
  const doubleElements = [...elements, ...elements];
  const set = new Set();
  const addTmp = new Array(elements.length).fill(0);
  for (let i = 0; i < elements.length; i++) {
    for (let j = 0; j < elements.length; j++) {
      addTmp[j] += doubleElements[j + i];
      set.add(addTmp[j]);
    }
  }

  return set.size;
}
