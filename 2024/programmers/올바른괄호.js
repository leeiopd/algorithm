function solution(strings) {
    const OPEN = "(";

    let stack = 0;

    for (let s of strings) {
        stack = s === OPEN ? stack + 1 : stack - 1;

        if (stack < 0) return false;
    }

    return stack === 0 ? true : false;
}
