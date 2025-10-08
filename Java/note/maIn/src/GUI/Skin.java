package GUI;

public class Skin {
    public static void main(String[] args) {
        // 只需要在最前面加上：
        // javax.swing.UIManager.setLookAndFeel("com.birosoft.liquid.LiquidLookAndFeel")；
        // 就可以把所有组件切换成不同的风格
        try{
            javax.swing.UIManager.setLookAndFeel("com.birosoft.liquid.LiquidLookAndFeel");
        }
        catch (Exception e){
            System.out.println("ERROR");
        }
    }
}
