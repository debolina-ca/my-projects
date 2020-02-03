// Write a method removeEvenLength that takes an ArrayList of Strings as a parameter and that removes all of the strings of even length from the list.
import java.util.ArrayList;
import java.util.Scanner;
public class RemoveEvenLength {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        ArrayList<String> list = new ArrayList<String>();
        System.out.println("Enter number of elements: ");
        int numElements = input.nextInt();
        for(int i = 0; i < numElements; i++) {
            list.add(input.nextLine());
        }
        list = removeEvenLength(list);
        System.out.println(list.toString());
    }
    public static ArrayList<String> removeEvenLength(ArrayList<String> list) {
        int len;
        String element;
        int staticSize = list.size();
        for (int i = 0; i < staticSize; i++) {
            element = list.get(i);
            len = element.length();
            if (len%2 == 0) {
                list.remove(i);
                staticSize--;
                i--;
            }
        }
        // System.out.println(list.toString());
        return list;
    }
}
