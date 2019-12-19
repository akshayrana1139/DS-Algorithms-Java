public class BubbleSort {

    static int[] array = new int[] { 7, 9, 5, 6, 3, 4, 8 };

    public static void main(String[] args) {
        int temp = 0;
        int count = 0;
        boolean flag = false;
        while (!flag) {
            System.out.println("FIRST CIRCLE");
            for (int i = 0; i < array.length; i++) {
                System.out.print(array[i]);
            }
            System.out.println();
            for (int i = 0; i < array.length - 1; i++) {
                if (array[i] < array[i + 1]) {
                    count++;

                    if (count == array.length - 2) {
                        flag = true;
                        break;
                    }
                } else {
                    count = 0;
                    temp = array[i];
                    array[i] = array[i + 1];
                    array[i + 1] = temp;
                }

            }

        }

    }
}
