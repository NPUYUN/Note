package GUI;

import javax.swing.JButton; // 按钮组件
import javax.swing.JFrame; // GUI中的容器

public class HelloSwing {
    public static void main(String[] args) {
        JFrame f = new JFrame("ycc"); // 主窗体

        f.setSize(400 , 300); // 设置主窗体大小
        f.setLocation(200 , 200); // 设置主窗口位置
        f.setLayout(null); // 主窗体组件设置为绝对定位

        JButton b = new JButton("OK"); // 按钮组件

        b.setBounds(50 , 50 , 280 , 30); // 设置组件大小和位置

        f.add(b); // 将组件加入主窗体

        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // 关闭窗体的时候退出程序
        f.setVisible(true); // 设置窗体可见
    }
}
