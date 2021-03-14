import java.util.Scanner;
class StringProcessor extends Thread {

    final Scanner scanner = new Scanner(System.in); // use it to read string from the standard input

    @Override
    public void run() {
        // implement this method
        while (true){
                String line = scanner.nextLine();
                if(!line.equals(line.toUpperCase())){
                    System.out.println(line.toUpperCase());
                } else {
                    System.out.println("FINISHED");
                    break;
                }
        }
    }

}