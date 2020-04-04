import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.Reader;
import java.util.Arrays;

class Main {
    public static void main(String[] args) throws Exception {

        try (BufferedReader reader = new BufferedReader(new InputStreamReader(System.in))) {
            // start coding here
            char[] chars = new char[100];
            reader.read(chars);

            String reverse = new StringBuilder(new String(chars)).reverse().toString();

            System.out.print(reverse.trim());
        }
    }
}