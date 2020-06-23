import java.math.BigInteger;

class DoubleFactorial {
    public static BigInteger calcDoubleFactorial(int n) {
        // type your java code here
        BigInteger m =  BigInteger.valueOf(n);
        if (m.equals(BigInteger.ZERO) || m.equals(BigInteger.ONE))
            return BigInteger.ONE;

        BigInteger i = m.multiply(calcDoubleFactorial(Integer.valueOf(String.valueOf(m.subtract(BigInteger.valueOf(2))))));
        return i;
    }
}