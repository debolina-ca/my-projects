import java.util.Scanner;
// Write a recursive method repeat that accepts a string s and an integer n as parameters and that returns a String consisting of n copies of s.
public class RepeatRecursiveAlgorithm {
    public static void main (String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String s = input.nextLine();
        System.out.print("Enter an integer: ");
        int n = input.nextInt();
        System.out.println(repeat(s, n));
    }
    public static String repeat (String s, int n) {
        if (n < 0) {
            throw new IllegalArgumentException();
        } else if (n==0) {
            return "";
        } else if (n==1) {
            return s;
        } else {
            return s + repeat(s, (n-1));
        }
    }
}
