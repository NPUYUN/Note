//类名为大驼峰命名法，属性名和方法名为小驼峰命名法
class Hero{ //创建类，除了主程序所在的类其他类一概不能用public修饰
    // 以下为属性
    String name;
    float hp;
    float armor;
    int moveSpeed;

    //以下为方法
    float getSpeed(){
        return moveSpeed;
    }

    void fuck(){
        System.out.println("Fuck You");
    }

    void addSpeed(int speed){
        moveSpeed += speed;
    }
}

public class ClassCreate {
    public static void main(String[] args) {
        Hero man = new Hero(); //创建对象
        // 以下为给对象属性赋值
        man.name = "YCC";
        man.hp = 100;
        man.armor = 1000;
        man.moveSpeed = 20;
        man.fuck();
        man.addSpeed(20);
        System.out.println(man.getSpeed());
    }
}
