// Build a pyramid-shaped tower given a positive integer number of floors. A tower block is represented with "*" character.

// For example, a tower with 3 floors looks like this:

// [
//   "  *  ",
//   " *** ", 
//   "*****"
// ]

function towerBuilder(nFloors) {
    let tree = []
    let width = nFloors + nFloors - 1
    for (let i = 1; i <= width; i+=2){
        
        let space = (width - i)/2
        let layer = (' '.repeat(space)) + ('*'.repeat(i)) + (' '.repeat(space))
        console.log(layer)
        tree.push(layer)
    }
    return tree
  }


console.log(towerBuilder(6))

word = `${'*'*5}`

console.log(word)