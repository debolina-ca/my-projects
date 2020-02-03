import java.util.Scanner;

public class PracticeRecursiveAlgorithm {
    /*
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter an integer: ");
        int n = input.nextInt();
        print(n);
    }
    public static void print(int n) {
        if (n == 1) {
            System.out.print("< bc >");
        } else {
            System.out.print("p(" + n + ") -> ");
            print(n-1);
        }
    }
    */
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter an integer: ");
        int n = input.nextInt();
        mystery1(n);
    }
    public static void mystery1(int n) {
        if (n <= 1) {
            System.out.print(n);
        } else {
            mystery1(n / 2);
            System.out.print(", " + n);
        }
    }
}


