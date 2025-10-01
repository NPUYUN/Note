package InterfaceAndObject;

public class Cat extends Animal implements Pet{
    String name;

    public Cat(String name){
        super(4);
        this.name = name;
    }

    public Cat(){
        this("");
    }

    public String getName(){
        return name;
    }

    public void setName(String name){
        this.name = name;
    }

    public void Play(){
        System.out.println("The Cat is playing");
    }

    public void eat(Animal ...item){
        System.out.println("The cat is eating: ");
        for(Animal each : item) System.out.print(each.name);
        System.out.println();
    }
}
