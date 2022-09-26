// Write a program that will calculate the number of trailing zeros in a factorial of a given number.

// N! = 1 * 2 * 3 *  ... * N

// Be careful 1000! has 2568 digits...

function zeros (n) {
    if (n == 0){
        return n
    }
    let fac = 1
    for (let i = 1; i<=n; i++){
        fac *= i
    }
    console.log(parseInt(fac))
    let trailing_zeros = 0
    for (let i = 10; i <= 100000000000000000000000000000000; i*=10){
        if (fac % i != 0){
            return trailing_zeros
        }else{
            trailing_zeros++
        }
    }

}

console.log(zeros(5))

function findTrailingZeros(n){
    if (n == 0){
        return n
    }
    for (let i = 5; n / i >= 1; i *= 5)
        count += Math.floor(n / i);
 
    return count;

}