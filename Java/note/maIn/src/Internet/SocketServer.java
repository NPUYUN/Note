package Internet;

import java.io.DataInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class SocketServer {
    public static void main(String[] args) {
        try{
            // 建立连接 -- 服务端
            ServerSocket ss = new ServerSocket(8888); // 服务端打开端口8888
            Socket s = ss.accept(); // 在端口上监听，看是否有连接请求过来
            System.out.println(s);


            // 收发数字
            // 服务器：打开输入流，接收数字
            InputStream is = s.getInputStream(); // 打开输入流
            int msg = is.read(); // 读取客户端发送的数据
            System.out.println(msg);


            // 收发字符串
            // 使用数据流对字节流进行封装（用字节流比较麻烦）
            // 把输入流封装到DataInput中，使用readUTF读取字符串
            DataInputStream dis = new DataInputStream(is); // 将输入流封装到DataInputStream
            String str = dis.readUTF();
            System.out.println(str);


            // 接收用Scanner发送的数据
            System.out.println(dis.readUTF());

            dis.close(); // 读取完关闭数据流
            is.close(); // 读取后关闭流

            // 用完要关闭湍口和监听
            s.close();
            ss.close();
        }
        catch (IOException e){ // 可能会出现错误
            System.out.println("Error");
        }

    }
}
