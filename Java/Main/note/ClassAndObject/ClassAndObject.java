package ClassAndObject; // 必须在最开始的地方声明包名
// 在同一个包下的类可以直接使用
import java.util.*; // 不在一个包下的类需要import后才能使用(* 表示导入所有类，可以替换成想要导入的类)

class Hero{
    String name;
    int hp;
    int speed;

    public int getSpeed(){
        return speed;
    }
}

// 单例模式三要素：构造方法私有化、静态属性指向实例、public static的 get方法，返回前面的静态属性
// 饿汉式单例模式模板
class hunger{
    // 私有化构造方法使得外部无法通过new进行实例化
    private hunger(){

    }

    // 类属性，用于指向一个实例化对象
    private static hunger item = new hunger();

    // 给出类方法给外部使用：获取一个实例
    public static hunger getItem(){
        return item;
    }
}

// 懒汉式单例模式模板
class lazy{
    // 私有化构造方法使得外部无法通过new进行实例化
    private lazy(){

    }

    // 类属性：用于指向一个实例化对象，但暂时指向null
    private static lazy item;

    // 给出类方法给外部使用：获取一个实例
    public static lazy getItem(){
        // 第一次访问时，对象为null，此时实例化一个对象
        if(null == item) item = new lazy();

        return item;
    }
}


// 枚举类型
enum Order{
    ONE , TWO , THREE // 建议大写，默认从1开始，与C++一致
}

public class ClassAndObject extends Hero { // 继承语法为在类声明后加上 extends 类名 表示继承该类(若父类不止一个可用逗号隔开)
    String name;

    // 参数一般可以为基本数据类型，也可以为类类型等
    // 参数为类类型，此时传入参数和形参引用地址相同
    public void printHero(ClassAndObject man){
        System.out.println(man.name + man.hp);
    }

    // 一般的方法重载
    public void print(int a){
        System.out.println(a);
    }

    public void print(int a , int b){
        System.out.println(a + b);
    }

    // 含有可变数量参数的重载：形参为：数据类型... 变量名
    public void printout(){
        System.out.println(" ");
    }

    public void printout(int ... items){
        for(int i : items) System.out.println(i); // 变量相当于一个存储对应数据类型的数组
    }


    // 构造方法：方法名和类名一致，没有返回类型(注意没有void)
    // 构造方法可以有参，也可以无参
    public ClassAndObject(){ // 无参的构造方法，若不写会默认提供一个无参的构造方法
        System.out.println("OK"); // 实例化对象时，必调用构造方法
    }
    // 构造方法也可以重载
    public ClassAndObject(String theName){ // 创建一个有参的构造方法时，默认的无参方法则会消失
        name = theName;
    }


    // this 的使用
    // this代表当前对象
    public void showAddress(){
        System.out.println(this);
    }

    // 用this访问属性
    public void setName(String name){
        this.name = name; // this.name 表示的时对象的name属性，而后面的name表示传入的参数
    }

    // 在构造方法里用this调用其他构造方法
    public ClassAndObject(String name , int hp){
        this(name); // 调用只有一个参数的构造方法
        this.hp = hp;
    }


    // 四种访问修饰符：写在数据类型之前
    // 类与类的关系有：自身、同包子类、不同包子类、同包类以及其他类
    // private(私有的)：只有自身可以访问
    private int pri; // 私有属性
    private void priMethod(){
        System.out.println("private"); // 私有方法
    }

    // package/friendly/default：无修饰符(友好的)，自身和同包可以访问
    int fri; // 友好属性
    void friMethod(){
        System.out.println("friendly"); // 友好方法
    }

    // protected(受保护的)：自身，同包子类、同包类、不同包子类均可访问
    protected int pro; // 受保护的属性
    protected void proMethod(){
        System.out.println("protected");
    }

    // public(公开的)：均可访问
    public int pub;
    public void pubMethod(){
        System.out.println("public");
    }


