import java.util.Scanner;

public class ConditionControl {
    public static void main(String[] args) {
        // java的条件控制语句和C++语法一致，不同点如下：

        // switch支持String类型：将String类型Hash后当作整型使用
        Scanner s = new Scanner(System.in);

        String str = s.next();
        switch(str){
            case "春":
                System.out.println("满园春色关不住");
                break;
            case "夏":
                System.out.println("小荷才露尖尖角");
                break;
            case "秋":
                System.out.println("我言秋日胜春朝");
                break;
            case "冬":
                System.out.println("独钓寒江雪");
                break;
            default:
                System.out.println("FUCK YOU");
        }

        // 结束外部循环除了可以用bool类型的外部变量来控制，还可以用标签来控制
        outlook: //定义标签，为任意合法的变量名，注意末尾为冒号:
        for (int i = 1 ; i < 10 ; i ++){
            for (int j = 1 ; j < 10 ; j ++){
                System.out.println(i * j);
                if(j % 2 == 0)
                    break outlook; // 直接结束外部循环
            }
        }
    }
}
