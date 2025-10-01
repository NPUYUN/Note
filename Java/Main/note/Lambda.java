
import InterfaceAndInherit.Abstract;

import java.util.*;
import java.util.function.Supplier;
import java.util.stream.Stream;

class Human{
    String name;
    int age;

    public Human(String name , int age){
        this.name = name;
        this.age = age;
    }

    public String toString(){
        return name + " " + age;
    }

    public boolean match(){
        return this.age >= 18 && this.age <= 50;
    }

    public int get() { return this.age; }
}

interface HumanCheck{
    public boolean check(Human man);
}

public class Lambda {
    public static void filter(List<Human> men){
        for(Human each : men){
            if(each.age <= 50 && each.age >= 18) System.out.println(each);
        }
    }

    public static void filter(List<Human> men , HumanCheck checker){
        for(Human each : men){
            if(checker.check(each)) System.out.println(each);
        }
    }

    public static boolean find(Human man){
        return man.age >= 18 && man.age <= 50;
    }

    public  boolean observe(Human man){
        return man.age >= 18 && man.age <= 50;
    }

    public static List getList(Supplier<List> s){
        return s.get(); // 返回一个List对象
    }

    public static void main(String[] args) {
        // 从普通方法升级到Lambda
        Random r = new Random();
        ArrayList<Human> men = new ArrayList<>();
        for(int i = 0 ; i < 5 ; i ++){
            men.add(new Human("Human" + i , r.nextInt(100)));
        }

        // 普通方法
        filter(men);
        System.out.println();

        // 匿名类
        HumanCheck checker = new HumanCheck() {
            @Override
            public boolean check(Human man) {
                return man.age >= 18 && man.age <= 50;
            }
        };
        filter(men , checker);
        System.out.println();

        // Lambda(匿名方法)
        filter(men , (h)->h.age >= 18 && h.age <= 50);
        System.out.println();

        // Lambda表达式基于匿名类的一般写法：
        // 第一步：将壳子去掉，只保留方法参数和方法体，参数和方法体中画上符号->
        // HumanCheck checker = (Human man) -> {
        //      return man.age >= 18 && man.age <= 50;
        // }

        // 第二步：将return和{}去掉，简化变量
        // HumanCheck checker = (Human h) -> h.age >= 18 && h.age <= 50;

        // 第三步：去掉参数类型和()(当只有一个参数时才能去掉())
        // HumanCheck checker = Human h -> h.age >= 18 && h.age <= 50;

        // 此时将checker的内容 Human h -> h.age >= 18 && h.age <= 50; 即为Lambda表达式


        // 方法的引用
        // 引用静态方法
        // 写法一：完整写法，参数 -> 类.类方法(参数)
        filter(men , h -> Lambda.find(h));

        // 写法二：简化写法，只有类::类方法，无参数
        filter(men , Lambda::find);

        // 引用对象方法
        // 由于不能直接使用对象方法，故Lambda通过对象来使用对象方法
        Lambda l = new Lambda();
        filter(men , h -> l.observe(h)); // 参数 -> 对象.对象方法(参数)
        filter(men , l::observe); // 对象::对象方法

        // 引用容器中的对象方法
        filter(men , Human::match); // 容器和方法正好为同一个类型

        // 引用构造器
        // 有些接口中的方法会返回一个对象
        // 匿名类
        Supplier<List> s = new Supplier<List>() {
            @Override
            public List get() {
                return new ArrayList();
            }
        };
        List list = getList(s);
        // Lambda表达式
        List list1 = getList(() -> new ArrayList());// 表示接收新对象
        // 引用构造器写法
        List list2 = getList(ArrayList::new); // 表示接收新对象


        // 聚合操作
        // Stream：流，一串数据
        // 管道：一系列聚合操作，分为管道源、中间操作、结束操作
        // 每个中间操作返回一个Stream，结束操作返回值或forEach，当什么都不返回时，结束操作才会进行真正的遍历。
        // 遍历的时候会进行中间操作的相关判断
        men
                .stream()
                .filter(h -> h.age >= 18 && h.age <= 50)
                .forEach(h -> System.out.println(h));

        // 管道源
        // 将Collection切换成管道源：stream()
        men.stream();

        // 数组没有stream方法，需要使用Arrays.stream(array)或者Stream.of(array)
        Human[] hu = new Human[10];
        Arrays.stream(hu);
        Stream.of(hu);

        // 中间操作
        // 对元素进行筛选
        // 匹配：filter
        men
                .stream()
                .filter(h -> h.age >= 18 && h.age <= 50)
                .forEach(h->System.out.println(h));

        // 去重（根据equals）：distinct
        men
                .stream()
                .distinct()
                .forEach(h->System.out.println(h));

        // 自然排序：sorted
        men
                .stream()
                .sorted((h1 , h2) -> h1.age >= h2.age ? 1 : -1)
                .forEach(h-> System.out.println(h));

        // 指定排序：sorted(Comparator<T>)
        Comparator<Human> c = new Comparator<Human>() {
            @Override
            public int compare(Human o1, Human o2) {
                if(o1.age > o2.age) return 1;
                else return -1;
            }
        };
        men
                .stream()
                .sorted(c)
                .forEach(h-> System.out.println(h));

        // 保留：limit
        men
                .stream()
                .limit(5) // 保留5个
                .forEach(h-> System.out.println(h));

        // 忽略：skip
        men
                .stream()
                .skip(4) // 忽略前四个
                .forEach(h-> System.out.println(h));

        // 转换为其他形式的流
        // mapTo数据类型：转换为某数据类型的流
        men
                .stream()
                .mapToDouble(Human::get)
                .forEach(h -> System.out.println(h));

        // map：转换为任意Stream
        men
                .stream()
                .map(h -> h.name + '-' + h.age)
                .forEach(h -> System.out.println(h));


        // 结束操作
        // 遍历每一个元素：forEach()
        men
                .stream()
                .filter(h -> h.age >= 18 && h.age <= 50)
                .forEach(h->System.out.println(h));

        // 转换为数组：toArray()（默认为Object类型）
        Object[] al = men
                .stream()
                .filter(h -> h.age >= 18 && h.age <= 50)
                .toArray();

        System.out.println(al.toString());

        // 取最小：min(Comparator<T>) + get()
        Human min = men
                .stream()
                .min(c)
                .get();
        System.out.println(min);

        // 取最大：max(Comparator<T>) + get()
        Human max = men
                .stream()
                .max(c)
                .get();
        System.out.println(max);

        // 总数：count()，默认返回Long
        long cnt = men
                .stream()
                .count();
        System.out.println(cnt);

        // 第一个元素：findFirst() + get()
        Human first = men
                .stream()
                .findFirst()
                .get();
        System.out.println(first);

    }
}
