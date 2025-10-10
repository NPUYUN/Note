package JDBC;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class Affair {
    public static void main(String[] args) {
        // 在事务中的多个操作，要么都成功，要么都失败
        // 前提：表为InnoDB的（默认为InnoDB）
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
        }
        catch(ClassNotFoundException e){
            System.out.println("Error");
        }

        try(Connection c = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/text", "root", "@Ycc20060308");
            Statement s = c.createStatement();) {

            // 关闭自动提交，代表开始事务
            c.setAutoCommit(false);

            String sql1 = "update human set name = name + '!' where id = 1";
            s.execute(sql1);

            String sql2 = "updated human set name = name + '!' where id = 100"; // 操作不正确，整个事务不会进行
            s.execute(sql2);
            // 手动提交，代表事务结束
            c.commit();
        }
        catch (SQLException e){
            System.out.println("Error");
        }
    }
}
