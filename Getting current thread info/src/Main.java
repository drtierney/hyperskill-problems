class Info {

    public static void printCurrentThreadInfo() {
        // get the thread and print its info
        Thread currentThread = Thread.currentThread();
        System.out.println("name: " + currentThread.getName());
        System.out.println("priority: " + currentThread.getPriority());
    }
}