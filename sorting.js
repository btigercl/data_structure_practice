//javascript practice for sorts- praticing on Khan and on own 

var insert = function(array, rightIndex, value) {
    for(var j = rightIndex;
        j >= 0 && array[j] > value;
        j--) {
        array[j + 1] = array[j];
    }   
    array[j + 1] = value; 
};

var insertionSort = function(array) {
	for(var i = 1; i < array.length; i++){
		insert(array, i - 1, array[i]);
	}
};

var array = [22, 11, 99, 88, 9, 7, 42];
insertionSort(array);
println("Array after sorting:  " + array);
//Program.assertEqual(array, [7, 9, 11, 22, 42, 88, 99]);


Selection Sort 
var swap = function(array, firstIndex, secondIndex) {
    var temp = array[firstIndex];
    array[firstIndex] = array[secondIndex];
    array[secondIndex] = temp;
};

var indexOfMinimum = function(array, startIndex) {

    var minValue = array[startIndex];
    var minIndex = startIndex;

    for(var i = minIndex + 1; i < array.length; i++) {
        if(array[i] < minValue) {
            minIndex = i;
            minValue = array[i];
        }
    } 
    return minIndex;
}; 

/*Selection Sort 
Run Time == 
The running time for all the calls to indexOfMinimum O(n2).
The running time for all the calls to swap(each call to swap takes constant time) O(n).
The running time for the rest of the loop in the selectionSort function(calls swap which takes constant time) O(n).


*/
 
var selectionSort = function(array) {
    var minIndex;
    for(var i = 0; i < array.length ; i ++){
        minIndex = indexOfMinimum(array, i );
        swap(array, i, minIndex); 
    }
};

var array = [22, 11, 99, 88, 9, 7, 42];
selectionSort(array);
println("Array after sorting:  " + array);

Program.assertEqual(array, [7, 9, 11, 22, 42, 88, 99]);

var zero = [5, -1, 0, 4, 9, 10];
selectionSort(zero);
println("Array after sorting:  " + array);
Program.assertEqual(zero, [-1, 0, 4, 5, 9, 10]);
