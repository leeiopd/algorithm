function solution(arr) {
    var answer = [arr[0]];

    for (let n of arr) {
        if (n !== answer[answer.length - 1]) {
            answer.push(n);
        }
    }

    return answer;
}
