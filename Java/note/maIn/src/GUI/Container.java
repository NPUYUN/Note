package GUI;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Objects;

public class Container {
    public static void main(String[] args) {
        // Java右两种容器：JFrame , JDialog
        // JFrame：最常用的窗体型容器，右上角有最大化最小化按钮，有标题的构造函数
        JFrame f = new JFrame("JFrame");
        f.setSize(400 , 300);
        f.setLocation(200 , 200);
        f.setLayout(null);
        f.setVisible(true);

        // JDialog：普通的窗体，右上角无最大化最小化按钮，无标题的构造函数
        JDialog d = new JDialog();
        d.setTitle("JDialog");
        d.setSize(400 , 300);
        d.setLocation(200 , 200);
        d.setLayout(null);
        d.setVisible(true);

        // 模态JDialog
        // 当一个对话框被设置为模态时，其背后的父窗体不被激活(无法选中)，除非该对话框被关闭
        JFrame f2 = new JFrame("父窗体");
        f2.setSize(800 , 600);
        f2.setLocation(100 , 100);

        JDialog d2 = new JDialog(f2); // 根据JFrame窗体实例化JDialog
        d2.setModal(true); // 设为模态
        d2.setTitle("模态");
        d2.setSize(400 , 300);
        d2.setLocation(200 , 200);
        d2.setLayout(null);

        f2.setVisible(true);
        d2.setVisible(true);

        // JFrame可以通过setResizeable设置窗体大小是否可变
        JFrame f3 = new JFrame("NO");
        f3.setSize(600 , 400);
        f3.setLocation(100 , 100);
        f3.setLayout(null);
        f3.setResizable(false); // 设置窗体大小不变
        f3.setVisible(true);


        // 组合小练习
        JFrame jf = new JFrame("Father");
        jf.setSize(800 , 600);
        jf.setLocation(100 , 100);
        jf.setLayout(null);

        JButton b = new JButton("打开一个模态窗口");
        b.setBounds(150 , 150 , 600 , 100);
        b.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JDialog jd = new JDialog(jf);
                jd.setModal(true);
                jd.setTitle("模态窗口");
                jd.setSize(400 , 300);
                jd.setLocation(200 , 200);
                jd.setLayout(null);

                JButton b2 = new JButton("锁定大小");
                b2.setBounds(0 , 0 , 400 , 300);
                b2.addActionListener(new ActionListener() {
                    @Override
                    public void actionPerformed(ActionEvent e) {
                        if(Objects.equals(b2.getText() , "锁定大小")){
                            jd.setResizable(false);
                            b2.setText("解锁大小");
                        }
                        else{
                            jd.setResizable(true);
                            b2.setText("锁定大小");
                        }
                    }
                });

                jd.add(b2);

                jd.setVisible(true);
            }
        });

        jf.add(b);
        jf.setVisible(true);

    }
}
