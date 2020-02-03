import java.util.Scanner;
// Write a method starString that accepts an integer parameter n and returns a string of stars (asterisks) 2n long (i.e., 2 to the nth power).
// You should throw an IllegalArgumentException if passed a value less than 0.
public class RecursiveStarString {
    public static void main (String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter an integer: ");
        int n = input.nextInt();
        System.out.println(starString(n));
    }
    public static String starString (int n) {
        String s = "*";
        if (n < 0) {
            throw new IllegalArgumentException();
        } else if (n == 0) {
            return s;
        } else {
            return starString(n-1) + starString(n-1);
        }
    }
}
