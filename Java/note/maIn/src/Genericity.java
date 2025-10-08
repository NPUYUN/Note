import java.util.*;

// 不支持泛型的类，内部的泛型只能为一种类型
class Man1{
    LinkedList<String> list = new LinkedList<>();
}

// 支持泛型的类，内部的类型可以写成 T，表示与类的泛型一致，为任意泛型
class Man2<T>{
    LinkedList<T> list = new LinkedList<>();
    public T info; // 泛型属性
    public T Op(){ // 泛型方法
        return (T)info;
    }
}

class Father{
    String name;

    public Father(String name){
        this.name = name;
    }

    public String toString(){
        return name;
    }
}

class Son1 extends Father{
    public Son1(String name){
        super(name);
    }
}

class Son2 extends Father{
    public Son2(String name){
        super(name);
    }
}

public class Genericity {
    public static void main(String[] args) {
        // 集合中的泛型详见Collections
        // 不支持泛型的类：内部泛型只能为固定属性
        Man1 man1 = new Man1();
        man1.list.add("FUCK");

        // 支持泛型的类：在类的声明上加一个<T>，表示该类支持泛型
        // 支持泛型的类中，<T>的泛型表示与类的泛型一致,可以为任意泛型
        Man2<String> man2 = new Man2<>(); // 声明类的泛型为String
        Man2<Integer> man3 = new Man2<>(); // 声明类的泛型为Integer
        man2.list.add("YOU");
        man3.list.add(1);


        // 通配符：？
        // ? extends 类：表示这是一个该类的泛型或者该类子类的泛型
        // 取出来的元素一定可以转型为类
        // 不能往里面放元素
        ArrayList<Father> f = new ArrayList<>();
        ArrayList<Son1> s1 = new ArrayList<>();
        ArrayList<Son2> s2 = new ArrayList<>();
        f.add(new Father("YCC"));
        s1.add(new Son1("ZXT"));
        s2.add(new Son2("LT"));
        ArrayList<? extends Father> ff = f;
        ArrayList<? extends Father> fs1 = s1;
        ArrayList<? extends Father> fs2 = s2;
        Father fa1 = ff.get(0);
        Father fa2 = fs1.get(0);
        Father fa3 = fs2.get(0);
        // ff.add(new Father("ycc"));

        // ? super 类：表示这是一个该类的泛型或者该类父类的泛型
        // 可以往里面放该类以及该类的子类
        // 取出来有风险，默认为Object类，不能直接转换成原类型（需要强制转换）
        ArrayList<? super Father> sf = new ArrayList<>();
        sf.add(new Father("YCC"));
        sf.add(new Son1("ZXT"));
        sf.add(new Son2("LT"));
        Father fa = (Father) sf.get(0); // 需强制转换
        System.out.println(fa);

        // ?：任意泛型
        // 只能以Object的形式取出来
        // 不能往里面放元素
        ArrayList<?> nf = sf;
        fa = (Father) nf.get(0);
        System.out.println(fa);

        // 子类泛型和父类泛型之间不能转型
    }
}
