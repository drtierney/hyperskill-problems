import java.io.CharArrayWriter;
import java.io.IOException;

class Converter {
    public static char[] convert(String[] words) throws IOException {
        // implement the method
        CharArrayWriter charArrayWriter = new CharArrayWriter();
        for (String s: words) {
            charArrayWriter.write(s);
        }
        charArrayWriter.close();
        return  charArrayWriter.toCharArray();
    }
}