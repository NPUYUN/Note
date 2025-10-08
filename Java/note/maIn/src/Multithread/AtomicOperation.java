package Multithread;

import java.util.concurrent.atomic.*; // 原子类

public class AtomicOperation {
    public static void main(String[] args) {
        // 原子操作：不可中断的操作，如赋值操作
        // 原子操作是线程安全的
        // 多个原子操作组合在一起线程不安全，如i ++经历了 取值->计算->赋值 三个原子操作，其中某个操作可能未完成就被其他线程调用导致出现同步问题

        // 原子类：以AtomicInteger为例，其他数据类型类似
        // AtomicInteger提供了线程安全的自增，自减等方法
        AtomicInteger atomicI = new AtomicInteger(8); // 默认值为0，可设初始值
        int i = atomicI.decrementAndGet(); // 自减方法
        int j = atomicI.incrementAndGet(); // 自增方法
        int k = atomicI.addAndGet(3); // 加后赋值
        System.out.println(i + " " + j + " " + k);
    }
}
