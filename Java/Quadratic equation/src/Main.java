import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double a = scanner.nextDouble();
        double b = scanner.nextDouble();
        double c = scanner.nextDouble();

        double a1 = Math.sqrt(Math.pow(b, 2) - (4 * a * c));
        double firstRoot = (-b + a1) / (2 * a);
        double secondRoot = (-b - a1) / (2 * a);
        System.out.println(Math.min(firstRoot, secondRoot) + " " + Math.max(firstRoot, secondRoot));
    }
}