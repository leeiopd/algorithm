function solution(numer1, denom1, numer2, denom2) {
  let numer3 = numer1 * denom2 + numer2 * denom1;
  let denom3 = denom1 * denom2;

  let i = 2;
  while (i <= denom3) {
    if (numer3 % i === 0 && denom3 % i === 0) {
      denom3 /= i;
      numer3 /= i;
      continue;
    }
    i++;
  }
  return [numer3, denom3];
}
