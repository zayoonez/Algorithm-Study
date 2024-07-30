function solution(n) {
    const countOne = (n) => {
        return n.toString(2).split("1").length-1
    }
    const targetNum = countOne(n);
    while(true) {
        n++;
        if (countOne(n) == targetNum) {
            return n
        }
    }
}


// function nextBigNumber(n) {
//     var size = n.toString(2).match(/1/g).length
//     while(n++) {
//         if(size === n.toString(2).match(/1/g).length) return n
//     }
// }