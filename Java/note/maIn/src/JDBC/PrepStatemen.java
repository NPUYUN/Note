package JDBC;

import java.sql.*;

public class PrepStatemen {
    public static void main(String[] args) {
        try{
            Class.forName("com.mysql.cj.jdbc.Driver");
        }
        catch (ClassNotFoundException e){
            System.out.println("Error");
        }

        String sql = "insert into human values(? , ?)"; // ?为占位符

        try(Connection c = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/text", "root", "@Ycc20060308");
            // 根据sql语句创建PreparedStatement
            PreparedStatement ps = c.prepareStatement(sql);
            )
        {
            // PreparedStatement与Statement的不同：
            // 前者需要sql语句
            // 前者可以设置参数，指定相应索引的值
            ps.setString(2 , "王五"); // 从1开始（唯二的从1开始）
            ps.setInt(1 , 3);

            ps.execute(); // 执行
        }
        catch (SQLException e){
            System.out.println("Error");
        }

        // PreparedStatement的优势
        // 参数设置，可读性强
        // 预编译机制，性能更快
        // 防止SQL注入式攻击
    }
}
