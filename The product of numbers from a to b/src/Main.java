import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        // put your code here
        Scanner scanner = new Scanner(System.in);

        long a = scanner.nextInt();
        long b = scanner.nextInt();

        long result = 1L;

        for (long i = a; i < b; i++){
            result *=i;
        }

        System.out.println(result);
    }
}