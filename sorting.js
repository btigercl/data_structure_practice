/* Algorithm	Worst-case running time	Best-case running time	Average-case running time
Selection sort	\Theta(n^2)Θ(n2)	\Theta(n^2)Θ(n2)	\Theta(n^2)Θ(n2)
Insertion sort	\Theta(n^2)Θ(n2)	\Theta(n)Θ(n)	\Theta(n^2)Θ(n2)
Merge sort	\Theta(n \lg n)Θ(nlgn)	\Theta(n \lg n)Θ(nlgn)	\Theta(n \lg n)Θ(nlgn)
Quicksort	\Theta(n^2)Θ(n​2)	\Theta(n \lg n)Θ(nlgn)	\Theta(n \lg n)Θ(nlgn)
*/


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

overall o(n2)

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

/*Merge Sort
Both merge sort and quicksort employ a common algorithmic paradigm based on recursion

Divide by finding the number qq of the position midway between pp and rr. Do this step the
 same way we found the midpoint in binary search: add pp and rr, divide by 2, and round down.
Conquer by recursively sorting the subarrays in each of the two subproblems created by the
 divide step. That is, recursively sort the subarray array[p..q] and recursively sort the subarray array[q+1..r].
Combine by merging the two sorted subarrays back into the single sorted subarray array[p..r].

Θ(nlgn)	
*/
// Takes in an array that has two sorted subarrays,
//  from [p..q] and [q+1..r], and merges the array
var merge = function(array, p, q, r) {
    // This code has been purposefully obfuscated,
    //  as you'll write it yourself in next challenge.
    var a=[],b=[],c=p,d,e;for(d=0;c<=q;d++,c++){a[d]=array[c];}for(e=0;c<=r;e++,c++){b[e]=array[c];}c=p;for(e=d=0;d<a.length&&e<b.length;){if(a[d]<b[e]){array[c]=a[d];d++;} else {array[c]=b[e]; e++;}c++; }for(;d<a.length;){array[c]=a[d];d++;c++;}for(;e<b.length;){array[c]=b[e];e++;c++;}
};


// Takes in an array and recursively merge sorts it
var mergeSort = function(array, p, r) {
    if(p < r){
        var q  = floor((p+r)/ 2);
        mergeSort(array, p, q);
        mergeSort(array, q + 1, r);
        merge(array, p, q, r);
    }
};

var array = [14, 7, 3, 12, 9, 11, 6, 2];
mergeSort(array, 0, array.length-1);
println("Array after sorting: " + array);
Program.assertEqual(array, [2, 3, 6, 7, 9, 11, 12, 14]);
var arrayTwo = [15, 42, 3, 6, 18, 1, 0, -55];
mergeSort(arrayTwo, 0, arrayTwo.length-1);
println("Array after sorting: " + arrayTwo);
Program.assertEqual(arrayTwo, [-55, 0, 1, 3, 6, 15, 18, 42]);
