import java.util.ArrayList;
import java.util.Scanner;

public class ArrayListMystery2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        ArrayList<Integer> list = new ArrayList<Integer>();
        System.out.println("Enter number of elements: ");
        int numElements = input.nextInt();
        for(int i = 0; i < numElements; i++) {
            list.add(input.nextInt());
        }
        mystery2(list);
    }
    public static void mystery2(ArrayList<Integer> list) {
        for (int i = list.size()-1; i >= 0; i--) {
            if(i%2 == 0) {
                list.add(list.get(i));
            } else {
                list.add(0, list.get(i));
            }
        }
        System.out.println(list);
    }
}
