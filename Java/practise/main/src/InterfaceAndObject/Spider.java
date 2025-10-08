package InterfaceAndObject;

public class Spider extends Animal{

    protected Spider(int legs){
        super(legs);
    }

    public void eat(Animal ... item){
        System.out.println("The Spider is eating: ");
        for(Animal each : item) System.out.print(each.name + ' ');
        System.out.println();
    }
}
