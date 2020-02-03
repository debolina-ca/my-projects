// Write Java code to read an integer from the user, then print even if that number is an even number or odd otherwise.
// You may assume that the user types a valid integer.
import java.util.Scanner;
public class evenOdd {
    public static void main (String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Type a number: ");
        int num = input.nextInt();
        if(num%2 == 0) {
            System.out.println("even");
        } else {
            System.out.println("odd");
        }
    }
}