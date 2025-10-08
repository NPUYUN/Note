import java.util.Scanner; // 使用Scanner需要先导入Scanner类

public class Operator {
    public static void main(String[] args) {
        // java的算数操作符、关系操作符、三元操作符、赋值操作符与C++一致，不再赘述。其他类型的操作符雷同，只展示相异的部分
        // 逻辑操作符
        int i = 0;
        System.out.println(i == 1 && i ++ < 2);
        System.out.println(i); // && 为短路与，第一个为false则不会运行第二个

        System.out.println(i == 1 & i ++ < 2);
        System.out.println(i); // & 为长路与， 两边必定会运行

        // | 与 || 同理，其他的与C++相同

        // 位操作符
        System.out.println(Integer.toBinaryString(i));// 返回某个数的二进制形式

        // 带符号移位与不带符号移位
        System.out.println(-20 >> 2); // 不带符号：>> << ，即移动不改变符号位
        System.out.println(-20 >>> 2);// 带符号: >>> <<<， 即符号位随之改变


        // 操作符Scanner：接收从控制台的输入(与C++的scanf相似)
        Scanner s = new Scanner(System.in); // 创建Scanner对象

        // 读取整数
        int a = s.nextInt();
        System.out.println("The First int : " + a);
        int b = s.nextInt();
        System.out.println("The Second int : " + b);

        // 读取浮点数
        float f = s.nextFloat();
        System.out.println("The Float : " + f);

        // 读取字符串
        String rn = s.nextLine(); // nextLine()会读入回车，要先清空缓冲区的回车
        String str = s.nextLine();
        System.out.println("The String : " + str);

        str = s.next(); //若使用next()方法，则会过滤掉回车、空格等空白字符
        System.out.println("The String : " + str);

        // Scanner的作用和scanf相同，但需要事先创建Scanner对象，并针对不同的数据类型使用不同的方法读取
    }
}
