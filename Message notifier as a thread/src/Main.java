import java.util.stream.IntStream;

class MessageNotifier extends Thread {

    // write fields to store variables here
    String msg;
    int repeats;

    public MessageNotifier(String msg, int repeats) {
        // implement the constructor
        this.msg = msg;
        this.repeats = repeats;
    }

    @Override
    public void run() {
        // implement the method to print the message stored in a field
        IntStream.rangeClosed(1, repeats).mapToObj(i -> msg).forEach(System.out::println);
    }
}