package GUI;

import java.awt.*;
import java.awt.event.*;

import javax.swing.*;

public class Monitor {
    public static void main(String[] args) {
        // 按钮监听：ActionListener接口
        // 当按钮被点击时，调用actionPerformed，重写该方法以实现点击后的逻辑
        JFrame f = new JFrame("ycc");
        f.setSize(400 , 300);
        f.setLocation(580 , 200);
        f.setLayout(new FlowLayout());

        JButton b1 = new JButton("click me");
        JButton b2 = new JButton("OK");

        b1.addActionListener(new ActionListener() { // 为按钮添加监听
            @Override
            public void actionPerformed(ActionEvent e) {
                b2.setVisible(false);
            }
        });

        f.add(b1);
        f.add(b2);


        // 键盘监听：KeyListener接口
        // keyPressed：键被按下
        // keyReleased：键被弹起
        // keyTyped：一个按下弹起的组合动作
        // KeyEvent.getKeyCode()：获取当前按下了哪个键(ASCII)
        // 上（38） ， 下（40），左（37），右（39）
        final JLabel l = new JLabel(); // 显示文本、图标的组件
        ImageIcon i = new ImageIcon("C:\\Users\\26506\\OneDrive\\图片\\屏幕快照\\屏幕截图 2025-03-15 162604.png"); // 图片对象
        l.setIcon(i);


        f.addKeyListener(new KeyListener() {
            @Override
            public void keyTyped(KeyEvent e) {
            }

            @Override
            public void keyPressed(KeyEvent e) {
            }

            @Override
            public void keyReleased(KeyEvent e) {
                if(e.getKeyChar() == 'r'){
                    l.setLocation(l.getX() + 10 , l.getY()); // 按钮向右移
                }
                if(e.getKeyChar() == 'l'){
                    l.setLocation(l.getX() - 10 , l.getY()); // 按钮向左移
                }
            }
        });
        // 注意：触发的组件必须处于聚焦状态，详情见下文


        // 鼠标监听：MouseListener接口
        // 鼠标释放：mouseReleased
        // 鼠标按下：mousePressed
        // 鼠标退出：mouseExited
        // 鼠标进入：mouseEntered
        // 鼠标点击：mouseClicked
        l.addMouseListener(new MouseListener() {
            @Override
            public void mouseClicked(MouseEvent e) {

            }

            @Override
            public void mousePressed(MouseEvent e) {

            }

            @Override
            public void mouseReleased(MouseEvent e) {

            }

            @Override
            public void mouseEntered(MouseEvent e) {
                l.setLocation(l.getX() + 10 , l.getY() + 10);
            }

            @Override
            public void mouseExited(MouseEvent e) {

            }
        });


        // 适配器：Adapter接口
        // 每种监听器(除了按钮监听)都有Adapter接口，表示只需要重写要用的方法即可
        // 以MouseAdapter为例，其他的与之类似
        l.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseEntered(MouseEvent e) {
                System.out.println("in");
            }
        });
        f.add(l);


        // 组件监听器：ItemListener
        // 适用于支持项状态变化的组件，包括：JCheckBox(复选框)、JRadioButton(单选按钮)、JComboBox(下拉列表)、JList(列表框)
        JCheckBox cb = new JCheckBox("B1");
        cb.addItemListener(new ItemListener() {
            @Override
            public void itemStateChanged(ItemEvent e) {
                System.out.println("OK");
            }
        });
        f.add(cb);

        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);
    }
}
