package JDBC;

import java.sql.*;

public class Search {
    public static void main(String[] args) {
        try{
            Class.forName("com.mysql.cj.jdbc.Driver");
        }
        catch (ClassNotFoundException e){
            System.out.println("Error");
        }

        try(Connection c = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/text","root","@Ycc20060308");
            Statement s = c.createStatement();){

            String sql = "select * from human";

            // 执行查询语句，结果集返回给ResultSet
            ResultSet rs = s.executeQuery(sql); // executeQuery 执行查询语句
            while(rs.next()){ // 判断是否有下一个。类似迭代器的hasNext
                int id = rs.getInt("id"); // 可以依据字段的名字查询
                String name = rs.getString(2); // 也可以依据字段的顺序查询，注意：从1开始（唯二从1开始的地方）
                System.out.println(id + " " + name);
            }


            // 判断数据是否正确
            String name = "王五";
            int id = 3;
            String sql2 = "select * from human where name = ' " + name + " ' and id = " + id;
            ResultSet rs2 = s.executeQuery(sql2);
            if(rs2.next()) System.out.println("Yes");
            else System.out.println("NO");


            // 获取总数：计数器计数
            int total = 0;
            String sql3 = "select count(*) from human";
            ResultSet rs3 = s.executeQuery(sql3);
            while(rs3.next()){
                total = rs3.getInt(1); // 第一列的个数
            }
            System.out.println(total);
        }
        catch (SQLException e){
            System.out.println("Error");
        }
    }
}
