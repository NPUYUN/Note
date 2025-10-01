package InterfaceAndInherit;

import java.util.Objects;

// 实现类：在类名后加上implements 接口名(若有多个接口，用逗号隔开)，若同时为继承和实现类，先写继承后写接口
class inter implements Interface{
    public static final String myName = "ycc"; // 常量：static 和 final 一起用

    public void print(){ //在该类里实现接口中定义的方法，访问权限必须为public
        System.out.println("OK");
    }
}

class Father{ // 声明一个类时，默认继承Object类
    String name;

    public void getName(){
        System.out.println("1");;
    }

    public static void print(){
        System.out.println("static");
    }

    public Father(){
        System.out.println("I'm your father");
    }

    public Father(String name){
        this.name = name;
    }

    public final void only(){
        System.out.println("You can not change me");
    }
}

class Son extends Father{
    String fatherName;

    public void getName(){
        System.out.println('2');// 重写
    }

    public static void print(){
        System.out.println("son static"); // 隐藏
    }

    public Son(){
        System.out.println("you are my son");
    }

    public Son(String fatherName){
        super(fatherName); // 使用super()可用显式调用父类的带参构造方法
        this.fatherName = fatherName;
        super.name = fatherName; // 使用super可以调用父类属性
        super.getName(); // 使用super可以调用父类的方法（未重写前的）
    }

    // 假设名字相同的为同一对象
    public boolean equals(Object o){ // 传入object对象
        if(o instanceof Father){ // 判断是否为该类或其子类的对象
             Father fa = (Father) o; // 转换为同一个类型
            return Objects.equals(fa.name, this.name); // 判断名字是否相同
        }
        return false; // 类不同，对象不可能相同
    }

    // public void only(); // final修饰的方法无法重写
}

class Son2 extends Father{
    String fatherName;

    public void getName(){
        System.out.println('3');
    }
}

final class Obj{
    public void finalize(){
        System.out.println("回收中");
    }
}

// class Obj2 extends Obj // final修饰的类不能被继承

class Abstracting extends Abstract{
    public void showName(){ // 实现抽象类中的抽象方法

    }
}


public class Main {
    private boolean canVisit;
    private static boolean canMeet;

    // 非静态内部类
    class InnerObj{
        public void canOut(){
            System.out.println(canVisit); // 非静态内部类可以直接访问private属性
        }
    }

    // 静态内部类
    static class StaticInnerObj{
        public void canOut(){
            System.out.println(canMeet); // 静态内部类只可以访问private static属性
        }
    }

