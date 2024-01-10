function solution(s) {
    let answer = [];
    let temp = [];
    for (let i = 0; i<s.length; i++) {
        //처음 나왔는지 안나왔는지 
        // 
        if(i == s.indexOf(s[i])) {
            answer.push(-1)
            temp.push(s[i])
        }
        else{
            answer.push(i - temp.lastIndexOf(s[i]))
            temp.push(s[i])
        }
    }
    return answer
}