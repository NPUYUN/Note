package Chatter;

import javax.swing.*;
import java.io.DataInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.Socket;
import java.net.UnknownHostException;

public class Receive extends Thread{
    private Socket s;
    private JTextArea ta;

    public Receive(Socket s , JTextArea ta){
        this.s = s;
        this.ta = ta;
    }

    public void run(){
        try{
            InputStream is = s.getInputStream();
            DataInputStream dis = new DataInputStream(is);
            while(true){
                ta.append(dis.readUTF() + "\n");
            }
        }
        catch (IOException e){
            e.printStackTrace();
        }
    }
}
