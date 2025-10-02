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

    public Human(String name , int age){
        this.name = name;
        this.age = age;
    }

    public synchronized boolean isDead(){ // 直接在方法前加上synchronized，可以达到和方式二一样的效果
        return age >= 50 ;
    }

    public String toString(){
        return name + " " + age;
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

        // 方式二：使用该类对象作为同步对象
        final Human man = new Human("YCC" , 18);
        List<Thread> threads1 = new ArrayList<>();
        List<Thread> threads2 = new ArrayList<>();

        for (int i = 0 ; i <= 9 ; i ++){
            int t = i;
            Thread th3 = new Thread(){
                public void run(){
                    synchronized (man){ // 方法一：直接用该类对象作为同步对象
                        man.young();
                    }

                    try{
                        Thread.sleep(200);
                    }
                    catch (InterruptedException e){
                        System.out.println("ERROR");
                    }
                }
            };
            threads1.add(th3);
        }

        for(int i = 0 ; i <= 9 ; i ++){
            int t = i;
            Thread th3 = new Thread(){
                public void run(){
                    man.older(); // 方法二：在方法内部使用该类对象作为同步对象
                }
            };
            try{
                Thread.sleep(200);
            }
            catch (InterruptedException e){
                System.out.println("ERROR");
            }
            threads2.add(th3);
        }

        for(Thread t : threads1){
            try{
                t.join();
            }
            catch (InterruptedException e){
                System.out.println("ERROR");
            }
        }

        for(Thread t : threads2){
            try{
                t.join();
            }
            catch (InterruptedException e){
                System.out.println("ERROR");
            }
        }
        System.out.println(man);

        // 方式三：在方法前加上修饰符synchronized
        // 为方式二的简化写法，不再赘述

        // 线程安全的类：类中所以方法都是被synchronized修饰的
        // 非线程安全的类：由于不需要同步，速度更快
        // 常见非线程安全类:
        // List: ArrayList , LinkedList , Stack
        // Map: HashMap , TreeMap
        // Set: HashSet , TreeSet
        // StringBuffer

        // 常见对比
        // HashMap 和 Hashtable
        // HashMap: 可以存放null，非线程安全
        // Hashtable: 不可以存放null，线程安全

        // StringBuffer 和 StringBuilder
        // StringBuffer：线程安全
        // StringBuilder：非线程安全

        // ArrayList 和 Vector
        // ArrayList: 非线程安全
        // Vector: 线程安全

        // 将非线程安全的集合转换为线程安全：工具类Collections
        // List：synchronizedList
        List list = new ArrayList();
        List synchronizedList = Collections.synchronizedList(list);

        // Map: synchronizedMap
        Map map = new HashMap();
        Map synchronizedMap = Collections.synchronizedMap(map);

        // Set: synchronizedSet
        Set set = new HashSet();
        Set synchronizedSet = Collections.synchronizedSet(set);

    }
}
