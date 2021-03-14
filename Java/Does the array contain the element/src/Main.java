import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static boolean contains(int[] numbers, int number) {
        // write your code here
        if (numbers.length > 0){
            for (int i = 0; i < numbers.length; i++) {
                if (numbers[i] == number){
                    return true;
                }
            }
        }
        return false;
    }

    /* Do not change code below */
    @SuppressWarnings("Duplicates")
    public static void main(String[] args) {
        final Scanner scanner = new Scanner(System.in);
        final int[] numbers;
        final int k;
        if (scanner.hasNextInt()) {
            numbers = Arrays.stream(scanner.nextLine().split("\\s+"))
                    .mapToInt(Integer::parseInt)
                    .toArray();
            k = Integer.parseInt(scanner.nextLine());
        } else {
            numbers = new int[0];
            k = 10;
        }
        System.out.println(contains(numbers, k));
    }
}