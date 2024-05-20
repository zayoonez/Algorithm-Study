function solution(t, p) {
    let cnt = 0;
    for (let i=0; i<t.length-p.length+1; i++) {
        if(Number(p)>=Number(t.substr(i,p.length))) {
            cnt+=1
        }
    }
    return cnt

    // var answer = 0;
    // return answer;
}