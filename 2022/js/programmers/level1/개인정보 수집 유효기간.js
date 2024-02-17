function makeDateToDay(date) {
  date = date.split(".");

  const year = parseInt(date[0]) * 12 * 28;
  const month = parseInt(date[1]) * 28;
  const day = parseInt(date[2]);

  return year + month + day;
}

function termsToDay(terms) {
  newTerms = {};

  terms.forEach((item) => {
    const tmp = item.split(" ");
    newTerms[tmp[0]] = parseInt(tmp[1]) * 28;
  });

  return newTerms;
}

function solution(today, terms, privacies) {
  var answer = [];

  today = makeDateToDay(today);
  terms = termsToDay(terms);

  for (i in privacies) {
    const privacy = privacies[i].split(" ");
    const privacyDay = makeDateToDay(privacy[0]);
    const type = privacy[1];

    if (privacyDay + terms[type] <= today) {
      answer.push(parseInt(i) + 1);
    }
  }

  return answer;
}
