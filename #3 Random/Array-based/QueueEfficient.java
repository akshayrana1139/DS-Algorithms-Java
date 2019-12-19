package org.akshay.ArrayBased;

public class QueueEfficient {

	static int[] abc = new int[50];
	static int j = 20;
	static int top = j;
	
	
	public void queue(int x){
		abc[j] = x;
		j++;
	}
	
    public int dequeue(){	
    	int z = abc[top];
    	top++;
    	return z;
	}
	
	
	
	public static void main(String[] args) {
	
		for (int i = 0; i < abc.length; i++) {
			abc[i] = 0;
		}
		
		
		for (int i = 15; i < 25; i++) {
			System.out.print(abc[i]);
		}
		
		new QueueEfficient().queue(9);
		System.out.println();
		
		for (int i = 15; i < 25; i++) {
			System.out.print(abc[i]);
		}
		
		new QueueEfficient().queue(8);
		System.out.println();
		
		for (int i = 15; i < 25; i++) {
			System.out.print(abc[i]);
		}
		
		
		new QueueEfficient().queue(7);
		System.out.println();
		
		for (int i = 15; i < 25; i++) {
			System.out.print(abc[i]);
		}
		
		System.out.println();
		System.out.println(	new QueueEfficient().dequeue());
		System.out.println(	new QueueEfficient().dequeue());
		
		System.out.println(	new QueueEfficient().dequeue());
		
		System.out.println(	new QueueEfficient().dequeue());
		
		
	}
}
