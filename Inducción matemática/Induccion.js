function first(){
    var n=1,Part1 = 2*n-1,Part2 = Math.pow(n,2);
    if (Part1 == Part2){
        var message = 'OK';
    }else{
        var message = 'BAD';
    }
return message;
}
function second(){
    var part1 = '2n - 1',part2 = 'n^2';
    var statement1 = part1.replace('n','k');
    var statement2 = part2.replace('n','k');
    return third(statement2);
}
function third(string){
    var statement3 = string+' + 2k + 1';
    var statement4 = 'k^2 + 2k + 1';
    if (statement3 == statement4){
        return statement3+' = '+statement4;
    }else{return 'BAD'}
}
console.log('2n - 1 = n^2')
console.log(first());
console.log(second());