    public static void main(String[] args) {
        // 对象转型：当引用类型和对象类型不一致时，需要转型
        // 判别方法：将 右边 当作 左边 来用，看看行不行
        // 转型后引用类型不变，只改变其指向的对象
        // 子类转父类/实现类转换为接口 (向上转型)：一定可以
        Son s1 = new Son();
        Father f1 = new Father();
        f1 = s1;

        inter i1 = new inter();
        Interface I1 = i1;

        // 父类转子类/接口转换为实现类 (向下转型)：强制转换，有时会失败(ClassCastException)
        // 能不能转换成功关键看右边指向哪种对象，对象类型一致则可以转换
        Son s2 = new Son();
        s2 = (Son) f1;  // 强制类型转换（类似其他数据类型）

        inter i2 = new inter();
        i2 = (inter) I1;

        // 没有继承关系的两个类无法转换

        // 判断一个引用所指向的对象的类型是否为某个类型或者该类型的子类：引用变量 instanceof 类型
        System.out.println(f1 instanceof Father);
        System.out.println(s2 instanceof Son);


        // 重写：子类可以重写父类的对象方法
        Son s3 = new Son();
        s3.name = "ZXT";
        s3.fatherName = "YCC";
        s3.getName(); // 执行重写的方法

        // 隐藏：子类可以重写父类的类方法
        Father.print();
        Son.print();
        Father f5 = new Son();
        f5.print(); // 类方法只与引用类型有关，和其指向的对象类型无关，与实例无关


        // 多态
        // 操作符的多态：一个操作符具备不同的作用
        int a = 1 + 2; // + 表示数字相加
        String str = "1" + "2"; // + 表示字符串拼接

        // 类的多态：同一类型，同一方法，呈现不同状态
        // 条件：父类(接口)引用指向子类对象，且调用的方法有重写
        Father f3 = new Son();
        Father f4 = new Son2();
        f3.getName();
        f4.getName();


        // super关键字
        // 实例化子类时，父类的构造方法一定会被调用，且默认调用无参的构造方法
        Son s4 = new Son();
        // 使用super()可以显式调用父类的带参构造方法
        // 使用super可用调用父类的属性、方法
        s4 = new Son("YCC");
        System.out.println(s4.fatherName + s4.name);


        // Object类：所有类的父类，在声明类时默认继承Object类，其中的方法为所有类共同所有
        // toString方法：返回当前对象的字符串表达
        System.out.println(s3.toString());

        // finalize方法：当对象没有被任何引用指向时，会累积，当累积到一定数量时会被该方法回收
        // finalize方法不需要主动调用，JVM会自动调用，但可以重写
        Obj s5;
        for (int i = 0 ; i < 380000 ; i ++){
            s5 = new Obj(); // 一旦一个对象被回收，他的finalize()方法就会被调用
        }

        // equals方法：判断两个对象是否相同，可以重写（自定义相同条件）
        System.out.println(s3.equals(s4));

        // == 符号：判断两个引用是否指向同一个对象
        System.out.println(s1 == s2);

        // hashCode方法：返回对象的哈希值
        System.out.println(s4.hashCode());

        // 其他高级方法：线性同步相关方法、getClass方法（反射）等


        // final修饰符
        // final修饰类、方法、基本类型变量、引用时有不同的含义
        // final修饰类：该类不能被继承
        // final修饰方法：该方法不能被重写

        // final修饰基本类型变量：只能赋值一次
        final int only = 1;
        // only = 2;

        // final修饰引用：只有一次指向对象的机会
        final Obj o1 = new Obj();
        // o1 = new Obj();

        // 常量：公开访问，不会变化的值


        // 抽象类：必须作为独立的文件(和public class一致)
        // 抽象方法：没有实现体的方法（空方法），有abstract修饰
        // 抽象类：含有抽象方法的类必须声明为抽象类，不含有的也可以声明为抽象类，有abstract修饰
        // 继承抽象类的类必须提供抽象方法，抽象类不能实例化
        // 与接口的区别：
        // 接口：子类可以实现多个接口，接口声明的属性只能是public static final，成员方法一般都为抽象方法
        // 抽象类：子类只能继承一个抽象类，抽象类声明的属性和方法没有限制


        // 内部类：在类的内部声明的类，必须位于成员的位置
        // 非静态内部类：可以直接访问外部类的private属性
        InnerObj inner = new Main().new InnerObj(); // 实例化：new 外部类().new 内部类()
        Main temp = new Main();
        temp.canVisit = true;
        InnerObj inner1 = temp.new InnerObj(); // 非静态内部类可以直接访问private属性

        // 静态内部类：不能访问外部类的实例属性和方法，可以访问外部类的私有静态成员
        StaticInnerObj Sinner = new StaticInnerObj(); // 实例化和普通类一致
        Main.canMeet = true;
        Sinner.canOut();

        // 匿名类：声明一个类的同时实例化(多用于含有抽象方法的类)，但这个类没有命名，系统自动分配。可以声明在任何代码块里
        // 只要在抽象类/接口中创建一个对象，并在末尾加上{}代码块，在代码块中完成抽象方法的实现即可
        Abstract abs = new Abstract() {
            public void showName() {
                System.out.println("OK");
            }
        };
        abs.name = "YCC";
        abs.showName();

        // 本地类：有名字的匿名类，可以声明在任何代码块里
        class SomeAbstract extends Abstract{
            public void showName(){
                System.out.println("OK");
            }
        }
        SomeAbstract Sabs = new SomeAbstract();
        Sabs.name = "YCC";
        Sabs.showName();

        // 在匿名类中使用外部局部变量，外部的局部变量必须为final（系统会自动加）
        final int fi1 = 1;
        int fi2 = 2;
        Abstract abs2 = new Abstract() {
            public void showName(){
                System.out.println(fi1 + fi2);
            }
        };


        // 默认方法：在接口中实现的具体方法，用default修饰
        inter inter = new inter();
        inter.dePrint();


    }
}
