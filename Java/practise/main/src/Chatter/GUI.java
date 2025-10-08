package Chatter;

import javax.swing.*;
import java.awt.*;

public class GUI extends JFrame {
    private JTextArea ta = new JTextArea();
    public GUI(){
        setSize(400 , 300);
        setLocation(400 , 300);
        setLayout(null);

        JLayeredPane layeredPane = new JLayeredPane();
        setContentPane(layeredPane);

        JMenuBar mb = new JMenuBar();

        JMenu m1 = new JMenu("文件");
        JMenu m2 = new JMenu("编辑");
        JMenu m3 = new JMenu("查看");

        m1.add(new JMenuItem("新建标签页"));
        m1.add(new JMenuItem("新建窗口"));
        m1.add(new JMenuItem("打开"));
        m1.add(new JMenu("最近使用").add(new JMenuItem("没有最近使用的文件")));
        m1.add(new JMenuItem("保存"));
        m1.add(new JMenuItem("另存为"));
        m1.add(new JMenuItem("全部保存"));
        m1.addSeparator();
        m1.add(new JMenuItem("页面设置"));
        m1.add(new JMenuItem("打印"));
        m1.addSeparator();;
        m1.add(new JMenuItem("关闭选项卡"));
        m1.add(new JMenuItem("关闭窗口"));
        m1.add(new JMenuItem("退出"));

        m2.add(new JMenuItem("撤销"));
        m2.addSeparator();
        m2.add(new JMenuItem("剪切"));
        m2.add(new JMenuItem("复杂"));
        m2.add(new JMenuItem("粘贴"));
        m2.add(new JMenuItem("删除"));
        m2.addSeparator();
        m2.add(new JMenuItem("查找"));
        m2.add(new JMenuItem("查找下一个"));
        m2.add(new JMenuItem("查找上一个"));
        m2.add(new JMenuItem("替换"));
        m2.add(new JMenuItem("转到"));
        m2.addSeparator();
        m2.add(new JMenuItem("全选"));

        JMenu m4 = new JMenu("缩放");
        m4.add(new JMenuItem("放大"));
        m4.add(new JMenuItem("缩小"));
        m4.add(new JMenuItem("还原"));
        m3.add(m4);
        m3.add(new JMenuItem("状态栏"));
        m3.add(new JMenuItem("自动换行"));
        m3.addSeparator();
        m3.add(new JMenuItem("Markdown"));

        mb.add(m1);
        mb.add(m2);
        mb.add(m3);

        setJMenuBar(mb);

        ta.setLineWrap(true);
        ta.setBounds(0 , 0 , 800 , 600);
        add(ta);

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        setVisible(true);
    }

    public JTextArea getTa(){
        return ta;
    }
}