    // 类中的属性有两种：实例属性（对象属性、非静态属性）、非实例属性（类属性、静态属性）
    // 相比于对象属性，类属性有static修饰
    // 类属性不会随着对象的改变而改变，是共享的，而对象属性会随着对象的改变而改变
    static String st = "YCC"; // 类属性


    // 类中的方法有两种：实例方法（对象方法、非静态方法）、非实例方法（类方法、静态方法）
    // 相比于对象方法，类方法有static修饰
    // 访问对象方法必须要有对象，而访问类方法不需要
    // 如果一个方法没有用到任何对象属性，则可以设计成类方法
    static void showString(){
        System.out.println(st);
    }

    // 属性初始化
    // 对象属性初始化：
    public String op = "YCC"; // 在声明时初始化
    public ClassAndObject(String op1 , String op2){
        this.op = op1 + op2; // 在构造方法中初始化
    }
    {
        op = "ycc"; // 初始化块
    }

    // 类属性初始化
    public static int old = 100; // 在声明时初始化
    static {
        old = 10000; // 静态初始化块
    }





    public static void main(String[] args) {
        // 引用
        // 引用与指向
        new ClassAndObject(); // 创建一个对象，但没有引用代表(指向)这个对象，无法访问
        ClassAndObject x = new ClassAndObject(); // 使用类变量(即引用)来代表(指向)该类的对象，才能访问这个对象

        // 一个对象可以有多个引用代表(指向)
        ClassAndObject y = x;
        ClassAndObject z = x;
        ClassAndObject w = z;

        // 一个引用只能代表一个对象，但可以改变指向
        x = new ClassAndObject();


        // 继承
        // 子类拥有父类的属性和方法
        x.name = "YCC";
        System.out.println(x.getSpeed());


        // 传入参数可以为类类型变量
        x.printHero(x);


        // 重载方法：方法名相同，参数不同的方法（包括数据类型，数量，顺序）
        x.print(1);
        x.print(1 , 2);
        x.printout();
        x.printout(1 , 2 ,3);


        // 构造方法：实例化对象
        ClassAndObject cl = new ClassAndObject("Hello");
        System.out.println(cl.name);


        // this关键字：在类中代表当前对象
        cl.showAddress(); // this可以指代对象
        cl.setName("YCC"); // this可以访问属性
        cl = new ClassAndObject("YCC" , 0x3f3f3f3); // this可以调用其他构造方法


        // 四种访问修饰符：见类中成员


        // 类属性
        // 访问类属性：推荐使用 类名.类属性
        System.out.println(ClassAndObject.st);
        System.out.println(x.st);
        cl.st = "ycc"; // 类属性可以修改，此时所有其他该类的对象的该属性也会修改
        System.out.println(cl.st);
        System.out.println(x.st);

        // 类方法
        // 访问类方法：推荐使用 类名.类方法
        ClassAndObject.showString();


        // 属性初始化：构造方法具有最终解释权


        // 单例模式(Singleton模式)：一个类在一个JVM中只有一个实例存在.
        // 饿汉式单例模式：无论如何都会创建一个实例
        // 立即加载方式：不论是否用这个对象，都会加载
        // hunger hu = new hunger(); // 无法通过new实例化：构造方法私有化
        hunger h1 = hunger.getItem(); //只能通过内部方法得到对象
        hunger h2 = hunger.getItem();
        System.out.println(h1 == h2); // 因为没有new操作，且类中实例化的为类属性，故两个不同的引用指向一个对象

        // 懒汉式单例模式：只用调用内部方法时才会创建一个实例
        // 延迟加载方式：使用时才会加载
        lazy l1 = lazy.getItem(); //只能通过内部方法得到对象
        lazy l2 = lazy.getItem();
        System.out.println(l1 == l2); // 因为没有new操作，且类中实例化的为类属性，故两个不同的引用指向一个对象


        // 枚举类型：定义常量的类

    }
}
