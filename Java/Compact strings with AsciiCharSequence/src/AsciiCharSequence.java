public class AsciiCharSequence implements java.lang.CharSequence {
    byte[] bytes;

    public AsciiCharSequence(byte[] sequence) {
        this.bytes = sequence;
    }

    @Override
    public int length() {
        return bytes.length;
    }

    @Override
    public char charAt(int i) {
        return (char) bytes[i];
    }

    @Override
    public AsciiCharSequence subSequence(int start, int end) {
        return new AsciiCharSequence(this.toString().substring(start, end).getBytes());
    }

    @Override
    public String toString() {
        return new String(this.bytes);
    }
}