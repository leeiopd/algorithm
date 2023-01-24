function solution(survey, choices) {
  const testResult = {
    R: 0,
    T: 0,
    C: 0,
    F: 0,
    J: 0,
    M: 0,
    A: 0,
    N: 0,
  };

  const addPoint = (dissagree, agree, point) => {
    if (point === 1) testResult[dissagree] += 3;
    if (point === 2) testResult[dissagree] += 2;
    if (point === 3) testResult[dissagree] += 1;
    if (point === 5) testResult[agree] += 1;
    if (point === 6) testResult[agree] += 2;
    if (point === 7) testResult[agree] += 3;
  };

  for (let i = 0; i < survey.length; i++) {
    addPoint(survey[i][0], survey[i][1], choices[i]);
  }

  let answer = "";

  answer += testResult.R >= testResult.T ? "R" : "T";
  answer += testResult.C >= testResult.F ? "C" : "F";
  answer += testResult.J >= testResult.M ? "J" : "M";
  answer += testResult.A >= testResult.N ? "A" : "N";

  return answer;
}
