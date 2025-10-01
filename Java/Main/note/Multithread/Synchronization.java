package Multithread;

import java.util.*;

class Human{
    String name;
    int age;

    public void older(){
        synchronized (this){ // 在方法内部使用该类对象作为同步对象，将方法的实现写进同步块中
            age ++;
        }
    }

    public void young(){
        age --;
    }

    public boolean isDead(){
        Random r  = new Random();
        return age >= r.nextInt(100);
    }

    public void live(){
        this.age ++;
        System.out.println("正在变老");
        if(this.isDead()) System.out.println(this.name + " die " + this.age);
    }
}

public class Synchronization {
    public static void main(String[] args) {
        // 同步
        // 同步问题产生的原因：上一个线程操作的结果还没完成（如修改数据），下一个线程操作就已经开始，此时下一个线程用到还不是上一个线程操作的结果
        // 此时因为后者操作结果覆盖前者，就会出现答案错误，称为脏数据
        // 解决方案一：认为规定执行顺序，上一个线程操作完成后再进行下一个线程操作

        // 解决方案二：synchronized同步对象
        // synchronized关键字的意义：当前线程独占某一个对象，如果有其他线程想要占用该对象，就会等待，直到当前线程释放占用
        // 释放同步对象的方式：synchronized块自然结束，或者有异常抛出
        // 方式一：使用Object对象辅助作为同步对象
        final Object someObj = new Object(); // 被内部类读取，变量须声明为final
        Thread th1 = new Thread(){
            public void run(){
                try{
                    System.out.println("th1线程运行");
                    synchronized (someObj){
                        System.out.println("th1占有对象");
                        Thread.sleep(1000);
                        System.out.println("th1停止占用对象");
                    }
                }
                catch(InterruptedException e){
                    System.out.println(e);
                }
            }
        };
        th1.start();

        Thread th2 = new Thread(){
            public void run(){
                try{
                    System.out.println("th2线程运行");
                    synchronized (someObj){
                        System.out.println("th2占有对象");
                        Thread.sleep(1000);
                        System.out.println("th2停止占用对象");
                    }
                }
                catch(InterruptedException e){
                    System.out.println(e);
                }
            }
        };
        th2.start();

        // 方式二：在方法内部使用该类对象作为同步对象
        final Human man = new Human();
        man.name = "YCC";
        man.age = 18;

        for

        // 方式三：在方法前加上修饰符synchronized
    }
}
