package Multithread;

import java.util.concurrent.TimeUnit;
import java.util.concurrent.locks.AbstractQueuedSynchronizer;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
import java.util.concurrent.locks.Condition;

class Father{
    String name;
    int age;

    public Father(String name , int age){
        this.age = age;
        this.name = name;
    }

    public void older(){age ++;}
    public void young(){age --;}
}

public class TheLock {
    public static void main(String[] args) {
        // Lock为一个接口
        // Lock可以手动同步对象: 借助ReentrantLock类
        // 手动：需要用lock()方法占用，用unlock()方法手动释放
        // 由于unlock必须执行，所以一般在try中lock，在finally中unlock
        Lock lock = new ReentrantLock();
        Thread t1 = new Thread(){
            public void run(){
                try{
                    System.out.println("线程一启动");
                    System.out.println("试图占有对象lock");
                    lock.lock();
                    Thread.sleep(1000);
                }
                catch (InterruptedException e){
                    System.out.println("ERROR");
                }
                finally{
                    lock.unlock(); // 释放对象
                }
            }
        };
        t1.start();

        try{
            Thread.sleep(2000); // 先让线程一运行两秒
        }
        catch (InterruptedException e){
            System.out.println("ERROR");
        }

        Thread t2 = new Thread(){
            public void run(){
                try{
                    System.out.println("线程二启动");
                    System.out.println("试图占有对象lock");
                    lock.lock();
                    Thread.sleep(1000);
                }
                catch (InterruptedException e){
                    System.out.println("ERROR");
                }
                finally{
                    lock.unlock(); // 释放对象
                }
            }
        };
        t2.start();

        // trylock(尝试占用时间，时间单位)：在规定时间范围内试图占用（若没有参数则一直尝试占用）
        // 返回是否占用成功
        // 注意：如果失败，unlock会报错
        Thread t3 = new Thread(){
            public void run(){
                boolean locked = false;
                try{
                    System.out.println("线程一启动");
                    System.out.println("试图占有对象lock");
                    locked = lock.tryLock(1 , TimeUnit.SECONDS);
                    if(locked) System.out.println("占用成功");
                    else System.out.println("fail");
                    Thread.sleep(5000);
                }
                catch (InterruptedException e){
                    System.out.println("ERROR");
                }
                finally{
                    if(locked) lock.unlock(); // 占用成功时才释放对象
                }
            }
        };
        t3.start();

        try{
            Thread.sleep(2000);
        }
        catch (InterruptedException e){
            System.out.println("ERROR");
        }

        Thread t4 = new Thread(){
            public void run(){
                boolean locked = false;
                try{
                    System.out.println("线程二启动");
                    System.out.println("试图占有对象lock");
                    locked = lock.tryLock(1 , TimeUnit.SECONDS);
                    if(locked) System.out.println("占用成功");
                    else System.out.println("fail");
                    Thread.sleep(5000);
                }
                catch (InterruptedException e){
                    System.out.println("ERROR");
                }
                finally{
                    if(locked) lock.unlock(); // 占用成功时才释放对象
                }
            }
        };
        t4.start();


        // Lock实现线程交互
        // 途径：通过Lock得到一个Condition对象，其中
        // await方法 对应 wait方法
        // signal方法 对应 notify方法
        // signalAll方法 对应 notifyAll方法
        Condition condition = lock.newCondition(); // 注意创建Condition对象的方式
        Thread t5 = new Thread(){
            public void run(){
                try{
                    System.out.println("线程一启动");
                    System.out.println("试图占有对象lock");
                    lock.lock();
                    Thread.sleep(1000);

                    System.out.println("线程一放弃占有对象lock");
                    condition.await();
                    System.out.println("线程一重新占有对象lock");
                }
                catch (InterruptedException e){
                    System.out.println("ERROR");
                }
                finally{
                    lock.unlock();
                }
            }
        };
        t5.start();

        try{
            Thread.sleep(2000); // 先让线程一运行两秒
        }
        catch (InterruptedException e){
            System.out.println("ERROR");
        }

        Thread t6 = new Thread(){
            public void run(){
                try{
                    System.out.println("线程二启动");
                    System.out.println("试图占有对象lock");
                    lock.lock();
                    Thread.sleep(1000);
                    System.out.println("唤醒等待中的线程");
                    condition.signal();
                }
                catch (InterruptedException e){
                    System.out.println("ERROR");
                }
                finally{
                    lock.unlock(); // 释放对象
                }
            }
        };
        t6.start();

        /* 小结：Lock 和 synchronized的区别
        1、Lock是一个接口，synchronized是一个关键字
        2、Lock可以选择性的获取锁，如果一段时间获取不到，可以放弃，从而规避死锁。而synchronized不行
        3、Lock必须手动释放锁，不然会造成死锁
        */
    }
}
