package Internet;

import java.io.DataOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Scanner;

public class SocketClient {
    public static void main(String[] args) {
        try{
            // 建立连接 -- 客户端
            Socket s = new Socket("127.0.0.1" , 8888); // 连接到本机的8888端口
            System.out.println(s);


            // 收发数字
            // 客户端：打开输出流，发送数据
            OutputStream os = s.getOutputStream();
            os.write(110); // 发送数字到服务端


            // 收发字符串
            // 使用数据流对字节流进行封装（用字节流比较麻烦）
            // 把输出流封装到DataOutput中，使用writeUTF读取字符串
            DataOutputStream dos = new DataOutputStream(os); // 将输出流封装到DataOutputStream
            dos.writeUTF("OK"); // 使用writeUTF发送字符串


            // 使用Scanner读取控制台的输入，并发送到服务端
            Scanner sc = new Scanner(System.in);
            dos.writeUTF(sc.next());

            dos.close();// 发送完关闭数据流
            os.close(); // 发送完关闭流

            // 用完要关闭湍口和监听
            s.close();
        }
        catch(UnknownHostException e){ // 可能会出错
            System.out.println("Error");
        }
        catch (IOException e){
            System.out.println("Error");
        }
    }
}
