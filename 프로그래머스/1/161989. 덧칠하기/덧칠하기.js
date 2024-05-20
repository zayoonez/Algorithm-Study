function solution(n, m, section) {
    var cnt = 0;
    let painted = 0;
//     let a = section[section.length-1]-section[0]+1
    
    
//     return a%m == 0? a/m : Math.floor(a/m)+1
    for(i of section){
        if(i<painted) {
            continue;
        }
        painted = i+m;
        cnt +=1;
    }
    return cnt;
}