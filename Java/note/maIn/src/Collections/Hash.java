package Collections;

import java.util.*;

public class Hash {
    public static void main(String[] args) {
        // HashMap与HashSet
        // HashMap(哈希表)：以键值对形式存储数据，键不能重复，值可以重复
        // Hashtable也实现了Map类，不能存放null，但是线性安全
        // HashMap实现了Map接口
        Map<String , String> dic = new HashMap<>();
        Map<String , String> dic_t = new Hashtable<>();

        // 常见操作
        // 添加键值对：put(Key , Value)
        dic.put("1" , "I");
        dic_t.put("1" , "I");

        // 查找键对应的值：get(Key)或者get(index)
        System.out.println(dic.get("1"));
        System.out.println(dic_t.get("1"));

        // 删除：remove(Key)
        dic.remove("1");
        dic_t.remove("1");

        // 返回大小：size()
        System.out.println(dic.size());
        System.out.println(dic_t.size());

        // 清空：clear()
        dic.clear();
        dic_t.clear();

        // 判断是否为空
        System.out.println(dic.isEmpty());
        System.out.println(dic_t.isEmpty());


        // HashSet(无序集合)：元素不能重复且没有顺序
        // HashSet实现了Set接口
        // LinkedHashSet和TreeSet也实现了Set接口，区别在于：
        // LinkedHashSet中元素的顺序为按照插入顺序
        // TreeSet中元素顺序为从小到大
        Set<String> set = new HashSet<>();
        Set<String> set2 = new LinkedHashSet<>();
        Set<String> set3 = new TreeSet<>();
        // 常见操作：与ArrayList一致，HashSet没有索引功能（没有含有索引的方法）

        // 遍历：由于HashSet没有元素没有顺序，无法通过get获取指定位置的元素，故只有两种方式遍历
        // 其他两种均可进行三种遍历方式，此处略
        for (int i = 0 ; i < 10 ; i ++){
            set.add("number" + i);
        }
        // 迭代器遍历：
        for(Iterator<String> iterator = set.iterator() ; iterator.hasNext();){
            System.out.println(iterator.next());
        }
        System.out.println();

        // 增强for循环：
        for(String str : set){
            System.out.println(str);
        }

        // HashSet和HashMap的关系：HashSet是作为HashMap的key而存在的
        // Java中哈希表的实现一般为链地址法
        // Java中字符的哈希值为(s[0]+ s[1] + s[2] + s[3]+ ... +  s[n-1])*23.
    }
}
