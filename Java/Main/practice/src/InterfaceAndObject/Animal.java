package InterfaceAndObject;

public abstract class Animal {
    String name;
    protected int legs;

    protected Animal(int legs){
        this.legs = legs;
    }

    public abstract void eat(Animal ...item);

    public void walk(){
        System.out.println("walk by " + legs);
    }
}
