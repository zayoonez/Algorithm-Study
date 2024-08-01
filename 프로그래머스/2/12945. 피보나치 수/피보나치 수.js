// F(n) = F(n-1) + F(n-2)
function solution(n) {
    return F(n)
}
const F = (n) => {
    const dp = new Array(n+1).fill(0);
    dp[0] = 0; dp[1] = 1;
    for (let i = 2; i <= n; i ++ ){
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567
    }
    return dp[n]
}