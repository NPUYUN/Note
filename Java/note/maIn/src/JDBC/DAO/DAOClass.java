package JDBC.DAO;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class DAOClass implements DAOInterface{
    public DAOClass(){ // 构造函数：创建对象时就初始化驱动
        try{
            Class.forName("com.mysql.cj.jdbc.Driver");
        }
        catch (ClassNotFoundException e){
            System.out.println("Error");
        }
    }

    public void add(Human man){
        String sql = "insert into human values(? , ? )";
        try(Connection c = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/text", "root", "@Ycc20060308");
            PreparedStatement ps = c.prepareStatement(sql);
        ){
            ps.setInt(1 , man.id);
            ps.setString(2 , man.name);

            System.out.println(ps.executeUpdate());
        }
        catch (SQLException e){
            System.out.println("Error");
        }
    }

    public void update(Human man){
        String sql = "update human set name = ? where id = ?";
        try(Connection c = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/text", "root", "@Ycc20060308");
            PreparedStatement ps = c.prepareStatement(sql);
        ){
            ps.setInt(2 , man.id);
            ps.setString(1 , man.name);

            System.out.println(ps.executeUpdate());
        }
        catch (SQLException e){
            System.out.println("Error");
        }
    }

    public void delete(Human man){
        String sql = "delete from human where id = ?";
        try(Connection c = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/text", "root", "@Ycc20060308");
            PreparedStatement ps = c.prepareStatement(sql);
        ){
            ps.setInt(1 , man.id);

            System.out.println(ps.executeUpdate());
        }
        catch (SQLException e){
            System.out.println("Error");
        }
    }

    public Human get(int id){
        Human man = null;

        String sql = "Select * from human where id = " + id;
        try(Connection c = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/text", "root", "@Ycc20060308");
            PreparedStatement ps = c.prepareStatement(sql);
        ){
            ResultSet rs = ps.executeQuery();
            while(rs.next()){
                man.id = id;
                man.name = rs.getString("name");
            }
        }
        catch (SQLException e){
            System.out.println("Error");
        }

        return man;
    }

    public List<Human> search(){
        String sql = "Select * from human";
        try(Connection c = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/text", "root", "@Ycc20060308");
            PreparedStatement ps = c.prepareStatement(sql);
        ){
            List<Human> humans = new ArrayList<>();
            ResultSet rs = ps.executeQuery();
            while(rs.next()){
                Human man = new Human();
                man.id = rs.getInt(1);
                man.name = rs.getString(2);
                humans.add(man);
            }
            return humans;
        }
        catch (SQLException e){
            System.out.println("Error");
        }

        return null;
    }

    public List<Human> search(int start , int end){
        String sql = "Select * from human limit ? , ?";
        try(Connection c = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/text", "root", "@Ycc20060308");
            PreparedStatement ps = c.prepareStatement(sql);
        ){
            ps.setInt(1 , start);
            ps.setInt(2 , end);

            List<Human> humans = new ArrayList<>();
            ResultSet rs = ps.executeQuery();
            while(rs.next()){
                Human man = new Human();
                man.id = rs.getInt(1);
                man.name = rs.getString(2);
                humans.add(man);
            }
            return humans;
        }
        catch (SQLException e){
            System.out.println("Error");
        }

        return null;
    }
}
