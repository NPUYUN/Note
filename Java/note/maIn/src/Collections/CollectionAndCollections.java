package Collections;

import java.util.*;

public class CollectionAndCollections {
    public static void main(String[] args) {
        // Collection是Set、List、Queue、Deque的接口
        // Collection与Map没有关系

        List<Integer> numbers = new ArrayList<>();
        for (int i = 0 ; i < 10 ; i ++){
            numbers.add(i);
        }

        // Collections：容器的工具类，提供一系列类方法
        // 反转：reverse(List)
        Collections.reverse(numbers);
        System.out.println(numbers);

        // 混淆(打乱顺序)：shuffle(List)
        Collections.shuffle(numbers);
        System.out.println(numbers);

        // 排序：sort(List)：默认从小到大
        Collections.sort(numbers);
        System.out.println(numbers);

        // 交换：swap(List , index1 , index2)
        Collections.swap(numbers , 0 , 2);
        System.out.println(numbers);

        // 滚动（将List中的数据向右滚动）：rotate(List , number)
        Collections.rotate(numbers , 2);
        System.out.println(numbers);
    }
}
