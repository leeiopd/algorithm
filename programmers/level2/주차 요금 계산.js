const timeToSecond = (date) => {
  date = date.split(":");

  return parseInt(date[0]) * 60 + parseInt(date[1]);
};

function solution(fees, records) {
  var answer = [];

  const parkings = {};
  const parkingTimes = {};

  for (record of records) {
    record = record.split(" ");
    const time = timeToSecond(record[0]);
    const car = parseInt(record[1]);
    const state = record[2];

    if (state === "IN") {
      parkings[car] = time;
      continue;
    }

    if (parkingTimes[car]) {
      parkingTimes[car] += time - parkings[car];
    } else {
      parkingTimes[car] = time - parkings[car];
    }

    delete parkings[car];
  }

  for (car in parkings) {
    if (parkingTimes[car]) {
      parkingTimes[car] += timeToSecond("23:59") - parkings[car];
    } else {
      parkingTimes[car] = timeToSecond("23:59") - parkings[car];
    }
  }

  for (car in parkingTimes) {
    if (parkingTimes[car] < fees[0]) {
      answer.push(fees[1]);
      continue;
    }

    answer.push(
      fees[1] + Math.ceil((parkingTimes[car] - fees[0]) / fees[2]) * fees[3]
    );
  }

  return answer;
}
