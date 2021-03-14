class ThreadProcessor {
    public static void findAndStartThread(Thread... threads) throws InterruptedException {
        // implement this method
        for (Thread t : threads){
            if (t.getState() == Thread.State.NEW) {
                t.start();
                t.join();
                break;
            }
        }
    }
}