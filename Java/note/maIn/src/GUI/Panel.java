package GUI;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;

public class Panel {
    public static void main(String[] args) {
        JFrame f = new JFrame();
        f.setSize(800 , 600);
        f.setLocation(200 , 200);
        f.setLayout(new FlowLayout());

        // 面板和JFrame一样都是容器，但是一般面板充当中间容器，将组件放在面板上，然后把面板放在窗体上
        // 移动面板时，上面的组件也会跟着移动。
        // 基本面板：JPanel
        JPanel p = new JPanel();
        p.setBounds(50 , 50 , 300 , 60);
        p.setBackground(Color.RED); // 设置面板背景颜色
        p.setLayout(new FlowLayout()); // 这句可以没有，因为JPanel默认使用FlowLayout布局

        JButton b1 = new JButton("b1");
        JButton b2 = new JButton("b2");
        p.add(b1);
        p.add(b2);

        f.add(p); // 将面板加入窗体


        // ContentPane
        // 往JFrame上加组件，实际上就是往JFrame上的ContentPane加组件
        // 即f.add() == f.getContentPane().add()
        // getParent()：获取组件在哪个容器中
        JButton b3 = new JButton("b3");
        b3.setBounds(100 , 100 , 280 ,30);
        f.add(b3);
        System.out.println(b3.getParent());


        // JSplitPane：分割面板
        // 参数：(分割类型(某常量)，左/上面板，右/下面板)
        JPanel pl = new JPanel();
        pl.setBounds(50 , 50 , 300 , 60);
        pl.setBackground(Color.RED);
        JPanel pr = new JPanel();
        pr.setBounds(10 , 150 , 300 , 60);
        pr.setBackground(Color.BLUE);

        JSplitPane sp = new JSplitPane(JSplitPane.HORIZONTAL_SPLIT , pl , pr); // 创建水平分割面板
        sp.setDividerLocation(80); // 设置分割条位置
        f.setContentPane(sp); // 将JSplitPane设置为ContentPane


        // JScrollPane：滚动面板
        // 使用带滚动条的面板有两种方式：
        // 方式一：创建JScrollPane时将组件作为参数传入
        // 方式二：希望带滚动条的面板显示其他组件时，调用setViewportView(组件)
        JTextArea ta = new JTextArea();
        for(int i = 0 ; i < 1000 ; i ++){
            ta.append(String.valueOf(i));
        }
//        ta.setLineWrap(true);
//        JScrollPane jsp = new JScrollPane(ta); // 选择方式一使用带滚动的面板
//        f.add(jsp);
//        f.setContentPane(jsp); // 将JScrollPane设置为ContentPane


        // JTabbedPane: 选项卡面板
        JTabbedPane tp = new JTabbedPane();
        tp.addTab("l" , pl);
        tp.addTab("r",pr);
        f.add(tp);

        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);

        // CardLayerout 布局器(类似于JTabbedPane)
        JFrame f2 = new JFrame();
        JPanel comboBoxPane = new JPanel();
        String buttonPanel = "控制面板";
        String inputPanel = "输入框面板";
        String[] comboBoxItems = {buttonPanel , inputPanel};
        JComboBox<String> cb = new JComboBox<>(comboBoxItems);
        comboBoxPane.add(cb);

        // 两个Panel充当卡片
        JPanel card1 = new JPanel();
        card1.add(new JButton("(1)"));
        card1.add(new JButton("(2)"));
        card1.add(new JButton("(3)"));
        JPanel card2 = new JPanel();
        card2.add(new JTextField("input" , 20));

        // 创建Panel使用CardLayout
        JPanel cards = new JPanel(new CardLayout());
        cards.add(card1 , buttonPanel);
        cards.add(card2 , inputPanel);

        f2.add(comboBoxPane , BorderLayout.NORTH); // 添加到BorderLayout中的北方
        f2.add(cards , BorderLayout.CENTER); // 添加到BorderLayout中的中间

        f2.setSize(250 , 150);
        f2.setLocationRelativeTo(null); // 设置为屏幕中央
        f2.setVisible(true);

        cb.addItemListener(new ItemListener() {
            @Override
            public void itemStateChanged(ItemEvent e) {
                CardLayout cl = (CardLayout) (cards.getLayout());
                cl.show(cards , (String)e.getItem());
            }
        });
    }
}
