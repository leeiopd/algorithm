function solution(topping) {
    var answer = 0;
    const toppingCountR = []
    const toppingCountL = []
    const toppingSetR = new Set()
    const toppingSetL = new Set()
    
    for(let i = 0; i < topping.length; i++){
        toppingSetR.add(topping[i])
        toppingSetL.add(topping[topping.length - i -1])
        
        toppingCountR.push(toppingSetR.size)
        toppingCountL.push(toppingSetL.size)
    }
    
    toppingCountL.reverse()
    
    for(let i = 0; i < topping.length-1; i++){
        if(toppingCountR[i] === toppingCountL[i+1]) answer++;
    }
    return answer;
}