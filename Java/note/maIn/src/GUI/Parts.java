package GUI;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.util.Objects;
import javax.swing.*;
import javax.swing.filechooser.FileFilter;

public class Parts {
    public static void main(String[] args) {
        JFrame f = new JFrame("Title");
        f.setSize(800 , 600);
        f.setLocation(200 , 200);
        f.setLayout(new FlowLayout());

        // Java有两组组件，一个为awt，一个为swing，一般为swing
        // 标签：JLabel
        // 标签用于显示文字
        JLabel l = new JLabel("文字");
        l.setForeground(Color.red); // 设置颜色
        f.add(l);


        // 使用JLabel显示图片：setIcon
        // java通过ImageIcon创建图片对象，然后通过Label显示
        JLabel li = new JLabel("图片");
        ImageIcon i = new ImageIcon("C:\\Users\\26506\\OneDrive\\图片\\屏幕快照\\屏幕截图 2025-03-15 162604");
        li.setIcon(i);
        li.setBounds(50 , 50 , i.getIconWidth() , i.getIconHeight()); // label大小设置为ImageIcon否则显示不完整
        f.add(li);


        // 按钮：JButton
        JButton b = new JButton("B");
        f.add(b);


        // 复选框：JCheckBox
        // 使用isSelected来获取是否选中，使用setSelected设置选中状态
        JCheckBox bCheckBox1 = new JCheckBox("B1");
        bCheckBox1.setSelected(true); // 设置为默认已选中
        JCheckBox bCheckBox2 = new JCheckBox("B2");
        System.out.println(bCheckBox2.isSelected());
        f.add(bCheckBox1);
        f.add(bCheckBox2);


        // 单选框：JRadioButton
        // 使用isSelected来获取是否选中，使用setSelected设置选中状态
        JRadioButton b1 = new JRadioButton("b1");
        b1.setSelected(true);
        JRadioButton b2 = new JRadioButton("b2");
        System.out.println(b2.isSelected());


        // 按钮组：ButtonGroup
        // ButtonGroup可以将按钮分组，同一分组同一时间只能选中一个按钮
        ButtonGroup bg = new ButtonGroup();
        // 把b1，b2放在 同一个 按钮分组对象里 ，这样同一时间，只有一个 按钮 会被选中
        bg.add(b1);
        bg.add(b2);
        f.add(b1);
        f.add(b2);


        // 下拉框：JComboBox
        // 使用getSelectedItem来获取被选中项
        // 使用setSelectedItem来指定要选中项
        String[] choice = new String[]{"1" , "2"};
        JComboBox<String> cb  = new JComboBox<>(choice); // 传入选项
        System.out.println(cb.getSelectedItem());
        f.add(cb);


        // 对话框：JOptionPane（以下均为静态方法）
        // showConfirmDialog(组件/窗体，内容) 询问（含确定按钮）
        // showInputDialog(组件/窗体，内容) 接收用户输入
        // showMessageDialog(组件/窗体，内容） 显示消息
        // 其中组件参数表示与哪个组件对齐
        int option = JOptionPane.showConfirmDialog(f,"Click"); // 返回操作，为整数
        if (option == JOptionPane.OK_OPTION){ // 当返回的数与确定键常量一致时
            String answer = JOptionPane.showInputDialog(f , "请输入yes"); // 接收用户输入，返回字符串
            if(Objects.equals("yes", answer )){
                JOptionPane.showMessageDialog(f, "OK");
            }
        }


        // 文本框：JTextField（单行文本）
        // setText：设置文本
        // getText：获取文本
        // 组件.grabFocus()：让组件获取焦点
        JTextField tf = new JTextField("input"); // 构造函数含设置文本
        System.out.println(tf.getText());
        f.add(tf);


        // 密码框：JPasswordField
        // getPassword：获取密码，返回字符数组。其他方式为字符串
        JPasswordField pf = new JPasswordField("&48kdh4@#");
        char[] password = pf.getPassword();
        System.out.println(password);
        f.add(pf);


        // 文本域：JTextArea（多行文本）
        // JTextArea通常会用到append来进行文本追加，\n表示换行
        // 为了防止文本过长，可以通过setLineWrap(true)来设置自动换行
        JTextArea ta = new JTextArea("FUCK\nYOU");
        ta.append(".");
        ta.setLineWrap(true); // 设置自动换行
        f.add(ta);


        // 进度条：JProgressBar
        // setMaximum：设置进度条最大值
        // setValue：设置当前进度
        // setStringPainted(true)：显示当前进度
        JProgressBar pb = new JProgressBar();
        pb.setMaximum(100);
        pb.setValue(50);
        pb.setStringPainted(true);
        f.add(pb);


        // 文本选择器：JFileChooser
        // setFileFilter(FileFilter)：设置文件筛选
        // showOpenDialog(组件/窗体)：打开文件
        // showSaveDialog(组件/窗体)：保存文件
        JFileChooser fc = new JFileChooser();
        fc.setFileFilter(new FileFilter() {
            @Override
            public boolean accept(File f) {
                return f.getName().toLowerCase().endsWith(".txt"); // 转换为全小写并在结尾加上.txt
            }

            @Override
            public String getDescription() {
                return ".txt";
            }
        });
        JButton bOpen = new JButton("打开文件");
        JButton bSave = new JButton("保存文件");

        bOpen.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int returnVal = fc.showOpenDialog(f); // 打开文件时返回整数
                File file = fc.getSelectedFile(); // 获取选择的文件
                if(returnVal == JFileChooser.APPROVE_OPTION){ // 若返回的是打开成功时的整数
                    JOptionPane.showMessageDialog(f , "打开文件 : " + file.getAbsolutePath());
                }
            }
        });

        bSave.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int returnVal = fc.showSaveDialog(f);
                File file = fc.getSelectedFile();
                if(returnVal == JFileChooser.APPROVE_OPTION){
                    JOptionPane.showMessageDialog(f , "保存文件" + file.getAbsolutePath());
                }
            }
        });

        f.add(bOpen);
        f.add(bSave);


        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);
        tf.grabFocus();
    }
}
