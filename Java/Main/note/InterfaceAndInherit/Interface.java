package InterfaceAndInherit;
// 接口（Interface）是一种用于定义规范的完全抽象的引用类型，它主要用来规定类应该实现的方法
// 定义格式：public interface 接口名
public interface Interface {
    public void print(); // 只定义方法，而不涉及方法的实现

    default void dePrint(){ // 默认方法(default修饰)，即不实现时默认的具体方法
        System.out.println("default");
    }
}
