import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int n = scanner.nextInt();
        int k = scanner.nextInt();

        int minSeed = a;
        int maxVal = 0;

        for (int seed = a; seed <= b; seed++) {
            int curMax = 0;
            Random random = new Random(seed);

            for (int i = 0; i < n; i++) {
                int nextVal = random.nextInt(k);
                if (curMax == 0 || nextVal > curMax) {
                    curMax = nextVal;
                }
            }

            if (maxVal == 0 || curMax < maxVal) {
                maxVal = curMax;
                minSeed = seed;
            }
        }

        System.out.println(minSeed);
        System.out.println(maxVal);
    }
}