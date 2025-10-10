import javax.swing.plaf.basic.BasicOptionPaneUI;
import java.io.File;
import java.io.FileInputStream;
import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.Member;
import java.lang.reflect.Method;
import java.util.Objects;
import java.util.Properties;

class Teacher{
    String name;
    static String school = "NPU";

    public Teacher(){ // 显式公共无参构造函数

    }

    public void setName(String name){
        this.name = name;
    }
}

public class Reflection {
    public static void main(String[] args) {
        // 类对象：所有的类都存在一个类对象，用于提供类本身的信息，如构造方法个数，属性个数等

        try{
            String className = "Teacher";
            // 获取类对象：
            // 方式一：Class.forName
            Class pClass1 = Class.forName(className);

            // 方式二：类名.class
            Class pClass2 = Teacher.class;

            // 方式三：new 类名().getClass()
            Class pClass3 = new Teacher().getClass();

            // 注意：获取类对象时，类属性(static)会被初始化

            // 反射机制：先获取到类对象，然后通过类对象获取”构造器对象“，再通过构造器对象创建一个对象
            Constructor c = pClass1.getConstructor(); // 构造器，获取公共的无参构造函数(必须有显式的无参构造函数，否则报错)
            Teacher t = (Teacher) c.newInstance(); // 通过构造器实例化
            t.name = "YCC";
            System.out.println(t.name);

            // 使用反射机制修改属性值
            // 获取类中的字段
            Field f1 = t.getClass().getDeclaredField("name"); // 获取name字段
            // getField和getDeclaredField的区别：
            // getField: 只能获取public的和从父类继承来的字段。
            // getDeclaredField：可以获取本类所有的字段，包括private的，但是不能获取继承来的字段
            // 注意：只能获取到private，而不能访问值，除非加上setAccessible(true)
            // 修改字段值
            f1.set(t , "ycc");
            System.out.println(t.name);

            // 使用反射机制调用方法
            // 获取方法名
            Method m = t.getClass().getMethod("setName", String.class); // 获取方法名以及需要的参数
            // 对对象t调用该方法
            m.invoke(t , "YCC");
            System.out.println(t.name);

        }
        catch (Exception e){
            System.out.println("Error");
            e.printStackTrace();
        }
        /*
        反射机制的用处：（Spring框架基本原理）
        准备一个配置文件，存放类名以及要调用的方法名
        随后在测试类中取出类名和方法名，然后通过反射去调用方法
        当需要切换类以及方法时，只需要修改配置文件中的类名和方法名，无需修改代码
        */
        // 模板：
        // 此时配置文件内容为：
        // class=类名
        // method=方法名
        try{
            File springConfigFile = new File("");
            Properties springConfig = new Properties(); // Properties用于处理配置文件
            springConfig.load(new FileInputStream(springConfigFile));
            String className = (String) springConfig.get("class");
            String methndName = (String) springConfig.get("method");

            // 根据类名获取类对象
            Class clazz = Class.forName(className);
            // 根据方法名获取方法对象
            Method m = clazz.getMethod(methndName);
            // 获取构造器
            Constructor c = clazz.getConstructor();
            // 根据构造器实例化对象
            Object service = c.newInstance();
            // 调用对象指定方法
            m.invoke(service);
        }
        catch (Exception e){
            System.out.println("Error");
        }
    }
}