package Multithread;

import java.util.LinkedList;
import java.util.concurrent.ThreadPoolExecutor; // 引入线程池
import java.util.concurrent.LinkedBlockingDeque; // 引入任务列表
import java.util.concurrent.TimeUnit;

class ThreadPool{
    int size; // 线程池大小
    LinkedList<Runnable> tasks = new LinkedList<>(); // 任务列表

    public ThreadPool(int size){
        this.size = size;

        synchronized (tasks){ // 创建多个线程
            for (int i = 0 ; i < size ; i ++){
                new TaskThread("线程" + i).start();
            }
        }
    }

    public void add(Runnable r){
        synchronized (tasks){
            tasks.add(r);
            tasks.notifyAll(); // 唤醒等待的进程
        }
    }

    class TaskThread extends Thread{
        public TaskThread(String name){
            super(name);
        }

         Runnable task;

        public void run(){
            System.out.println("启动: " + this.getName());
            while(true){
                synchronized (tasks){
                    while(tasks.isEmpty()){ // 让所有线程处于等待状态
                        try{
                            tasks.wait();
                        }
                        catch(InterruptedException e){
                            System.out.println("ERROR");
                        }
                    }
                    task = tasks.removeLast(); // 加入任务列表末尾
                }
                System.out.println(this.getName() + "执行");
                task.run();
            }
        }
    }

}

public class Pool {
    public static void main(String[] args) {
        // 线程池：
        // 准备一个空的任务容器，以及若干个处于wait的线程
        // 当有一个任务进入任务容器后，就会有一个线程被notify，并执行任务，执行完毕后等待下个任务
        // 如果短时间内有多个任务，则会唤醒多个线程分别执行
        // 在整个过程中，都不需要创建新的线程，而是循环使用这些已经存在的线程

        // 自定义线程池
        ThreadPool pool = new ThreadPool(10);
        int sleep = 1000;
        while(true){
            pool.add(new Runnable() {
                @Override
                public void run() {
                    System.out.println("OK");
                    try{
                        Thread.sleep(1000);
                    }
                    catch (InterruptedException e){
                        System.out.println("ERROR");
                    }
                }
            });
            try{
                Thread.sleep(sleep);
                sleep -= 100;
                if(sleep == 100) break;
            }
            catch (InterruptedException e){
                System.out.println("ERROR");
            }
        }
        System.out.println();

        // Java自带的线性池：ThreadPoolExecutor
        // 参数列表：(核心线程池大小，线程池最大大小，非核心线程空闲存活时间，时间单位(一般为TimeUnit.SECONDS)，任务列表(LinkedBlockingQueue<Runnable>))
        // execute方法用来添加新任务
        ThreadPoolExecutor threadPoolExecutor = new ThreadPoolExecutor(10 , 15 , 60 , TimeUnit.SECONDS , new LinkedBlockingDeque<Runnable>());
        threadPoolExecutor.execute(new Runnable() {
            @Override
            public void run() {
                System.out.println("task1");
            }
        });

        // 运行完后不会退出程序：线程池中的线程处于等待状态
    }
}
