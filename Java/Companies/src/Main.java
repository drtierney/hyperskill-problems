import java.util.List;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        // put your code here
        Scanner scanner = new Scanner(System.in);

        List<String> myList = List.of(scanner.nextLine().split("\\s+"));

        System.out.println(myList);
    }
}