import java.util.ArrayList;
import java.util.Scanner;

public class PracticeArrayList {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        ArrayList<Integer> list = new ArrayList<Integer>();
        System.out.println("Enter number of elements: ");
        int numElements = input.nextInt();
        for(int i = 0; i < numElements; i++) {
            list.add(input.nextInt());
        }
        mystery3(list);
    }
    public static void mystery3(ArrayList<Integer> list) {
        for(int i = list.size() - 2; i > 0; i--) {
            int a = list.get(i);
            int b = list.get(i+1);
            list.set(i, a+b);
        }
        System.out.println(list);
    }
}