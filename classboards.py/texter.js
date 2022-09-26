// Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.
// Write a function in javaScript which takes an array of strings and returns an array containing each line prepended by the correct number.
// The numbering starts at 1. The format is n: string. Notice the colon and space in between.
// Examples: (Input --> Output)
// [] --> []
// ["apple", "banana", "carrott"] --> ["1: apple", "2: banana", "3: carrot"]

const texter=(arr)=>{
    outputArray = []
    for (let i = 0; i< arr.length; i++){
        let entry = `${i+1}: ${arr[i]}`
        outputArray.push(entry)
    }
    return outputArray
}


myArray= ["apple", "banana", "carrot"]
console.log(texter(myArray))
