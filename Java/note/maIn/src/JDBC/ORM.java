package JDBC;

import java.sql.*;

class Human{
    int id;
    String name;
}

public class ORM {
    public static Human get(int id){ // 根据数据库返回一个对象
        Human man = null;
        //ORM：对象与关系数据库的映射
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
        }
        catch(ClassNotFoundException e){
            System.out.println("Error");
        }

        try(Connection c = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/text", "root", "@Ycc20060308");
            Statement s = c.createStatement();) {

            String sql = "select * from human where id = " + id;

            ResultSet rs = s.executeQuery(sql);

            if(rs.next()){
                man = new Human();
                String name = rs.getString(2);
                man.name = name;
                man.id = id;
            }
        }
        catch (SQLException e){
            System.out.println("Error");
        }

        return man;
    }

    public static void main(String[] args) {
        Human man = get(1);
        System.out.println(man.name);
    }
}
