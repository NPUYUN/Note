package Multithread;

class Role{
    int hp;
    int attack;
    String name;

    public synchronized void recover(){
        hp ++;
        System.out.println(name + ' ' + hp);
        this.notify(); // 通知等待在this兑现上的线程苏醒
    }

    public synchronized void hurt(){
        if(hp == 1){
            try{
                this.wait(); // 让占有this的线程暂时释放对this的占用，并等待
            }
            catch (InterruptedException e){
                System.out.println("ERROR");
            }
        }

        hp --;
        System.out.println(name + ' ' + hp);
    }
}

public class Interactions {
    public static void main(String[] args) {
        // Object中有三种方法可以控制线程的交互
        // wait()方法：临时释放当前占用，必须在synchronized块里调用，可能会出现InterruptedException异常
        // notify()方法：通知一个等待在该同步对象上的线程可以苏醒并重新占用当前对象
        // notifyAll()方法：通知所有等待在该同步对象上的线程可以苏醒并重新占用当前对象
        Role role = new Role();
        role.hp = 10;
        role.name = "YCC";

        Thread t1 = new Thread(){
            public void run(){
                while(true){
                    role.hurt();

                    try{
                        Thread.sleep(10);
                    }
                    catch (InterruptedException e){
                        System.out.println("ERROR");
                    }
                }
            }
        };
        t1.start();
        Thread t2 = new Thread(){
            public void run(){
                while(true){
                    role.recover();

                    try{
                        Thread.sleep(100);
                    }
                    catch (InterruptedException e){
                        System.out.println("ERROR");
                    }
                }
            }
        };
        t2.start();
    }
}
