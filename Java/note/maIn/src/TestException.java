import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

class NumberException extends Exception{
    public NumberException(){

    }

    public NumberException(String str){
        super(str);
    }
}

public class TestException {
    // throw
    public boolean canBigger(int x , int y){
        if(x < 0 || y < 0) throw new IllegalArgumentException("数值错误"); // 主动抛出错误
        return true;
    }

    // throws
    public void FileOpen() throws FileNotFoundException{ // 声明该方法可能抛出的异常
        File f = new File("d:/try");
        System.out.println("打开中");
        new FileInputStream(f);
        System.out.println("成功打开");
    }

    // 自定义异常
    public boolean numberError(int x) throws NumberException{ // 声明该方法可能抛出的异常
        if(x < 0) throw new NumberException("NO"); // 抛出自定义异常
        if(x > 10) return true;
        return false;
    }

    public static void main(String[] args) {
        // 异常处理的常见手段：try catch finally throws
        // try catch
        // 将可能出错的代码放在try中，当try中代码出错时会执行catch里面的内容
        File f = new File("d:/try.exe"); // 创建文件对象

        try{
            System.out.println("打开中");
            new FileInputStream(f); // 试图打开文件
            System.out.println("成功打开");
        }
        catch (FileNotFoundException e){ // 出现文件无法打开异常时
            System.out.println("打开失败");
            e.printStackTrace(); // 打印出方法调用痕迹
        }

        // 使用异常的父类进行catch
        // 异常的父类为Exception，可以用来捕捉任何异常
        try{
            System.out.println("打开中");
            new FileInputStream(f);
            System.out.println("成功打开");
        }
        catch (Exception e){ // 使用父类异常
            System.out.println("打开失败");
        }

        // 多异常捕捉方法
        // 方法一：分别catch
        try{
            System.out.println("打开中");
            new FileInputStream(f);
            System.out.println("成功打开");

            SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
            Date d = sdf.parse("2016-06-03");
        }
        catch (FileNotFoundException e){
            System.out.println("打开失败");
        }
        catch (ParseException e){
            System.out.println("格式错误");
        }

        // 方法二：多个异常放在一起捕捉（无法确定是哪个异常）
        try{
            System.out.println("打开中");
            new FileInputStream(f);
            System.out.println("成功打开");

            SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
            Date d = sdf.parse("2016-06-03");
        }
        catch (FileNotFoundException | ParseException e){ // 使用|隔开异常
            System.out.println("打开失败");
        }


        // finally：无论出不出现异常，finally中的代码都会被执行
        // 若try catch finally中均有return，则finally中的return会覆盖掉其中所有的return，只执行这一个return
        try{
            System.out.println("打开中");
            new FileInputStream(f);
            System.out.println("成功打开");
        }
        catch (FileNotFoundException e){
            System.out.println("打开失败");
        }
        finally{
            System.out.println("OK");
        }


        // throw和throws
        // throw：方法体内主动抛出异常
        // trow new ExceptionType(String)
        TestException ts = new TestException();
        // ts.canBigger(-1 , -2);

        // throws：方法体外声明该方法可能抛出的异常，提示调用该方法时要处理
        try{
            ts.FileOpen();
        }
        catch (FileNotFoundException e){
            System.out.println("调用异常：" + e);
        }


        // 异常的分类
        // 可查异常：必须处理的异常，不处理则编译不通过，如FileNotFoundException
        // 运行时异常：运行时产生的异常，不必须处理，不会有编译错误，如下标越界(ArrayIndexOutOfBoundsException)、除0异常(ArithmeticException)
        // 错误：系统级别的异常，一般为内存用光了(OutOfMemoryError)，不必须处理


        // Throwable：Exception和Error的父类
        // Exception里包括可查异常和运行时异常
        try{
            System.out.println("打开中");
            new FileInputStream(f);
            System.out.println("成功打开");
        }
        catch (Throwable e){ // 使用Throwable类显示异常
            System.out.println("打开失败");
        }


        // 自定义异常
        // 创建一个类用作自定义异常，继承Exception类
        // 该类继承Exception的两个构造方法：无参的构造方法，带参的（String s）的构造方法（调用父类的构造方法）
        try{
            ts.numberError(-1);
        }
        catch (NumberException e){
            System.out.println(e);
        }
    }
}
