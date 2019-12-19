package org.akshay.ArrayBased;

public class StackEfficient {

	static int[] a = new int[1];
	
public void push(int x){
	int[] b = new int[a.length+1];
	// resize
	System.arraycopy(a,0,b,0,a.length);
	a = b;
	a[a.length-1]=x;
}


public int pop(){
	int c = a[a.length-1];
	int[] b = new int[a.length-1];
	// resize
	System.arraycopy(a,0,b,0,a.length-1);
	a = b;
	return c;
}

	
	public static void main(String[] args) {
		
		for (int i = 0; i < a.length; i++) {
			System.out.print(a[i]);
		}
        System.out.println();
		
		new StackEfficient().push(5);
		for (int i = 0; i < a.length; i++) {
			System.out.print(a[i]);
		}
		System.out.println();
		
		
		new StackEfficient().push(6);
		for (int i = 0; i < a.length; i++) {
			System.out.print(a[i]);
		}
		System.out.println();
		
		new StackEfficient().push(7);
		for (int i = 0; i < a.length; i++) {
			System.out.print(a[i]);
		}
		System.out.println();
		
		new StackEfficient().push(8);
		for (int i = 0; i < a.length; i++) {
			System.out.print(a[i]);
		}
		System.out.println();
		
		new StackEfficient().push(9);
		
		for (int i = 0; i < a.length; i++) {
			System.out.print(a[i]);
		}
		
		System.out.println();
		
		new StackEfficient().pop();
		
		for (int i = 0; i < a.length; i++) {
			System.out.print(a[i]);
		}
		
		System.out.println();
		
		new StackEfficient().pop();
		
		for (int i = 0; i < a.length; i++) {
			System.out.print(a[i]);
		}
		System.out.println();
		
		new StackEfficient().pop();
		
		for (int i = 0; i < a.length; i++) {
			System.out.print(a[i]);
		}
		
	System.out.println();
		
		new StackEfficient().pop();
		
		for (int i = 0; i < a.length; i++) {
			System.out.print(a[i]);
		}
		
	System.out.println();
		
		new StackEfficient().pop();
		
		for (int i = 0; i < a.length; i++) {
			System.out.print(a[i]);
		}
		
		
	}
	
}
