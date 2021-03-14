import java.util.*;

class Main {
    public static void main(String[] args) {
        // put your code here
        Scanner scanner = new Scanner(System.in);
        List<Integer> list = new ArrayList<Integer>();
        String[] line = scanner.nextLine().split("\\s+");
        for (String s : line) {
            list.add(Integer.parseInt(s));
        }

        List<Integer> list2 = new ArrayList<Integer>();
        for (int i = 1; i < list.size(); i += 2){
            list2.add(list.get(i));
        }

        Collections.reverse(list2);
        list2.forEach(l2 -> System.out.print(l2 + " "));
    }
}