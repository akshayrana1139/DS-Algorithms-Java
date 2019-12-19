package org.akshay.ArrayBased;

public class QueueStackDeque {

	static public int[] array = new int[1];
	
	public void queue(int x){
		add(array.length,x);
	}
	
	public int dequeue(){
		int x = array[1];
		remove(1);
		return x;
	}
	
	
	public void push(int x){
		add(1,x);
	}
	
	public int pop(){
		int x = array[1];
		remove(1);
		return x;
	}
	
	public void add(int i, int x){
		if(i>=array.length)
		grow(array.length+(i-array.length)+1);
		else
			grow(array.length+1);
		for (int j = array.length-1; j > i; j--) {	
			array[j] = array[j-1];
		}
		array[i] = x;
	}
	
	public void remove(int i){
		
		if(i<array.length){
			for (int j = i; j < array.length-1; j++) {
				
				array[j]=array[j+1];
			}
			shrink(array.length-1);
		}
		else{
			System.out.println("Index does not exist in Array");
		}
	}
	
	public void grow(int j){	
		//System.out.println(j);
		int[] b = new int[j];
		for (int i = 0; i < array.length; i++) {
			b[i]=array[i];
		}
		array=b;
	}
	
	public void shrink(int j){	
		int[] b = new int[j];
		for (int i = 0; i < b.length; i++) {
			b[i]=array[i];
		}
		array=b;
	}
	
	public static void main(String[] args) {

		QueueStackDeque q = new QueueStackDeque();
		//q.push(5);
		//q.push(6);
		//q.push(9);
	
		q.add(5, 9);
		q.add(7, 3);
		
		q.remove(5);
		
	for (int i = 1; i < array.length; i++) {
		System.out.println(array[i]);
	}
		
		
//System.out.println("Popping"+q.pop());

	}
}
