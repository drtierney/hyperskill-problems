import java.io.InputStream;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;

class Main {
    public static void main(String[] args) throws Exception {
        InputStream inputStream = System.in;
        byte[] bytes = inputStream.readAllBytes();
        for (byte b : bytes){
            System.out.print(b);
        }
    }
}