function solution(progresses, speeds) {
    var answer = [];

    progresses = progresses.map((item) => 100 - item);

    speeds.forEach((item, index) => {
        progresses[index] = Math.ceil(progresses[index] / item);
    });
    
    
    let at = 0

    for(let i = 1; i < progresses.length; i++){
        if(at !== i && progresses[at] < progresses[i]){
            answer.push(i-at)
            at = i
        }
    }
    
    if(at < progresses.length){
        answer.push(progresses.length-at)
    }

    return answer;
}

