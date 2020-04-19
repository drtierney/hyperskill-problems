import java.util.*;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        // write your code here
        Scanner scanner = new Scanner(System.in);

        ArrayList<Integer> intArrList = readArrayList(scanner);
        int n = scanner.nextInt();

        ArrayList<Integer> absDistArrList = new ArrayList<>();
        ArrayList<Integer> result = new ArrayList<>();

        int distance = Integer.MAX_VALUE;

        for (int i : intArrList) {
            int absDist = Math.abs(n - i);
            if (absDist < distance) {
                distance = absDist;
            }
            absDistArrList.add(absDist);
        }

        for (int j = 0; j < absDistArrList.size(); j++) {
            if (absDistArrList.get(j) == distance) {
                result.add(intArrList.get(j));
            }
        }

        Collections.sort(result);
        result.forEach((k) -> System.out.print(k + " "));

    }

    private static ArrayList<Integer> readArrayList(Scanner scanner) {
        return Arrays
                .stream(scanner.nextLine().split("\\s+"))
                .map(Integer::parseInt)
                .collect(Collectors.toCollection(ArrayList::new));
    }
}