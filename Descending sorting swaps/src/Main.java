import java.util.*;

public class Main {
    public static void main(String[] args) {
        // write your code here
        Scanner scanner = new Scanner(System.in);
        int[] numbers = Arrays.asList(scanner.nextLine()
                .split(" ")).stream()
                .mapToInt(Integer::parseInt).toArray();

        System.out.println(bubbleSortDescendingSwapCount(numbers));
    }

    public static int bubbleSortDescendingSwapCount(int[] array) {
        int count = 0;
        for (int i = 0; i < array.length - 1; i++) {
            for (int j = 0; j < array.length - i - 1; j++) {
                if (array[j] < array[j + 1]) {
                    int temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                    count++;
                }
            }
        }
        return count;
    }
}
