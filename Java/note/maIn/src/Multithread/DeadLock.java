package Multithread;

public class DeadLock {
    public static void main(String[] args) {
        // 死锁：
        // 当多个进程/线程因竞争资源形成循环等待链时，每个进程都在等待其他进程释放资源，导致系统进入无法继续执行的状态
        // 线程A持有锁1并请求锁2，线程B持有锁2并请求锁1，双方互相等待
        // 死锁会使程序停滞不前
        // 典例：
        /*
        // 线程1
        synchronized(lock1) {
            synchronized(lock2) { ... }
        }
        // 线程2
        synchronized(lock2) {
            synchronized(lock1) { ... }
        }
        */

        Human man = new Human("YCC" , 18);
        Human son = new Human("ZXT" , 18);

        Thread t1 = new Thread(){
            public void run(){
                synchronized (man){
                    System.out.println("t1占有" + man.name);

                    try{
                        Thread.sleep(1000); // 让t2有足够的时间占用son
                    }
                    catch (InterruptedException e){
                        System.out.println("ERROR");
                    }

                    System.out.println("t1试图占有" + son.name);
                    synchronized (son){
                        System.out.println("OK");
                    }
                }
            }
        };
        Thread t2 = new Thread(){
            public void run(){
                synchronized (son){
                    System.out.println("t2占有" + son.name);

                    try{
                        Thread.sleep(1000); // 让t1有足够的时间占用man
                    }
                    catch (InterruptedException e){
                        System.out.println("ERROR");
                    }

                    System.out.println("t2试图占有" + man.name);
                    synchronized (man){
                        System.out.println("OK");
                    }
                }
            }
        };

        t1.start();
        t2.start();
    }
}
