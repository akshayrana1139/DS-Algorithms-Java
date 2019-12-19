package org.akshay.algorithms.sorting;

public class InsertionWithOneArray {

	static int[] array = new int[]{9,3,4,5,4,0};

	public static void main(String[] args) {
int temp = 0;
		for (int i = 0; i < array.length-1; i++) {				
				for(int j=i;j>=0;j--){
					if(array[j]>array[j+1]){
				temp = array[j];
				array[j]=array[j+1];
				array[j+1] = temp;
					}
					
					
					
				}
				
				
		}
		
		for (int i = 0; i < array.length; i++) {
			System.out.print(array[i]);
		}
}
}
