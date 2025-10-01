package InterfaceAndObject;

public class Fish extends Animal implements Pet{
    private String name;

    public Fish(){
        super(0);
    }

    public void walt(){
        System.out.println("Fish can not walk");
    }

    public String getName(){
        return name;
    }

    public void setName(String name){
        this.name = name;
    }

    public void Play(){
        System.out.println("The fish is playing");
    }

    public void eat(Animal ... item){
        System.out.println("The fish is eating: ");
        for(Animal each : item) System.out.print(each.name);
        System.out.println();
    }
}
