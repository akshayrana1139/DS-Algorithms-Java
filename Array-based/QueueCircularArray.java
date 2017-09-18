package org.akshay.ArrayBased;



public class QueueCircularArray {

	static int[] a = new int[5];
	int j = 2;
	int n = 0; 
	
	public void add(int x){
		if(n+1 > a.length)
		resize();
		//
		a[(j+n)%a.length] = x;
		n++;	
	}
	
	public int remove(){
		int x = a[j];
		j = (j + 1) % a.length;
		n--;
		if(a.length>=3)
			resize();
		return x;
	}
		
	
	
	
	public void resize(){
		System.out.println("resize called");
		int[] b = new int[max(1, 2*n)];
		for (int k = 0; k < n; k++)
			b[k] = a[(j+k) % a.length];
		a = b;
        j=0;
	}
	
	
private int max(int i, int k) {
	if (i>k) 
	return i;	
	else
	return k;
	}

public static void main(String[] args) {
	
	
	QueueCircularArray qc = new QueueCircularArray();

	qc.add(1);
	qc.add(2);
	qc.add(3);
	qc.add(4);
	qc.add(5);
	
	for (int i = 0; i < a.length; i++) {
		System.out.println(a[i]);
	}
	
	System.out.println("-----------------------------------");
	
System.out.println(qc.remove());
System.out.println(qc.remove());
System.out.println(qc.remove());
System.out.println(qc.remove());
System.out.println(qc.remove());
}	
	
}
