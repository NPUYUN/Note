package Collections;

import java.util.*;

class man{
    String name;

    public man(String name){
        this.name = name;
    }

    public String toString(){ // 重写toString，让其返回属性
        return name;
    }
}

public class ArrayLists {
    @SuppressWarnings("rawtypes") // 消除对泛型的警告
    public static void main(String[] args) {
        // 容器：容量随着对象的增加而增长的类
        // 常见容器类：
        // 变长数组：ArrayList
        // 基本用法
        ArrayList men = new ArrayList();
        men.add(new man("YCC")); // 放入对象
        System.out.println(men.size()); // 容器内对象个数

        // 常用方法
        // 增加：add(Object)
        men.add(new man("ZXT"));

        // 在指定位置增加：add(index , Object)
        men.add(2 , new man("lt"));

        // 判断是否存在：contains(Object)，注意：判断标准为是否为同一个对象
        System.out.println(men.contains(new man("YCC")));

        // 获取指定位置的对象：get(index)
        System.out.println(men.get(2)); // 返回的是man类型toString方法的返回值

        // 获取对象所处的位置：indexOf(Object)
        man m = new man("wyb");
        men.add(m);
        System.out.println(men.indexOf(m));

        // 根据下标删除：remove(index)
        men.remove(1);
        System.out.println(men.get(1));

        // 根据对象删除：remove(Object)
        men.remove(m);
        System.out.println(men.contains(m));

        // 替换指定位置的对象：set(index，Object)
        men.set(0 , new man("ycc"));
        System.out.println(men.get(0));

        // 获取大小：size()
        System.out.println(men.size());

        // 转换为数组：toArray(ArrayObject)，默认转换为Object类型的数组，可以传入想要转为的数组
        man[] allMan1 = new man[men.size()];
        men.toArray(allMan1);
        System.out.println(allMan1);
        // 简化版
        man[] allMan2 = (man[])men.toArray(new man[] {});
        System.out.println(allMan2);

        // 并集：addAll(ArrayList)
        ArrayList men2 = new ArrayList();
        men2.add(new man("yummy"));
        men.addAll(men2);
        System.out.println(men);

        // 交集：retainAll(ArrayList)
        // 差集：removeAll(ArrayList)

        // 清空：clear()
        men2.clear();
        System.out.println(men2);

        // 判断是否为空：isEmpty()
        System.out.println(men2.isEmpty());


        // List接口
        // ArrayList实现了List接口，一般会把引用声明为接口List类型
        List list = new ArrayList();


        // 泛型(Generic)初步
        // 不指定泛型的容器可以存放任何类型的元素，而指定泛型的元素只能存放指定类型及其子类的元素
        // 写法：在引用类型和对象类型后加入<类>（后者可以省略）
        List<man> genericMen = new ArrayList<man>();
        List<man> genericMen2 = new ArrayList<>();


        // 遍历
        List<man> mens = new ArrayList<>();
        for(int i = 0 ; i < 5 ; i ++){
                mens.add(new man("man - " + i));
        }
        // for循环遍历
        for(int i = 0 ; i < mens.size() ; i ++){
            System.out.println(mens.get(i));
        }

        // iterator迭代器遍历
        // 迭代器原理：从空开始判断，hasNext判断是否有下一个，如果有则取出来，指针向下移
        Iterator<man> it = mens.iterator(); // 定义迭代器，引用为iterator类型
        while(it.hasNext()){ // 当存在下一个时
            System.out.println(it.next()); // 输出下一个
        }

        // 增强for循环遍历(常用)
        // 弊端：无法进行ArrayList的初始化，无法得知当前为第几个元素
        for(man each : mens){
            System.out.println(each);
        }

    }
}
