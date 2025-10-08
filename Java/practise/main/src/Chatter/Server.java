package Chatter;

import javax.swing.*;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.UnknownHostException;

public class Server {
    public static void main(String[] args) {
        GUI g = new GUI();
        try{
            ServerSocket ss = new ServerSocket(8888);
            Socket s = ss.accept();

            new Receive(s , g.getTa()).start();

            new Send(s , g.getTa()).start();
        }
        catch (UnknownHostException e){
            e.printStackTrace();
        }
        catch (IOException e){
            e.printStackTrace();
        }
    }
}
