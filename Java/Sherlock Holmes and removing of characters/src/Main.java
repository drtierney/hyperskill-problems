import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        // put your code here
        Scanner scanner = new Scanner(System.in);
        String word1 = scanner.nextLine().toUpperCase();
        String word2 = scanner.nextLine().toUpperCase();

        Map<String, Integer> word1map = generateAlphaMap();
        Map<String, Integer> word2map = generateAlphaMap();

        fillAlphaMap(word1map, word1);
        fillAlphaMap(word2map, word2);

        int count = compareAlphaMaps(word1map, word2map);
        System.out.println(count);
    }

    public static Map<String, Integer> generateAlphaMap() {
        Map<String, Integer> map = new HashMap<>();
        for (char ch = 'A'; ch <= 'Z'; ++ch) {
            map.put(String.valueOf(ch), 0);
        }
        return map;
    }

    public static void fillAlphaMap(Map<String, Integer> map, String word) {
        for (char ch : word.toCharArray()) {
            int count = map.getOrDefault(String.valueOf(ch), 0);
            map.put(String.valueOf(ch), count + 1);
        }
    }

    private static int compareAlphaMaps(Map<String, Integer> map1, Map<String, Integer> map2) {
        int count = 0;

        for (char ch = 'A'; ch <= 'Z'; ++ch) {
            var ch1 = map1.get(String.valueOf(ch));
            var ch2 = map2.get(String.valueOf(ch));
            if (!ch1.equals(ch2)) {
                count += ch1 > ch2 ? ch1 - ch2 : ch2 - ch1;
            }
        }
        return count;
    }
}