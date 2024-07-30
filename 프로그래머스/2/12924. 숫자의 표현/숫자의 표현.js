function solution(n) {
    // 홀수인 약수의 개수 . . 
    var answer = 0;

    for(var i=1; i<=n; i++) {
        if (n%i == 0 && i%2 == 1)
        answer++
     }
    return answer ;
}

