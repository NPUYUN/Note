package Chatter;

import javax.swing.*;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.net.Socket;

public class Send extends Thread{
    private Socket s;
    private JTextArea ta;

    public Send(Socket s , JTextArea ta){
        this.s = s;
        this.ta = ta;
    }

    public void run(){
        try{
            OutputStream os = s.getOutputStream();
            DataOutputStream dos = new DataOutputStream(os);
                ta.addKeyListener(new KeyAdapter() {
                    @Override
                    public void keyPressed(KeyEvent e) {
                        if(e.getKeyChar() == '\n'){
                            String text = ta.getText();
                            String[] line = text.split("\n");
                            try{
                                dos.writeUTF(line[line.length - 1]);
                            }
                            catch (IOException i){
                                i.printStackTrace();
                            }
                        }
                    }
                });
        }
        catch (IOException e){
            e.printStackTrace();
        }
    }
}
