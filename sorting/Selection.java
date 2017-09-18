package org.akshay.algorithms.sorting;


public class Selection {


	static int[] array = new int[]{65,25,12,22,11};

	
	public static void main(String[] args) {
		
		int temp = 0;
		for(int i=0;i<array.length;i++){
			for (int j = i+1; j < array.length; j++) {
				if(array[i]<array[j]){
					
				}
				else{
					temp = array[i];
					array[i]=array[j];
					array[j]=temp;
				}
			}
			
			for (int k = 0; k < array.length; k++) {

				System.out.print(array[k]);	
			}
			System.out.println();
			
		}
		
	}
}
