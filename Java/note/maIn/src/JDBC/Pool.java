package JDBC;

import JDBC.DAO.DAOClass;
import com.mysql.cj.jdbc.ConnectionImpl;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

class ConnectionPool{ // 数据池类
    List<Connection> cs = new ArrayList<>();

    int size;

    public ConnectionPool(int size){
        this.size = size;
        init();
    }

    public void init(){
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            for(int i = 0 ; i < 10 ; i ++){
                Connection c = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/text", "root", "@Ycc20060308");
                cs.add(c);
            }
        }
        catch(ClassNotFoundException e){ // 可能会出现找不到库的情况
            System.out.println("Error");
        }
        catch (SQLException e){
            System.out.println("Error");
        }
    }

    public synchronized Connection getConnection(){
        while(cs.isEmpty()){
            try{
                this.wait(); // 判断是否有线程可以用，如果没有则等待
            }
            catch (InterruptedException e){
                System.out.println("Error");
            }
        }
        Connection c = cs.remove(0);
        return c;
    }

    public synchronized void returnConnection(Connection c){
        cs.add(c);
        this.notifyAll(); // 通知所有线程，可能有新的连接
    }
}

class Working extends Thread{
    private ConnectionPool cp;

    public Working(String name , ConnectionPool cp){
        super(name);
        this.cp = cp;
    }

    public void run(){
        Connection c = cp.getConnection();
        System.out.println(this.getName() + "开始工作");
        try(Statement st = c.createStatement()){
            Thread.sleep(1000);
            st.execute("select * from human");
        }
        catch (SQLException | InterruptedException e){
            System.out.println("Error");
        }
        cp.returnConnection(c);
    }
}

public class Pool {
    public static void main(String[] args) {
        // 与线性池类似，数据库也有一个数据库连接池
        // 连接池在使用之前，就会创建好一定数量的连接。
        // 如果有任何线程需要使用连接，那么就从连接池里面借用，而不是自己重新创建.
        // 使用完毕后，又把这个连接归还给连接池供下一次或者其他线程使用。
        // 倘若发生多线程并发情况，连接池里的连接被借用光了，那么其他线程就会临时等待，直到有连接被归还回来，再继续使用。
        // 整个过程，这些连接都不会被关闭，而是不断的被循环使用，从而节约了启动和关闭连接的时间。
        ConnectionPool cp = new ConnectionPool(3);
        for(int i = 0 ; i < 100 ; i ++){
            new Working("Working" + i , cp).start();
        }
    }
}
