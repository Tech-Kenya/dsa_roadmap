/* 
Week 1
- [ ] Find the maximum and minimum element in an array

                ======= Solution ========
    - Create an array
    - Create a function
    - Loop through the array and Transverse the Array
    - Return the min and max from the function
               
*/

const testArray = [12,-5,2,3,12,34,12,21,90,80,100];

const MinMax = (arr) =>{

    //Initialise variables min and max to store the minimimum and maximum array element
    let min = arr[0]
    let max = arr[0]

    //Loop over the arr

    for(let i = 1; i<arr.length; i++){
        if(arr[i] > max){
            max = arr[i]
        }
        if(arr[i] < min){
            min = arr[i]
        }
    }
    return{max,min}
}
const result = MinMax(testArray)
console.log("Maximum number in the array is :", result.max)
console.log("Minimum number in the array is :",result.min)