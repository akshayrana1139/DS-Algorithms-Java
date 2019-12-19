
import java.util.Arrays;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;

public class QuickSort {

    static int[] array = new int[] { 1, 3, 7, 5, 4, 3, 9 };

    static Integer[] array1;
    static Integer[] array2;

    public static void main(String[] args) {

        List<Integer> array1 = new LinkedList<>();
        List<Integer> array2 = new LinkedList<>();

        int pivot = 5;

        // splitting : O(n) improve splitting 
        for (int i = 0, j = 0, k = 0; i < array.length; i++) {
            if (array[i] < pivot) {
                array1.add(j, array[i]);
                j++;
            } else {
                array2.add(k, array[i]);
                k++;
            }

        }

        for (int i = 0; i < array1.size(); i++) {
            System.out.print(array1.get(i));
        }

        System.out.println();

        for (int i = 0; i < array2.size(); i++) {
            System.out.print(array2.get(i));
        }

        System.out.println();

        // Sorting : O(nlog(n))
        array1 = sort(array1);
        array2 = sort(array2);

        for (int i = 0; i < array1.size(); i++) {
            System.out.print(array1.get(i));
        }

        System.out.println();

        for (int i = 0; i < array2.size(); i++) {
            System.out.print(array2.get(i));
        }

        System.out.println();
        boolean result = array1.addAll(array2);
        for (Integer integer : array1) {
            System.out.print(integer);
        }

    }

    static public List<Integer> sort(List<Integer> array) {
        System.out.println("agya");
        int temp = 0;
        for (int i = 0; i < array.size() - 1; i++) {

            for (int j = i; j >= 0; j--) {
                if (array.get(j) > array.get(j + 1)) {

                    Integer l = array.get(j + 1);
                    array.remove(j + 1);
                    array.add(j, l);
                    //temp = array.get(j);
                    //array.set(j,array.get(j+1));
                    //array.set(j+1,temp);

                }
            }
        }
        return array;
    }
}
