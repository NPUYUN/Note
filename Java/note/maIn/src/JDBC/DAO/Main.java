package JDBC.DAO;

public class Main {
    public static void main(String[] args) {
        // DAO实际上为通过ORM的思路，将数据库的操作封装到一个类里面
        // 先创建一个DAO接口，提供增删查改的操作
        // 再设计实现类实现接口即可
        DAOClass dao = new DAOClass();
        System.out.println(dao.search());
    }
}
