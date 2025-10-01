import java.text.ParseException; // 导入parse所在的处理异常类
import java.util.Date; // 导入Date类
import java.util.Calendar; // 导入Calendar类
import java.text.SimpleDateFormat; //导入SimpleDateFormat类

public class DateObject {
    public static void main(String[] args) throws ParseException {
        // 时间原点
        // java的时间原点为1970/1/1/8/0/0，在计算机中表示为0
        // 所有日期都以时间原点为基准，每过一毫秒，数字+1

        // 创建日期对象
        Date d1 = new Date(); // 不带参数：默认为当前时间
        System.out.println(d1);

        Date d2 = new Date(5000); // 带参数：从时间原点开始计算，+参数个ms
        System.out.println(d2);

        // getTime方法：返回long型整数，代表从时间原点到该时间的毫秒数
        System.out.println(d1.getTime());

        // System.currentTimeMills方法：返回当前时间到时间原点的毫秒数
        System.out.println(System.currentTimeMillis());


        // 日期格式化：SimpleDateFormat类
        // 日期转字符串：
        // y代表年，M代表月，d代表日，H代表24进制的小时，h代表12进制的小时，m代表分钟，s代表秒，S代表毫秒
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss SSS"); // 传入想要的格式
        String str = sdf.format(d1); // 将日期格式化成字符串(format方法)
        System.out.println(str);

        // 字符串转日期：parse方法（需要ParseException类）
        Date d3 = sdf.parse(str); // str的格式需要和sdf完全一致
        System.out.println(d3);


        // 日历：Calendar类
        // 日历与日期的转换
        // 采取单例模式获取日历对象Calendar.getInstance()
        Calendar c = Calendar.getInstance();

        // 通过日历对象得到日期对象：getTime()
        Date d = c.getTime();
        System.out.println(d);

        // 将日历转换为日期：setTime()
        Date dd = new Date();
        c.setTime(dd);
        System.out.println(c);

        // 翻日历
        // add(Calendar.YEAR/MONTH/DATE , amount)：在原日期上增加年/月/日
        c.add(Calendar.MONTH , 1);
        System.out.println(sdf.format(c.getTime()));
        c.add(Calendar.YEAR , -1); // 反向增加则为减少
        System.out.println(sdf.format(c.getTime()));

        // set(Calendar.YEAR/MONTH/DATE , number)：直接设置年/月/日
        c.set(Calendar.YEAR , 2024);
        System.out.println(sdf.format(c.getTime()));
    }
}
