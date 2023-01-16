function solution(polynomial) {
  let x_num = 0;
  let num = 0;

  polynomial = polynomial.split(" + ").forEach((item) => {
    if (item.indexOf("x") > -1) {
      if (item === "x") {
        x_num++;
        return;
      }

      x_num += parseInt(item.slice(0, item.length - 1));
      return;
    }

    num += parseInt(item);
  });

  x_num = x_num === 0 ? "" : x_num === 1 ? "x" : x_num.toString() + "x";
  num = num === 0 ? "" : num.toString();

  if (x_num && num) {
    return x_num + " + " + num;
  }
  if (!x_num && !num) {
    return "0";
  }

  return x_num ? x_num : num;
}
