import java.util.ArrayList;
import java.util.Scanner;

// Write a method maxLength that takes an ArrayList of Strings as a parameter and that returns the length of the longest string in the list.
// If your method is passed an empty list, it should return 0.
public class MaxLength {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        ArrayList<String> list = new ArrayList<String>();
        System.out.println("Enter number of elements: ");
        int numElements = input.nextInt();
        for(int i = 0; i < numElements; i++) {
            list.add(input.next());
        }
        System.out.println(maxLength(list));
    }
    public static int maxLength(ArrayList<String> list) {
        String element;
        int len = 0;
        int longestLength = 0;
        for(int i = 0; i < list.size(); i++) {
            element = list.get(i);
            len = element.length();
            if (longestLength < len) {
                longestLength = len;
            }
        }
        return longestLength;
    }
}
