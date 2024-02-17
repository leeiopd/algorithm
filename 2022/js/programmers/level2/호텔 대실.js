function solution(book_time) {
  const checkIn = [];
  const checkOut = [];
  const rooms = [];

  book_time.sort((a, b) => {
    const timeA = a[0].split(":").map((i) => parseInt(i));
    const timeB = b[0].split(":").map((i) => parseInt(i));

    return timeA[0] * 60 + timeA[1] > timeB[0] * 60 + timeB[1] ? 1 : -1;
  });

  for (book of book_time) {
    const inTime = book[0].split(":");
    checkIn.push(parseInt(inTime[0]) * 60 + parseInt(inTime[1]));
    const outTime = book[1].split(":");
    checkOut.push(parseInt(outTime[0]) * 60 + parseInt(outTime[1]) + 10);
  }

  rooms.push(checkOut[0]);
  let index = 1;
  var answer = 1;
  while (index < book_time.length) {
    const inTime = checkIn[index];

    if (!rooms.length) {
      rooms.push(checkOut[index]);
      index++;
      answer = answer < rooms.length ? rooms.length : answer;
      continue;
    }

    if (rooms[0] > inTime) {
      rooms.push(checkOut[index]);
      rooms.sort((a, b) => (a > b ? 1 : -1));
      index++;
      answer = answer < rooms.length ? rooms.length : answer;
      continue;
    }

    rooms.shift();
    rooms.push(checkOut[index]);
    rooms.sort((a, b) => (a > b ? 1 : -1));
    index++;

    answer = answer < rooms.length ? rooms.length : answer;
  }
  return answer;
}
