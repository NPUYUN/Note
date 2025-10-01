import java.io.*;
import java.util.Date;
import java.util.Scanner;

class ObjStream implements Serializable{
    // 表示这个类当前的版本号
    private static final long serialVersionUID = 1L;

    public String name;
}

public class IO {
    public static void main(String[] args) {
        // 文件
        // 创建文件对象：new File(文件路径)
        // 绝对路径创建
        File f1 = new File("d:/try");
        System.out.println(f1.getAbsoluteFile()); // 获取f1的绝对路径

        // 相对路径：相对于工作目录
        File f2 = new File("IO.java");
        System.out.println(f2.getAbsoluteFile());

        // 将File对象作为父目录创建对象：File(File对象，文件路径)
        File f3 = new File(f1 , "try.exe");
        System.out.println(f3.getAbsoluteFile());

        // 文件常用方法
        // 判断文件是否存在：exists()
        System.out.println(f1.exists());

        // 判断是否为文件夹：isDirectory()
        System.out.println(f2.isDirectory());

        // 判断是否为文件而非文件夹：isFile()
        System.out.println(f3.isFile());

        // 返回文件长度：length()
        System.out.println(f2.length());

        // 返回文件修改时间：lastModified()
        System.out.println(new Date(f2.lastModified()));

        // 设置文件修改时间：setLastModified(number)
        f2.setLastModified(0);

        // 文件重命名：renameTo(File对象)：File对象指向改前同一目录下改后的文件
        File f4 = new File("IAndO");
        f2.renameTo(f4);

        // 以字符串数组的形式返回当前文件夹的所有文件（不包括子文件和子文件夹）:list()
        String[] slist = f2.list();

        // 以文件数组的形式，返回当前文件夹下的所有文件（不包含子文件及子文件夹）：listFiles()
        File[] flist = f2.listFiles();

        // 以字符串的形式返回所在文件夹：getParent()
        String p = f2.getParent();

        // 以文件的形式返回所在文件夹：getParentFile()
        File f5 = f2.getParentFile();

        // 创建文件夹，如果父文件夹不存在，则无效：mkdir()
        f1.mkdir();

        // 创建文件夹，如果父文件夹不存在，就会创建父文件夹：mkdirs()
        f1.mkdirs();

        // 创建空文件，如果父类文件夹不存在，则会抛出异常：createNewFile()
        try{
            f2.createNewFile();
        }
        catch (Exception e){
            System.out.println("ERROR");
        }

        // 以File数组形式列出所有的盘符（静态方法）：listRoots()
        File[] f6 = File.listRoots();

        // 删除文件：delete()
        f1.delete();

        // JVM结束时删除文件，用于临时文件的删除：deleteOneExit()
        f1.deleteOnExit();


        // 文件输入流：FileInputStream类
        // 通过输入流可以把数据从硬盘读取到Java虚拟机中来，也就是读取到内存中
        // 建立流：
        try{
            File f = new File("d/");
            FileInputStream fis = new FileInputStream(f);
        }
        catch(FileNotFoundException e){
            System.out.println("打开失败");
        }

        // 文件输出流
        // 通过输入流可以把数据从内存中写入文件
        // 建立流：
        try{
            File f = new File("d/");
            FileOutputStream fis = new FileOutputStream(f);
        }
        catch(FileNotFoundException e){
            System.out.println("打开失败");
        }


        // 字节流
        // 以字节流的形式读取文件：FileInputStream
        try{
            File f = new File("note/try.txt");
            FileInputStream fis = new FileInputStream(f);

            byte[] all = new byte[(int)f.length()]; // 创建字节数组，长度为文件长度
            System.out.println(fis.read(all));; // 以字节流的形式读取文件，注意传入的是字节数组，返回的是字节数
            for(byte b : all) System.out.println(b);
            System.out.println(fis.read(all , 0 , 1)); // 可以传入开始点和长度两个数据，表示从某个点开始读取某个长度的数据
            fis.close(); // 每次使用完流要关闭
        }
        catch(IOException e){
            System.out.println("打开失败");
        }

        // 以字节流的形式向文件写入数据：FileOutputStream
        try{
            File f = new File("note/try.txt");
            FileOutputStream fos = new FileOutputStream(f); // 默认为覆盖模式，即先清空，后写入

            byte[] data = {88 , 89}; // 创建输入的字节数组，分别表示X,Y
            fos.write(data); // 以字节流的形式将数据写入文件，注意传入的是字节数组
            fos.close(); // 每次使用完流要关闭

            FileOutputStream fos2 = new FileOutputStream(f , true); // 改为追加模式，即直接写入
            fos2.write(data,0 , 1); // 可以传入开始点和长度两个数据，表示从data的某个点开始写入某个长度的数据
            fos2.close();
        }
        catch(IOException e){
            System.out.println("打开失败");
        }


        // 关闭流的方式
        // 所有流使用完毕后都应该关闭
        // 方式一：再try中关闭，参照前文
        // 如果文件不存在，会在读取的时候抛出异常，就不会执行关闭流的代码，存在隐患，不推荐使用

        // 方式二：在finally中关闭：标准的关闭流方式，较为繁琐，要求如下：
        // 首先把流声明到try外（null），扩大作用域
        // 在finally关闭之前要检查引用是否为空
        // 关闭的时候需要再一次进行try catch处理
        FileInputStream fis2 = null; // 声明在try外，为null
        try{
            File f = new File("note/try.txt") ;
            fis2 = new FileInputStream(f);
            byte[] all = new byte[(int)f.length()];
            System.out.println(fis2.read(all));
            for(byte b : all) System.out.println(b);
        }
        catch(IOException e){
            System.out.println("打开失败");
        }
        finally {
            if(null != fis2){ // 判断是否为空
                try{ // 检测异常
                    fis2.close(); // 关闭流
                }
                catch(IOException e){
                    System.out.println("关闭失败");
                }
            }
        }

        // 方式三：try()：try-with-resources
        // 在try-catch或finally结束时，会自动关闭
        File fx = new File("note/try.txt") ;
        try(FileInputStream fis3 = new FileInputStream(fx)){ // 将流定义在try()中，会自动关闭
            byte[] all = new byte[(int)fx.length()];
            System.out.println(fis3.read(all));
            for(byte b : all) System.out.println(b);
        }
        catch(IOException e){
            System.out.println("打开失败");
        }


        // 字符流
        // 使用字符流读取文件：FileReader
        File fy = new File("note/try.txt");
        try(FileReader fr = new FileReader(fy)){
            char[] all = new char[(int)fy.length()]; // 创建字符数组，长度为文件长度
            fr.read(all); // 以字符流的形式读取文件所有内容
            for(char b : all) System.out.println(b);
        }
        catch(IOException e){
            System.out.println("ERROR");
        }

        //使用字符流把字符串写入文件：FileWriter
        try(FileWriter fw = new FileWriter(fy)){
            String s = "I love you";
            char[] cs = s.toCharArray();
            fw.write(cs);
        }
        catch (IOException e){
            System.out.println("ERROR");
        }
        // write和read的其他用法和之前相同


        // 编码：Java默认使用Unicode
        // 对于FileInputStream，JVM会自动找到Unicode中对应的数字
        // 对于FileReader：默认为GBK，不能手动设置编码方式
        // 若想使用其他编码方式，只能用InputStreamReader来代替
        // new InputStream(new FileInputStream(fy).Charset.forName("UTF-8"));


        // 缓存流：通过缓存区读取写入，减少IO操作，提高性能
        // 一次读取一行数据：BufferedReader
        try(FileReader fr = new FileReader(fy) ; BufferedReader br = new BufferedReader(fr)){ // 缓存流必须要建立在一个流的基础上
            String line = br.readLine(); // 一次读一行
            System.out.println(line);

        }
        catch(IOException e){
            System.out.println("ERROR");
        }

        // 一次写入一行数据：PrintWriter
        try(FileWriter fw = new FileWriter(fy, true) ; PrintWriter pw = new PrintWriter(fw)){ // 缓存流必须要建立在一个流的基础上
            pw.println("I Love You"); // 一次写入一行
        }
        catch(IOException e){
            System.out.println("ERROR");
        }

        // 一般来说，只有当缓存区满了才能写入硬盘
        // 立即把数据写入硬盘：flush
        try(FileWriter fw = new FileWriter(fy, true) ; PrintWriter pw = new PrintWriter(fw)){ // 缓存流必须要建立在一个流的基础上
            pw.println("I Love You");
            pw.flush(); // 立即写入
            pw.println("I Love You");
            pw.flush();
            pw.println("I Love You");
            pw.flush();
        }
        catch(IOException e){
            System.out.println("ERROR");
        }


        // 数据流：附有额外信息以确定输入的成分的输入输出
        // 使用数据流的writeUTF()和readUTF()可以进行数据的格式化读写，write数据类型()和read数据类型()可以读写特定的数据类型，注意数据类型首字母大写
        // 数据输出流：DataOutputStream
        File ft = new File("note/try2.txt");
        try(FileOutputStream fos = new FileOutputStream(ft) ; DataOutputStream dos = new DataOutputStream(fos)){ // 数据流必须基于一个流上
            dos.writeBoolean(true); // 写入boolean类型数据
            dos.writeInt(20); // 写入int类型数据
            dos.writeUTF("FUCK YOU"); // 写入格式化字符串
        }
        catch (IOException e){
            System.out.println("ERROR");
        }

        // 数据输入流：DataInputStream
        // 要用DataInputStream读入一个文件，该文件必须是DataOutputStream写出的，否则会报错
        try(FileInputStream fis = new FileInputStream(ft) ; DataInputStream dis = new DataInputStream(fis)){ // 数据流必须基于一个流上
            boolean b = dis.readBoolean(); // 读取boolean类型数据
            int i = dis.readInt(); // 读取int类型数据
            String s = dis.readUTF(); // 读取格式化字符串
            System.out.println(b);
            System.out.println(i);
            System.out.println(s);
        }
        catch (IOException e){
            System.out.println("ERROR");
        }


        // 对象流：把一个对象以流的形式传输（序列化）给其他介质
        // 该对象所对应的类必须实现Serializable接口
        // 对象输入流：ObjectInputStream，有方法readObject() 读取对象
        // 对象输出流：ObjectOutputStream，有方法writeObject(Object) 写入对象
        ObjStream os = new ObjStream();
        os.name = "YCC";

        File fo = new File("note/ObjStream.ojs");
        try(FileOutputStream fos = new FileOutputStream(fo);
            ObjectOutputStream ops = new ObjectOutputStream(fos);// 对象流必须基于一个流上
            FileInputStream fis = new FileInputStream(fo);
            ObjectInputStream ips = new ObjectInputStream(fis)) // 对象流必须基于一个流上
        {
            ops.writeObject(os); // 写入对象
            ObjStream os2 = (ObjStream) ips.readObject(); // 读取对象
            System.out.println(os2.name);
        }
        catch (IOException | ClassNotFoundException e){ // ClassNotFoundException：读取对象文件失败时抛出
            System.out.println("ERROR");
        }


        // System.in与System.out
        // System.out：在控制台输出数据
        System.out.println("FUCK");

        // System.in：从控制台输入数据，由InputStream类型接收
        try(InputStream is = System.in){
            int i = is.read(); // 读取控制台输入，注意：控制台输入的均为字符，会读取第一个字符的ASCII码
            System.out.println(i);
        }
        catch (IOException e){
            System.out.println("ERROR");
        }

        // Scanner实现更高级的读入
    }
}
