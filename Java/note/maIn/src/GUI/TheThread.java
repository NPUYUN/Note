package GUI;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class TheThread {

    public static void main(String[] args) {
        // swing 编程开发时有三种线程
        // 初始化线程：创建各种容器并显示他们
        // 事件调度线程：所有事件相关操作，为单线程（Swing里的各种组件都不是线程安全的）
        // 长耗时任务线程：所有需要长时间操作的事件

        // 初始化线程
        // 初始化一个图形界面时，都会在主线程里调用如下代码
        // new TestFrame().setVisible(true);
        // 但由于主线程和事件调度线程同时访问组件，在复杂的程序里可能出现问题
        // 为了规避问题，可以将创建和显示界面的工作交给事件调度线程
        SwingUtilities.invokeLater(new Runnable() { // 交给事件调度线程
            @Override
            public void run() {
                new TestFrame().setVisible(true);
            }
        });
        // 还可以用SwingUtilities.isEventDispatchThread()来判断当前线程是否为事件调度线程


        // 事件调度线程：所有事件监听都为事件调度线程
        JFrame f = new JFrame();
        f.setSize(800 , 600);
        f.setLocation(200 , 200);
        f.setLayout(new FlowLayout());

        JButton b = new JButton("B1");
        b.addActionListener(new ActionListener() { // 事件调度线程
            @Override
            public void actionPerformed(ActionEvent e) {
                b.setVisible(false);
                System.out.println(SwingUtilities.isEventDispatchThread()); // 用SwingUtilities.isEventDispatchThread()来判断当前线程是否为事件调度线程
            }
        });
        f.add(b);
        f.setVisible(true);


        // 长耗时任务线程
        // 长耗时任务（数据库查询、文件复制、访问网络等）会进入事件调度线程
        // 为了将其独立成长耗时任务线程，可以通过抽象类SwingWorker来实现
        // 为了使用SwingWorker类，必须实现方法doInBackground，在该方法内可以编写长耗时任务，然后通过SwingWorker的execute方法，放在专门的工作线程中运行
        // SwingWorker工作原理：执行execute时，调用默认的10根线程的线程池，执行doInBackground中的代码
        // 通过Thread.currentThread().getName()可以获取执行当前SwingWorker的线程名称
        JFrame f2 = new JFrame();
        f2.setSize(300 , 300);
        f2.setLocation(200 , 200);
        f2.setLayout(new FlowLayout());

        JButton b1 = new JButton("在事件调度线程中执行长时任务");
        JButton b2 = new JButton("在SwingWorker中执行长时任务");
        JLabel l = new JLabel();

        b1.addActionListener(new ActionListener() { // 事件调度线程
            @Override
            public void actionPerformed(ActionEvent e) {
                l.setText("开始执行完毕");
                try{
                    Thread.sleep(5000);
                }
                catch (InterruptedException i){
                    System.out.println("Error");
                }
                l.setText("任务执行完毕");
            }
        });

        b2.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) { // 长耗时线程
                SwingWorker<Void , Void> worker = new SwingWorker<Void, Void>() { // 泛型为键值对<T , V>，T为doInBackground的返回类型，V表示后台任务执行过程中可能逐步返回的中间结果类型
                    @Override
                    protected Void doInBackground() throws Exception {
                        System.out.println(Thread.currentThread().getName());
                        l.setText("开始执行完毕");
                        try{
                            Thread.sleep(5000);
                        }
                        catch (InterruptedException i){
                            System.out.println("Error");
                        }
                        l.setText("任务执行完毕");
                        return null;
                    }
                };
                worker.execute();
            }
        });

        f2.add(b1);
        f2.add(b2);
        f2.add(l);

        f2.setVisible(true);
    }

    static class TestFrame extends JFrame{
        public TestFrame(){
            setSize(400 , 300);
            setLocation(200 , 200);
            setLayout(null);

            JButton b = new JButton("B");
            b.setBounds(50 , 50 , 280 , 30);
            add(b);

            setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            setVisible(true);

            // 用SwingUtilities.isEventDispatchThread()来判断当前线程是否为事件调度线程
            System.out.println(SwingUtilities.isEventDispatchThread());
        }
    }
}
