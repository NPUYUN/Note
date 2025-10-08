package GUI;

import java.awt.*;
import javax.swing.JFrame;
import javax.swing.JButton;
import java.util.List;
import java.util.ArrayList;

public class LayoutManager {
    public static void addButton(JFrame f , JButton ... buttons){
        for(JButton b : buttons){
            f.add(b);
        }
    }

    public static void main(String[] args) {
        List<JButton> buttons = new ArrayList<>();
        for(int i = 1 ; i <= 15 ; i ++){
            buttons.add(new JButton("B" + i));
        }

        // 绝对定位：setLayout(null)
        // 组件的位置和大小需要单独指定
        JFrame f = new JFrame();
        f.setLayout(null);

        // 顺序布局器：FlowLayout类
        // 容器组件水平摆放，无需指定大小和位置
        JFrame f1 = new JFrame("FlowLayout");
        f1.setSize(800 , 600);
        f1.setLocation(200 , 200);
        f1.setLayout(new FlowLayout());
        LayoutManager.addButton(f1 , buttons.get(0) , buttons.get(1) , buttons.get(2));
        f1.setVisible(true);

        // 设置布局器：BorderLayout类
        // 组件按照上北下南 左西右东 中 的顺序摆放
        JFrame f2 = new JFrame("BorderLayout");
        f2.setSize(800 , 600);
        f2.setLocation(200 , 200);
        f2.setLayout(new BorderLayout());
        LayoutManager.addButton(f2 , buttons.get(3) , buttons.get(4) , buttons.get(5) , buttons.get(6) , buttons.get(7));
        f2.setVisible(true);

        // 网格布局器：GridLayout类
        JFrame f3 = new JFrame("GridLayout");
        f3.setSize(800 , 600);
        f3.setLocation(200 , 200);
        f3.setLayout(new GridLayout());
        LayoutManager.addButton(f3 , buttons.get(8) , buttons.get(9) , buttons.get(10) , buttons.get(11));
        f3.setVisible(true);

        // 在布局器中设置组件大小：setPreferredSize，Dimension类
        // 由于很多布局器有格式要求，故仅对部分布局器有效，如FlowLayout
        JFrame f4 = new JFrame("set");
        f4.setSize(800 , 600);
        f4.setLocation(200 , 200);
        f4.setLayout(new FlowLayout());

        JButton b1 = new JButton("B1");
        JButton b2 = new JButton("B2");
        JButton b3 = new JButton("B3");

        b3.setPreferredSize(new Dimension(180 , 40));

        LayoutManager.addButton(f4 , b1 , b2 , b3);

        f4.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f4.setVisible(true);
    }
}
