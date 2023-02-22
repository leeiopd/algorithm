function solution(data, col, row_begin, row_end) {
    var answer = 0;
    
    data.sort((A, B) => {
        if(A[col-1] === B[col-1]){
            return A[0] < B[0]? 1:-1;
        }
        return A[col-1] > B[col-1]? 1: -1;
    })
    
    const S_list = data.map((row, index)=> {
        let result = 0;
        row.forEach(i => {
            result += i % (index+1)
        })
        return result;
    })
    
    for(let i = row_begin-1; i < row_end; i++){
        let [A, B] = S_list[i].toString(2).length > answer.toString(2).length ? [S_list[i].toString(2), answer.toString(2)] : [answer.toString(2), S_list[i].toString(2)] 
        
        
        while(B.length !== A.length){
            B = '0'+B;
        }
        
        let result = '';
        
        for(let j = 0; j < A.length; j++){
            if(A[j] === '0' && B[j] === '0'){
                result += '0';
                continue;
            }
            if(A[j] !== '0' && B[j] !== '0'){
                result += '0';
                continue;
            }
            result += '1';
        }
        answer = parseInt(result, 2);
        
    }
    
    return answer;
}