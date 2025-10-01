public class NumberAndString {
    public static void main(String[] args) {
        // 封装类
        // 所有基本数据类型都有对应的类类型，称为封装类
        // 封装类有：Byte Short Integer Long Float Double等
        int i = 1;
        // Integer it = new Integer(i); // 已弃用
        Integer it = Integer.valueOf(i); // 基本类型转封装类
        int i2 = it.intValue(); // 封装类转基本类型

        // Number类：所有整型、浮点型封装类的抽象父类
        System.out.println(it instanceof Number);

        // 自动装箱：通过 = 自动把基本类型转换为类类型(封装类类型)
        Integer it2 = i;

        // 自动拆箱：通过 = 自动把类类型(封装类类型)转换为基本数据类型
        int i3 = it;

        // 基本数据类型的最值：最大值：封装类类型.MAX_VALUE，最小值：封装类类型.MIN_VALUE
        System.out.println(Integer.MAX_VALUE);
        System.out.println(Integer.MIN_VALUE);


        // 字符串转换
        // 数字转字符串
        // 方法一：使用String类的静态方法valueOf
        String str1 = String.valueOf(i);

        // 方法二：先把基本数据类型装箱成对象，然后调用对象的toString方法
        Integer it3 = i;
        String str2 = it3.toString();

        // 字符串转数字
        // 调用封装类的静态方法parse..
        int i4 = Integer.parseInt(str1);


        // 数学方法：Math提供了一些常用的数学运算方法，都以静态的形式存在
        // 四舍五入：Math.round()
        System.out.println(Math.round(4.4));
        System.out.println(Math.round(4.5));

        // 随机数：Math.random()（默认为0~1的浮点数，取不到1）
        System.out.println(Math.random());
        System.out.println((int)(Math.random() * 10)); // 转换成整型1~10，取不到10

        // 开方：Math.sqrt()
        System.out.println(Math.sqrt(9));

        // 次方：Math.pow()
        System.out.println(Math.pow(2 , 4));

        // 圆周率： Math.PI
        System.out.println(Math.PI);

        // 自然常数：Math.E
        System.out.println(Math.E);


        // 格式化输出(printf)：类似python的格式化字符串，需要用到printf/format输出
        String ch1 = "I";
        String ch2 = "you";
        String sentence = "%s love %s %n"; // %n：所有操作系统一致的换行符
        System.out.printf(sentence,ch1,ch2);
        System.out.format(sentence,ch2,ch1);
        // 其他格式化方式：小数位数，对齐等：与C++的printf一致


        // 字符：char
        // char对应的封装类为Character
        char c1 = 'a';
        Character c = c1; // 自动装箱
        c1 = c; // 自动拆箱

        // Character有如下静态方法
        // 判断是否为字母：isLetter()
        System.out.println(Character.isLetter(c1));

        // 判断是否为数字：isDigit()
        System.out.println(Character.isDigit(c1));

        // 判断是否为空白：isWhitespace()
        System.out.println(Character.isWhitespace(c1));

        // 判断是否为大写：isUpperCase()
        System.out.println(Character.isUpperCase(c1));

        // 判断是否为小写：isLowerCase()
        System.out.println(Character.isLowerCase(c1));

        // 转换为大写：toUpperCase()
        System.out.println(Character.toUpperCase(c1));

        // 转换为小写：toLowerCase()
        System.out.println(Character.toLowerCase(c1));

        // 转换为字符串：toString()
        String cs = Character.toString(c1);

        // 转义字符：和C++相同


        // 字符串
        // 字符串的创建
        // 方式一：字面值
        String string1 = "你好";

        // 方式二：调用String构造方法创建一个字符串对象
        // 可以直接输入字符串
        String string2 = new String("FUCK");
        // 也可以通过字符数组来创建
        char[] cs2 = {'1' , '2'};
        String string3 = new String(cs2);

        // String被修饰成final，不能被继承
        // String对象一但创建后不可改变

        // 字符串长度：length方法
        System.out.println(string1.length());

        // 字符串操作：
        // 获取指定位置的字符：chatAt(int index)
        System.out.println(string2.charAt(0));

        // 获取对应的字符数组：toChatArray()
        char[] cstring = string2.toCharArray();
        for(char each : cstring) System.out.println(each);

        // 截取子字符串：sybString(int beginning , int ending) 没有ending则截取到末尾
        System.out.println(string2.substring(1));
        System.out.println(string2.substring(1 , 3));

        // 分隔：split(分割字符串)，分割字符串会被删去
        String sentences = " I , love , you ";
        String[] subSentences = sentences.split(",");
        for(String each : subSentences) System.out.println(each);

        // 去掉首尾空格：trim()
        System.out.println(sentences.trim());

        // 全变为大写：toUpperCase()
        System.out.println(sentences.toUpperCase());

        // 全变为小写：toLowerCase()
        System.out.println(sentences.toLowerCase());

        // 定位：indexOf(字符/字符串)
        System.out.println(sentences.indexOf("I"));

        // 判断是否包含：contains(字符/字符串)
        System.out.println(sentences.contains("love"));

        // 替换所有的：replaceAll(待替换子串，替换字符串)
        System.out.println(sentences.replaceAll("you" , "I"));

        // 替换第一个：replaceFirst(待替换子串，替换字符串)
        System.out.println(sentences.replaceFirst("I" , "you"));


        // 比较字符串
        // 是否为同一个对象：==
        String s1 = "1";
        String s2 = new String(s1);
        System.out.println(s1 == s2);
        // 注意：当两个字符串的字面值相同且均用字面值初始化时，二者指向同一个对象
        String s3 = "the light";
        String s4 = "the light";
        System.out.println(s3 == s4);

        // 判断内容是否相同
        // 一般比较：equals(String)
        System.out.println(s1.equals(s2));

        // 忽略大小写比较:equalsIgnoreCase(String)
        System.out.println(s3.equalsIgnoreCase(s4));

        // 判断是否以子串开始或者结束
        // 以...开始：startsWith(String)
        System.out.println(s3.startsWith("the"));

        // 以...结束：endsWith(String)
        System.out.println(s3.endsWith("light"));


        // 可变长字符串：StringBuffer
        // 创建StringBuffer对象
        String st1 = "I love you";
        StringBuffer sb = new StringBuffer(st1); // 传入字符串

        // 变长字符串操作
        // 追加：append(String)
        sb.append("!!!");
        System.out.println(sb);

        // 删除：delete(beginning , ending)，左闭右开
        sb.delete(10 , 14);
        System.out.println(sb);

        // 插入：insert(index , String)
        sb.insert(2 , "really ");
        System.out.println(sb);

        // 反转：reverse()
        sb.reverse();
        System.out.println(sb);

        // 长度和容量：
        // 与C++容器类似，长度为实际长度，容量为系统分配的字符数组长度
        // 当长度大于容量时，系统会自动创建一个大小为原来两倍的字符数组（倍增），然后讲原来的字符数组复制到其中
        // length：显示长度
        System.out.println(sb.length());

        // capacity：显示容量
        System.out.println(sb.capacity());

        // 倍增
        sb.append(sb);
        System.out.println(sb.capacity());

        // StringBuffer与String的性能区别
        System.out.println(System.currentTimeMillis()); // 获取当前时间（ms）
        String string = "";
        for(int k = 0 ; k < 10000 ; k ++) string += sb;

        System.out.println(System.currentTimeMillis());
        StringBuffer sb2 = new StringBuffer(); // 可以不加字符串参数，默认为空字符
        for(int k = 0 ; k < 10000 ; k ++) sb2.append(sb);
        System.out.println(System.currentTimeMillis());
        // 显然StringBuffer效率更高
    }
}
