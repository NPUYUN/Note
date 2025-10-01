package Multithread;

class Student{
    String name;
    int age;

    public Student(String name , int age){
        this.name = name;
        this.age = age;
    }

    public boolean isOver(){
        if(this.age <= 19){
            this.age ++;
            return false;
        }
        return true;
    }

    public void isClass(Student stu){
        System.out.printf(this.name + "(%d) studies with " + stu.name + "(%d)\n" , this.age , stu.age);
    }
}

class DoStudent extends Thread implements Runnable{ // 继承Thread // 实现Runnable接口
    private Student s1;
    private Student s2;

    public DoStudent(Student s1 , Student s2){
        this.s1 = s1;
        this.s2 = s2;
    }

    public void run(){ // 复写run方法
        while(!s2.isOver()) s1.isClass(s2);
    }
}

public class Start{
    public static void main(String[] args) {
        Student s1 = new Student("YCC" , 17);
        Student s2 = new Student("ZXT" , 16);
        Student s3 = new Student("HAN" , 15);
        // 创建多线程
        // 方式一：继承线程类
        // 类继承Thread，重写run方法
        // 启动线程：实例化，并调用start方法，此时就会调用run里面的方法
        DoStudent ds1 = new DoStudent(s1 , s2);
        ds1.start();
        DoStudent ds2 = new DoStudent(s3 , s1);
        ds2.start();

        // 方式二：实现Runnable接口
        // 类实现Runnable接口（含有run方法）
        // 启动线程：创建Thread对象时将对象传进去，使用Thread的对象方法start启动线程
        Student s4 = new Student("YCC" , 17);
        Student s5 = new Student("ZXT" , 16);
        Student s6 = new Student("HAN" , 15);
        ds1 = new DoStudent(s4 , s5);
        new Thread(ds1).start();
        ds2 = new DoStudent(s6 , s4);
        new Thread(ds2).start();


        // 方式三：匿名类
        // 直接使用继承Thread的匿名类，重写run方法
        // 启动线程：调用匿名类对象的start方法
        Student s7 = new Student("YCC" , 17);
        Student s8 = new Student("ZXT" , 16);
        Student s9 = new Student("HAN" , 15);
        Thread t1 = new Thread(){
            public void run(){
                while(!s8.isOver()) s7.isClass(s8);
            }
        };
        t1.start();
        Thread t2 = new Thread(){
            public void run(){
                while(!s7.isOver()) s9.isClass(s7);
            }
        };
        t2.start();

        // 常见线程方法
        // 当前线程停止：sleep(time(ms)) 静态方法
        // 当前线程sleep时可能会被停止，会抛出InterruptedException
        // sleep期间会被其他线程乘虚而入
        Thread t3 = new Thread(){
            public void run(){
                int second = 0;
                while(true){
                    try{
                        Thread.sleep(100);
                    }
                    catch (InterruptedException e){
                        System.out.println(e);
                    }
                    System.out.println(second ++);
                    if(second > 10) break;
                }
            }
        };
        t3.start();

        // 加入当前线程：join()
        // 主线程：从main方法开始执行
        // 在主线程加入该线程时，会等待该线程结束完毕，再往下运行主线程
        // 加入的线程可能会被停止，会抛出InterruptedException
        Thread t4 = new Thread(){
            public void run(){
                int seconds = 0;
                while(true){
                    System.out.println(seconds ++);
                    if(seconds > 10) break;
                }
            }
        };
        t4.start();
        try{
            // t4线程加入到main中来，只有t4结束时才会继续往下走
            t4.join();
        }
        catch (InterruptedException e){
            System.out.println(e);
        }
        // t4运行完成后，再运行
        System.out.println("t4 over");

        // 线程优先级：setPriority()
        // 一般线程为竞争关系，优先级高的线程会有更大的几率获得CPU资源
        // Thread中有两个优先级常量：
        // MAX_PRIORITY：最高优先级
        // MIN_PRIORITY：最低优先级
        // 其他数字：越大优先级越高
        Thread t5 = new Thread(){
            public void run(){
                int seconds = 0;
                while(true){
                    System.out.println("MAX_Priority : " + seconds ++);
                    if(seconds > 10) break;
                }
            }
        };
        Thread t6 = new Thread(){
            public void run(){
                int seconds = 0;
                while(true){
                    System.out.println("MIN_Priority : " + seconds ++);
                    if(seconds > 10) break;
                }
            }
        };
        t5.setPriority(Thread.MAX_PRIORITY);
        t6.setPriority(Thread.MIN_PRIORITY);
        t5.start();
        t6.start();

        // 临时暂停：yield() 静态方法
        final int[] times = {0}; // 被内部类读取，变量须声明为final(如果为基本数据类型，需要修改为单元素final数组)
        Thread t7 = new Thread(){
            public void run(){
                while(true){
                    System.out.println("MAX : " + times[0] ++);
                    if(times[0] > 10) break;
                }
            }
        };
        Thread t8 = new Thread(){
            public void run(){
                int seconds = 0;
                while(true){
                    if(times[0] < 10) Thread.yield(); // 临时暂停，为t7腾出空间
                    System.out.println("MIN : " + seconds ++);
                    if(seconds > 10) break;
                }
            }
        };
        t7.setPriority(5);
        t8.setPriority(5);
        t7.start();
        t8.start();

        // 守护线程：setDaemon(Boolean)
        // 如果一个进程只剩下守护线程，那么这个进程就会自动结束
        Thread t9 = new Thread(){
            public void run(){
                int seconds = 0;
                while(true){
                    try{
                        Thread.sleep(400);
                    }
                    catch (InterruptedException e){
                        System.out.println(e);
                    }
                    System.out.println("守护 : " + seconds ++);
                    if(seconds > 10) break;
                }
            }
        };
        t9.setDaemon(true);
        t9.start();
    }
}
