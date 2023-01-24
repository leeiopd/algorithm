function solution(number, limit, power) {
  const powerList = Array(number + 1).fill(0);

  for (let i = 1; i <= number; i++) {
    let count = 1;

    while (count * i <= number) {
      powerList[i * count]++;
      count++;
    }
  }

  return powerList.reduce(
    (acc, cur, idx) => (cur > limit ? acc + power : acc + cur),
    0
  );
}
