package Internet;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.InetAddress;

public class IP {
    public static void main(String[] args) throws IOException {
        // 获取本机IP：InetAddress类，可能会出现找不到的错误
        InetAddress host = InetAddress.getLocalHost();
        System.out.println(host.getHostAddress());

        // Java实现ping命令：用Runtime.getRuntime().exec()可以运行windows的exe程序
        Process p = Runtime.getRuntime().exec("ping " + "192.168.31.72");
        BufferedReader br = new BufferedReader(new InputStreamReader(p.getInputStream() , "GBK")); // cmd默认用GBK
        String line = null;
        StringBuilder sb = new StringBuilder();
        while((line = br.readLine()) != null){
            if(!line.isEmpty()){
                sb.append(line + "\r\n");
            }
        }
        System.out.println("result: " + sb.toString());
    }
}
