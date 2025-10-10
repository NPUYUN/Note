package JDBC;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class ExeUpdate {
    public static void main(String[] args) {
        // 相同点：都可以执行增加，删除，修改
        // 不同点：
        // executeUpdate不能执行查询语句，返回的是int，表示有多少条数据受影响
        // execute可以执行查询语句，返回的是boolean，true表示执行的是查询，false表示执行的是增删改
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
        }
        catch(ClassNotFoundException e){
            System.out.println("Error");
        }

        try(Connection c = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/text", "root", "@Ycc20060308");
            Statement s = c.createStatement();) {

            // 执行SQL语句：executeUpdate
            String sql = "delete from human where name = '李四'";
            System.out.println(s.executeUpdate(sql));
            System.out.println(s.execute(sql));
        }
        catch (SQLException e){
            System.out.println("Error");
        }
    }
}
