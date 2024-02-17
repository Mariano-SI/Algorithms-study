function searchSmallerIndex(arr: number[]){
    let smaller:number = arr[0];
    let smallerIndex:number = 0;

    arr.forEach((num, index)=>{
        if(num < smaller){
            smaller = num;
            smallerIndex = index;
        }
    });

    return smallerIndex;
}

function selectionSort(arr: number[]){
    const sortedArray: number[] = [];

    while (arr.length > 0) {
        const smallerIndex = searchSmallerIndex(arr);
        sortedArray.push(arr.splice(smallerIndex, 1)[0]);
    }

    return sortedArray;
}

const myArray = [5,3,6,2,10]

console.log(selectionSort(myArray))  // Saída: [2, 3, 5, 6, 10]