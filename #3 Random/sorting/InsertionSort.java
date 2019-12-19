public class InsertionSort {

	
	static int[] array = new int[]{9,3,4,5,4,0};
	static int[] finalArray = new int[array.length];
 public static void main(String[] args) {
		
		
		finalArray[0] = array[0];
		
		for (int i = 0; i < array.length-1; i++) {
			if(finalArray[i]<array[i+1]){
				finalArray[i+1]=array[i+1]; 
			}
			
			else{
				// Doing this bcoz third digit needs to chk not only second digit, but also the first , upto the first index.
				for(int j =i;j>=0;j--){
					if (finalArray[j]>array[i+1]) {
						finalArray[j+1] = finalArray[j];
						finalArray[j]=array[i+1];
					}
				}
			}
		}
		
		for (int i = 0; i < finalArray.length; i++) {
			System.out.print(finalArray[i]);
		}
		
	}
	
	
}
