public class Variable {
    public static void main(String[] args) {
        // 变量的数据类型
        // 整型
        byte a = 1; // 8位 -128 ~ 127
        short b = 2; // 16位
        int c = 3; // 32位
        long d = 4L; // 64位 用L结尾
        // 16进制在数字前面加上 0x
        // 8进制在数字前面加上：0
        // 2进制在数字前面加上：0b

        // 字符型
        char ch = 'c'; // 16位 只存放一个字符 用单引号

        // 浮点型
        float fl = 1.0f; // 32位 末尾要加 f 表示类型转换
        double dl = 1.0; // 64位 浮点型默认为double类型
        // 可以用科学计数法表示（e）

        // 布尔型
        boolean bl = true; // 1位 只有false（0）和true（1）两种值

        // 类型的转换等内容与C++相同
        // 整数运算答案默认为其中容量最大的类型（< int 则为int）

        // String类型
        // String类型不是基本数据类型，但被广泛使用
        String name = "YCC"; // 存放多个字符 用双引号

        // 作用域内容与C++相同，注意就近原则

        // final修饰符
        final int fi = 10; // final修饰的变量只能被赋值一次
        final double fd;
        fd = 1.0;
        // final修饰其他（方法，类）也是如此

    }
}
