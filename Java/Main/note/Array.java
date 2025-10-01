// java 的数组与 C++ 差异较大
import java.util.Arrays; // 使用Arrays工具类需先导入

public class Array {
    public static void main(String[] args) {
        // 声明数组：数据类型[] 变量名 或者 数据类型 变量名[] , 推荐使用前者
        int a[];
        double[] b; // 推荐使用

        // 创建数组：new 数据类型[长度]，表示分配空间
        a = new int[3]; // a为长度为3的整型数组
        b = new double[4]; // b为长度为4的浮点型数组
        char[] c = new char[5]; // 声明和创建可以写在一个语句中

        // 访问数组：和C++一致的下标访问

        // 数组长度：数组具有length属性
        System.out.println(a.length);
        System.out.println(b.length);
        System.out.println(c.length);

        // 数组的直接赋值
        // 没有赋值则会用默认值，如int默认为0
        System.out.println(a[0]);
        // 分配空间的同时赋值
        int[] d = new int[]{1 , 2 , 3}; // 赋值后就不能设置长度了
        int[] e = {1 , 2 , 3}; //new 数据类型[] 可以省略

        // 增强型for循环：只用来取值，不能修改里面的值
        // for(数据类型 变量名 ：数组名)，表示用变量依次指代数组里的每个数（类似python的容器遍历）
        for(int each : d){
            System.out.println(each);
        }

        // 复制数组
        // System.arraycopy(原数组，从原数组复制的起始位置，目标数组，复制到目标数组的起始位置，复制的长度)
        int[] a1 = new int[]{1 , 2 , 3 , 4, 5};
        int[] a2 = new int[3];
        System.arraycopy(a1 , 0 , a2 , 0 , 3); // 复制a2到a1
        for(int item : a2) System.out.println(item);

        // 二维数组
        // 初始化二维数组: 数据类型[][] 变量名 = new 数据类型[行数][列数]
        int[][] da = new int[2][3];
        int[][] db = new int[2][]; // 二维数组的第一维必须确定，空间必须分配，第二维可以先不确定
        db[0] = new int[3]; // 访问前需要明确第二维的长度
        int[][] dc = new int[][]{{1 , 2 , 3} , {4 , 5 , 6} , {7}}; //直接赋值，每一维的长度可以不统一
        int[][] dd = {{1 , 2 , 3 ,4 ,5 } , {6 , 7 ,8}}; // 简化写法

// --------------------------------------------------------------------------------
        // Arrays：针对数组的工具类
        // 数组复制：copyOfRange(原数组，复制开始位置，复制结束位置) 遵循左闭右开
        int[] t1 = {8 , 2 , 3, 4};
        int[] t2 = Arrays.copyOfRange(t1 , 0 , 4);
        for(int i : t2) System.out.println(i);

        // 转换为字符串：toString(数组) 将数组转化为字符串
        String content = Arrays.toString(t1);
        System.out.println(content);

        // 排序：sort(数组) 将数组从小到大排序
        Arrays.sort(t1);
        System.out.println(Arrays.toString(t1));

        // 搜索（基于排好序的数组）：binarySearch(数组，查找元素) 返回元素位置
        System.out.println(Arrays.binarySearch(t1 , 8));

        // 判同：equals(数组1，数组2) 比较两个数组，若数组1和2相同（包括顺序），则返回true，否则返回false
        System.out.println(Arrays.equals(t1 , t2));

        // 填充：fill(数组，填充数据）将数组中全部空间填充维填充数据
        Arrays.fill(t2 , 1);
        System.out.println(Arrays.toString(t2));

// ----------------------------------------------------------------------------------
        // 实例：找到数组最小数
        // 随机数生成方法：Math.random()：会生成0~1之间的随机数
        int[][] array = new int[5][5];
        int x = 0 , y = 0;
        int min = 0x3f3f3f3f;
        for(int i = 0 ; i < 5 ; i ++){
            for (int j = 0 ; j < 5 ; j ++){
                array[i][j] = (int)(Math.random() * 100);
                if(min > array[i][j]){
                    min = array[i][j];
                    x = i;
                    y = j;
                }
            }
        }
        System.out.println("min is array[" + x + "][" + y + "] = " + min);

    }
}
