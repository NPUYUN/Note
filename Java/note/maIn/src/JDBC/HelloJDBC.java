package JDBC;

import javax.swing.plaf.nimbus.State;
import java.sql.Connection; // 导入外部库
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class HelloJDBC {
    public static void main(String[] args) {
        // Java自身没有实现JDBC的库，需要导入外部库

        try {
            // 初始化驱动：初始化驱动类com.mysql.jdbc.Driver
            Class.forName("com.mysql.cj.jdbc.Driver");
            System.out.println("数据库驱动加载中");
        }
        catch(ClassNotFoundException e){ // 可能会出现找不到库的情况
            System.out.println("Error");
            e.printStackTrace();
        }

        try(// 建立与数据库之间的连接
            // 需要提供：数据库的ip、端口号、名称、编码方式(一般为UTF-8)、账号(一般为root)、密码
            Connection c = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/text", "root", "@Ycc20060308");

            // 创建Statement
            // Statement是用来执行SQL语句的
            Statement s = c.createStatement();) {

            System.out.println("数据库连接成功");

            // 执行SQL语句：execute
            String sql = "insert into human values(2 ," + "'李四'" + ")"; // 注意字符串要加上单引号
            s.execute(sql);
        }
        catch (SQLException e){
            System.out.println("Error");
        }

    }
}
