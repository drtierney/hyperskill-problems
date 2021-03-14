import java.util.Scanner;
import java.math.BigInteger;

class Main {
    public static void main(String[] args) {
        // put your code here
        Scanner scanner = new Scanner(System.in);

        final String[] parts = scanner.nextLine().split("\\s+");

        try {
           BigInteger a = new BigInteger(parts[0]);
           BigInteger b = new BigInteger(parts[1]);
           BigInteger c = new BigInteger(parts[2]);
           BigInteger d = new BigInteger(parts[3]);

           BigInteger e = a.negate();
           e = e.multiply(b);
           e = e.add(c);
           e = e.subtract(d);
           System.out.println(e);

        } catch (Exception e) {
            System.out.println("Can't parse a big integer value");
            e.printStackTrace();
        }

    }
}