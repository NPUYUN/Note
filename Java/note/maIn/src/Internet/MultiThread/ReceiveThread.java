package Internet.MultiThread;

import java.io.DataInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.Socket;

// 接收消息线程
public class ReceiveThread extends Thread {
    private Socket s;

    public ReceiveThread(Socket s){
        this.s = s;
    }

    public void run(){
        try{
            InputStream is = s.getInputStream();
            DataInputStream dis = new DataInputStream(is);
            while(true){
                String msg = dis.readUTF();
                System.out.println(msg);
            }
        }
        catch (IOException e){
            e.printStackTrace();
        }
    }
}
