package JDBC;

import java.sql.*;

public class SpecialOperate {
    public static void main(String[] args) {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
        }
        catch(ClassNotFoundException e){
            System.out.println("Error");
        }

        String sql = "insert into student values(? , ? , ?)";

        try(Connection c = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/try", "root", "@Ycc20060308");
            PreparedStatement ps = c.prepareStatement(sql,Statement.RETURN_GENERATED_KEYS);) {
            // 获取自增长的id
            // 当表中id设置为自增长时，在通过execute或者executeUpdate执行插入语句后，MySQL会为其分配一个自增长id
            // 需要通过Statement或者PreparedStatement的getGeneratedKeys获取该id，注意在PreparedStatement里加上Statement.RETURN_GENERATED_KEYS参数，以确保会返回自增长ID
            ps.setInt(1 , 2);
            ps.setString(2 , "李四");
            ps.setString(3 , "2024303469");
            ps.execute();

            ResultSet rs = ps.getGeneratedKeys(); // 获取自增长id
            while(rs.next()){
                System.out.println(rs.getInt(1));
            }


            // 查看数据库层面的元数据
            DatabaseMetaData dmd = c.getMetaData();

            // 获取服务器产品名称
            System.out.println(dmd.getDatabaseProductName());
            // 获取服务器产品版本号
            System.out.println(dmd.getDatabaseProductVersion());
            // 获取服务器用作类别和表名之间的分隔符
            System.out.println(dmd.getCatalogSeparator());
            // 获取驱动版本
            System.out.println(dmd.getDriverVersion());
            // 获取数据库名称
            ResultSet rs2 = dmd.getCatalogs();
            while(rs2.next()){
                System.out.println(rs2.getString(1));
            }
        }
        catch (SQLException e){
            System.out.println("Error");
            e.printStackTrace();
        }

    }
}
