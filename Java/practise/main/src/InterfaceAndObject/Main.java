package InterfaceAndObject;

public class Main {
    public static void main(String[] args) {
        Spider spider = new Spider(8);
        Cat cat = new Cat("Jerry");
        Fish fish = new Fish();
        fish.setName("fish");
        cat.eat(fish);
        spider.walk();
    }
}
