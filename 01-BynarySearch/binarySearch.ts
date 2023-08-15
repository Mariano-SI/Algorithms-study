function binarySearch(list: Array<any>, item: any){
    let low  = 0;
    let high = list.length -1;


    while (low <= high) {
        let mid =  Math.floor((low+high)/2);

        let test = list[mid];

        if(test == item){
            return mid;
        }
        if(test> item){
            high = mid - 1;
        }else{
            low = mid + 1
        }
    }
}

// Testes
const my_list = [1,2,3,4,5,6,7,8]      
console.log( binarySearch(my_list, 7) ) //6

const another_list = [5, 15, 30, 42, 57, 61, 75, 80, 88, 99]
console.log( binarySearch(another_list, 57) ) //4
