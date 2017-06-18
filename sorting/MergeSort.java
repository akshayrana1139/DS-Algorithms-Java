package org.akshay.algorithms.sorting;

import java.util.Arrays;
import java.util.LinkedList;

public class MergeSort {

    static int[] array = new int[] { 1, 3, 7, 5, 4, 3, 9 };

    static Integer[] array1;
    static Integer[] array2;

    public static void main(String[] args) {

        int high = array.length, mid;
        if (high % 2 == 0) {
            mid = high / 2;
        } else {
            mid = high / 2 + 1;
        }
        array1 = new Integer[mid];
        array2 = new Integer[high - mid];

        // splitting : O(1) and defining mids 
        for (int i = 0, k = 0; i < array.length; i++) {
            if (i < mid)
                array1[i] = array[i];
            else {
                array2[k] = array[i];
                k++;
            }
        }

        // Sorting : O(nlog(n))
        array1 = sort(array1);
        array2 = sort(array2);

        //	LinkedList list2 = new LinkedList<>(Arrays.asList(Arrays.stream(array).boxed().collect(Collectors.toList())));
        LinkedList<Integer> list2 = new LinkedList<>(Arrays.asList(array2));

        // Merging : O(n), no need to come bak, jst go forward, as the joining array are sorted.
        for (int i = 0, j = 0; i < array.length - 1; i++) {

            if (array1[j] < list2.get(i)) {
                list2.add(i, array1[j]);
                j = j + 1;
            } else {
                continue;
            }

        }

        for (Integer integer : list2) {
            System.out.print(integer);
        }

    }

    static public Integer[] sort(Integer[] array) {
        int temp = 0;
        for (int i = 0; i < array.length - 1; i++) {
            for (int j = i; j >= 0; j--) {
                if (array[j] > array[j + 1]) {
                    temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                }

            }
        }

        return array;
    }

}
