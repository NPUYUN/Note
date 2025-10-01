package Collections;

import java.util.Collections;
import java.util.ArrayList;
import java.util.Random;
import java.util.List;
import java.util.Comparator;
import java.util.TreeSet;
import java.util.Set;

class Man implements Comparable<Man>{ // 实现Comparable<数据类型>接口
    String name;
    int old;

    public Man(String name , int old){
        this.name = name;
        this.old = old;
    }

    public String toString(){ // 重写toString以规定直接输出对象的结果
        return name + " " + old;
    }

    @Override
    public int compareTo(Man another){ // 参数类型和泛型一致
        if(old > another.old){
            return 1; // 返回正数代表this会排在another后面
        }
        else if(old == another.old){
            return 0; // 返回0代表二者相对位置不变
        }
        else{
            return -1; // 返回负数代表this会排在another前面
        }
    }
}

public class Comparision {
    public static void main(String[] args) {
        // 比较器：定义比较的逻辑
        Random r = new Random(); // 创建随机数对象（详情请见Random模块）
        List<Man> men = new ArrayList<>();
        for (int i = 0 ; i < 10 ; i ++){
            men.add(new Man("man-" + i , r.nextInt(100)));
        }
        // 由于man有两种属性，一个为String，一个为int，无法用sort排序
        // Collections.sort(men);

        // 方法一：Comparator指定比较算法，与C++里的自定义比较函数类似
        Comparator<Man> c = new Comparator<Man>() {
            @Override
            public int compare(Man o1, Man o2) {
                // 按照年龄大小排序
                if(o1.old > o2.old){
                    return 1; // 返回正数代表o1会排在o2后面
                }
                else if(o1.old == o2.old){
                    return 0; // 返回0代表二者相对位置不变
                }
                else{
                    return -1; // 返回负数代表o1会排在o2前面
                }
            }
        };

        Collections.sort(men , c); // 将比较对象传入sort以执行比较器逻辑（与C++相同）
        System.out.println(men);
        // 注：TreeSet的构造方法默认支持传入一个Comparator，此时内部顺序依照比较强逻辑
        Set<Man> treeSet = new TreeSet<>(c);


        // 方法二：需要比较的类实现Comparable接口，无需传入比较对象即可比较
        Collections.sort(men);
        System.out.println(men);
    }
}
