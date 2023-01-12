function solution(id_pw, db) {
  for (info of db) {
    if (id_pw.join("") === info.join("")) return "login";
    if (id_pw[0] === info[0]) return "wrong pw";
  }
  return "fail";
}
