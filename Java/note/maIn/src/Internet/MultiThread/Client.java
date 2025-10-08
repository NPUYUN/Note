package Internet.MultiThread;

import java.io.IOException;
import java.net.Socket;
import java.net.UnknownHostException;

// 因为接受和发送都在主线程，无法同时进行
// 为了实现同时收发消息，可以将收发消息放在两个不桐的线程中进行

// 客户端：一旦接收到连接，就启动收发的两个个线程
public class Client {
    public static void main(String[] args) {
        try{
            Socket s = new Socket("127.0.0.1" , 8888);

            // 启动发送消息的线程
            new SendThread(s).start();
            // 启动接受消息的线程
            new ReceiveThread(s).start();
        }
        catch (UnknownHostException e){ // 可能会出现无法找到主机的错误，与其父类错误分开，以便区分
            e.printStackTrace();
        }
        catch (IOException e){
            e.printStackTrace();
        }
    }
}
