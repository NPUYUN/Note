package Chatter;

import java.io.IOException;
import java.net.Socket;

public class Client {
    public static void main(String[] args) {
        GUI g = new GUI();
        try{
            Socket s = new Socket("127.0.0.1" , 8888);

            new Receive(s , g.getTa()).start();
            new Send(s , g.getTa()).start();
        }
        catch (IOException e){
            e.printStackTrace();
        }
    }
}
