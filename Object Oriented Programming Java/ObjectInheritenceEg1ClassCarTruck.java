public class ObjectInheritenceEg1ClassCarTruck {
    public static void main(String[] args) {
        Car mycar = new Car();
        Truck mytruck = new Truck();
        System.out.println(mycar);
        mycar.m1();
        mycar.m2();
        System.out.println(mytruck);
        mytruck.m1();
        mytruck.m2();
    }
}
