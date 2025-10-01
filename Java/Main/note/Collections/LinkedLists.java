package Collections;

import java.util.*;

public class LinkedLists {
    public static void main(String[] args) {
        // 链表：LinkedList
        // LinkList实现了List接口
        List<man> linkedList = new LinkedList<>();
        // 操作与ArrayList相同


        // LinkedList实现了Deque接口
        Deque<man> deque = new LinkedList<>();
        LinkedList<man> ll = new LinkedList<>(); // LinkedList本身也为Deque
        // 常见操作：
        // 在末尾插入：addLast(Object)
        ll.addLast(new man("YCC"));

        // 在最前面插入：addFirst(Object)
        ll.addFirst(new man("ycc"));

        // 查看最前面：getFirst()
        System.out.println(ll.getFirst());

        // 查看最后面：getLast()
        System.out.println(ll.getLast());

        // 取出最前面：removeFirst()
        System.out.println(ll.removeFirst());

        // 取出最后面：removeLast()
        System.out.println(ll.removeLast());


        // LinkedList还实现了Queue
        Queue<man> q = new LinkedList<>();

        // 常用方法
        // 在队尾添加：offer(Object)
        q.offer(new man("YCC"));

        // 查看队头：peek()
        System.out.println(q.peek());

        // 取出队头：poll()
        System.out.println(q.poll());
    }
}
