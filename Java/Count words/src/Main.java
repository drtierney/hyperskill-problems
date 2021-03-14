import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.Reader;

class Main {
    public static void main(String[] args) throws Exception {
        try (Reader reader = new BufferedReader(new InputStreamReader(System.in))) {
            String s = ((BufferedReader) reader).readLine().trim();
            int counter = 0;
            if (!s.isEmpty()) {
                counter = s.split("\\W+").length;
            }
            System.out.println(counter);
        }
    }
}