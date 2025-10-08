package GUI;

import javax.swing.*;
import javax.swing.table.AbstractTableModel;
import java.awt.*;
import java.util.Objects;

class JTableModel extends AbstractTableModel{ // 继承AbstractTableModel，进而实现接口TableModel
    // 表格上的标题：一维数组
    String[] column = new String[]{"name" , "sex" , "age"};
    // 表格中的内容：二维数组
    String[][] items = new String[][]{{"Ycc" , "boy" , "18"} , {"ycc" , "boy" , "0"}};

    public int getRowCount(){
        return items.length;
    }

    public int getColumnCount(){
        return column.length;
    }

    public String getColumnName(int columnIndex){
        return column[columnIndex];
    }

    public boolean isCellEditable(int rowIndex , int columnIndex){
        return false;
    }

    public Object getValueAt(int rowIndex , int columnIndex){
        return items[rowIndex][columnIndex];
    }
}

public class Table {
    public static void main(String[] args) {
        // 基本表格：JTable
        // 显示一个表格需要两组数据：一维数组（表示表格的标题）、二维数组（表格中的内容）
        // 默认情况下，表格标题不会显示出来，除非使用了JScrollPane
        JFrame f = new JFrame();
        f.setSize(400 , 300);
        f.setLocation(200 , 200);
        f.setLayout(new BorderLayout());

        // 表格上的标题：一维数组
        String[] column = new String[]{"name" , "sex" , "age"};
        // 表格中的内容：二维数组
        String[][] items = new String[][]{{"Ycc" , "boy" , "18"} , {"ycc" , "boy" , "0"}};

        JTable t = new JTable(items , column); // 先传入内容，后传入标题
        t.getColumnModel().getColumn(0).setPreferredWidth(10); // 设置列宽，参数分别为列数和预设宽度

        f.add(t , BorderLayout.CENTER); // 放在中间

        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);


        // JScrollPane实现带滚动条且可以看到标题的表格
        JFrame f2 = new JFrame();
        f2.setSize(800 , 400);
        f2.setLocation(200 , 200);
        f2.setLayout(new BorderLayout());
        JTable t2 = new JTable(items , column);
        JScrollPane sp = new JScrollPane(t2); // 采用根据表格的方式创建JScrollPane（或者可以通过setViewportView）
        t2.getColumnModel().getColumn(0).setPreferredWidth(10); // 设置列宽，参数分别为列数和预设宽度

        f2.add(sp , BorderLayout.CENTER); // 将JScrollPane而非JTable加入JFrame

        f2.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f2.setVisible(true);

        // TableModel接口：TableModel存储JTable的数据部分，定义了对数据部分的获取与操作
        // 需要显示的信息有（方法重写）：
        // getRowCount 返回一共有多少行
        // getColumnCount 返回一共有多少列
        // getColumnName 每一列的名字
        // isCellEditable 单元格是否可以修改
        // getValueAt 每一个单元格里的值
        // 在创建JTable时，底层代码实际上去创建了一个TableModel对象
        JTableModel tm = new JTableModel();
        JTable t3 = new JTable(tm); // 根据TableModel来创建Table


        // 下面内容在学完JDBC后再进行
        // TableModel与DAO结合
        // TableSelectionModel
        // 更新Table
        // 输入项验证
        // 选中指定行


    }
}
