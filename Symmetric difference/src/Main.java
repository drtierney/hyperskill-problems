import java.util.*;

class SetUtils {

    /**
     * @return symmetric difference between set1 and set2
     */
    public static <T> Set<T> symmetricDifference(Set<T> set1, Set<T> set2) {
        // write your code here
        Set<T> diff = new HashSet<T>(set1);
        diff.addAll(set2);

        Set<T> same = new HashSet<T>(set1);
        same.retainAll(set2);

        diff.removeAll(same);

        return diff;
    }

}

/* Do not change the code below */
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String strSet1 = scanner.nextLine();
        String strSet2 = scanner.nextLine();

        Set<String> set1 = new HashSet<>();
        Set<String> set2 = new HashSet<>();

        if (!Objects.equals(strSet1, "empty")) {
            Collections.addAll(set1, strSet1.split("\\s+"));
        }

        if (!Objects.equals(strSet2, "empty")) {
            Collections.addAll(set2, strSet2.split("\\s+"));
        }

        Set<String> resultSet = SetUtils.symmetricDifference(set1, set2);

        System.out.println(String.join(" ", resultSet));
    }
}