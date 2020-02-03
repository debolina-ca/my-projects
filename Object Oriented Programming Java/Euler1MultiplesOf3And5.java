import java.util.ArrayList;

// Multiples of 3 and 5
// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
// The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
public class Euler1MultiplesOf3And5 {
    public static void main(String[] args){
        int sum = 0;
        ArrayList<Integer> list = new ArrayList<>();
        for(int i = 1; i<1000; i++){
            if(i%3 == 0 || i%5 == 0){
                list.add(i);
            }
        }
        System.out.println(list);
        for(int i = 0; i<list.size(); i++){
            sum = sum + list.get(i);
        }
        System.out.println("Sum is: "+sum);
    }
}
