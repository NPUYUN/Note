package GUI;

import javax.swing.*;
import java.awt.*;

public class MenuAndToolbar {
    public static void main(String[] args) {
        // 菜单
        // 菜单栏：JMenuBar
        // 菜单：JMenu
        // 菜单项：JMenuItem
        // 加入菜单：setJMenuBar(JMenuBar)
        JFrame f = new JFrame();
        f.setSize(400 , 300);
        f.setLocation(200 , 200);

        // 菜单栏
        JMenuBar mb = new JMenuBar();

        // 菜单
        JMenu m1 = new JMenu("001");
        JMenu m2 = new JMenu("002");

        //菜单项
        m1.add(new JMenuItem("File -CTRL + R"));
        m1.add(new JMenuItem("Save -CTRL + S"));
        m1.addSeparator(); // 加入分隔符
        m1.add(new JMenuItem("ALL"));

        mb.add(m1); // 将菜单加入菜单栏
        mb.add(m2);

        f.setJMenuBar(mb); // 把菜单栏加入到frame

        // 工具栏：JToolBar
        JToolBar tb = new JToolBar();
        JButton b1 = new JButton("1");
        tb.add(b1); // 为工具栏添加按钮

        // 给按钮设置提示信息(鼠标放上时显示): setToolTipText
        b1.setToolTipText("Sure");

        // 一般来说，工具栏是可以拖动的，通过设置setFloatable为false来实现禁止拖动
        tb.setFloatable(false);

        f.setLayout(new BorderLayout());
        f.add(tb , BorderLayout.NORTH); // 将工具栏放在上方


        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);
    }
}
