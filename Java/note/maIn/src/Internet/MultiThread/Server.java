package Internet.MultiThread;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

// 因为接受和发送都在主线程，无法同时进行
// 为了实现同时收发消息，可以将收发消息放在两个不桐的线程中进行

// 服务端，一旦接收到连接，就启动收发的两个个线程
public class Server {
    public static void main(String[] args) {
        try{
            ServerSocket ss = new ServerSocket(8888);
            Socket s = ss.accept();

            // 启动发送消息的线程
            new SendThread(s).start();
            // 启动接受消息的线程
            new ReceiveThread(s).start();
        }
        catch (IOException e){
            e.printStackTrace();
        }
    }
}
