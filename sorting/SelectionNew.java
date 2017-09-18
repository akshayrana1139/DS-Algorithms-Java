package org.akshay.algorithms.sorting;

public class SelectionNew {
	static int[] array = new int[]{64,25,12,22,11};
public static void main(String[] args) {
	
	int j,set = 0;
	for (int i = 0; i < array.length-1; i++) {
		int min = array[i];
		for (j = i+1; j < array.length; j++) {	
			if(min>array[j]){
				min=array[j];
				set = j;
			//	System.out.println("MIN->"+min);
			}
		}
		array[set]=array[i];
		array[i]=min;
		
		
		for (int k = 0; k < array.length; k++) {
			System.out.print(array[k]+" ");
		}
		System.out.println();
	}
	
	
//	Here is an example of this sort algorithm sorting five elements:
//		64 25 12 22 11 // this is the initial, starting state of the array
//
//		11 25 12 22 64 // sorted sublist = {11}
//
//		11 12 25 22 64 // sorted sublist = {11, 12}
//
//		11 12 22 25 64 // sorted sublist = {11, 12, 22}
//
//		11 12 22 25 64 // sorted sublist = {11, 12, 22, 25}
//
//		11 12 22 25 64 // sorted sublist = {11, 12, 22, 25, 64}
//
//		Selection sort animation. Red is current min. Yellow is sorted list. Blue is current item.
//		(Nothing appears changed on these last two lines because the last two numbers were already in order)
//		Selection sort can also be used on list structures that make add and remove efficient, such as a linked list. In this case it is more common to remove the minimum element from the remainder of the list, and then insert it at the end of the values sorted so far. For example:
//		64 25 12 22 11
//
//		11 64 25 12 22
//
//		11 12 64 25 22
//
//		11 12 22 64 25
//
//		11 12 22 25 64
	
	
	

	
}
}
