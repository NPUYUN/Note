package GUI;

import com.eltima.components.ui.DatePicker;
import org.jdesktop.swingx.JXDatePicker;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Date;
import java.util.Locale;

public class DataControl {
    public static void main(String[] args) {
        // swing 没有自带的日期控件，需要第三方类
        // DataPicker：不能设置时间，只能在创建控件时传入指定日期
        JFrame f = new JFrame();
        f.setSize(400 , 300);
        f.setLocation(200 , 200);
        f.setLayout(null);

        // 格式
        String DefaultFormat = "yyyy-MM-dd HH:mm:ss";
        // 当前时间
        Date date = new Date();
        // 字体
        Font font = new Font("Times New Roman" , Font.BOLD , 14);
        // 大小
        Dimension dimension = new Dimension(177 , 24);

        final DatePicker datePicker = new DatePicker(date , DefaultFormat,font,dimension);
        datePicker.setLocation(137, 83);
        datePicker.setBounds(137 , 83 , 177 , 24);

        int[] hilightDays = {1 , 3 , 5 , 7};
        int[] disabledDays = {4 , 6 , 5 , 9};

        // 设置一个月份中需要高亮显示的日子，须手动设置颜色
        datePicker.setHightlightdays(hilightDays , Color.RED);
        // 设置一个月份中不需要的日子，呈灰色
        datePicker.setDisableddays(disabledDays);

        // 设置国家
        datePicker.setLocale(Locale.CHINA);
        //设置时钟面板可见
        datePicker.setTimePanleVisible(true);

        f.add(datePicker);

        JButton b = new JButton("获取时间");
        b.setBounds(137 , 183 , 100 , 30);
        f.add(b);

        b.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JOptionPane.showMessageDialog(f , "获取控件里的日期: " + datePicker.getValue());
                System.out.println(datePicker.getValue());
            }
        });
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);


        // JXDatePicker：界面简介，可以设置日期
        JFrame f2 = new JFrame();
        f2.setSize(400, 300);
        f2.setLocation(200 , 200);
        f2.setLayout(null);

        final JXDatePicker jxDatePicker = new JXDatePicker();

        // 设置date日期
        jxDatePicker.setDate(date);

        jxDatePicker.setBounds(137 , 83 , 177 , 24);

        f2.add(jxDatePicker);

        f2.setVisible(true);
    }
}
