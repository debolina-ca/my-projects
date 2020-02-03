import java.util.*;             // Random must be imported, but it is part of the same "package" as Scanner so just import java.util.*
// import java.util.Scanner;

public class OddsAndEvens {
    public static void main(String[] args) {
        // Part 1 - Pick odds or evens
        Scanner input = new Scanner(System.in);
        System.out.println("Let’s play a game called “Odds and Evens”");
        System.out.print("What is your name? ");
        String name = input.nextLine();
        System.out.print("Hi " + name + ", which do you choose? (O)dds or (E)vens? ");
        String choice = input.next();
        if (choice.equals("O")) {
            System.out.println(name + " has picked odds! The computer will be evens.");
        } else if (choice.equals("E")) {
            System.out.println(name + " has picked evens! The computer will be odds.");
        } else {
            System.out.println("You have entered an invalid choice. ");
        }
        System.out.println("-------------------------------------------------\n");

        // Part 2 - Play the Game
        System.out.print("How many “fingers” do you put out? ");
        int userNumber = input.nextInt();
        Random rand = new Random();
        int computerNumber = rand.nextInt(6);                     //let the computer choose a random number to represent their fingers
        System.out.println("The computer plays " + computerNumber + " \"fingers\".");
        System.out.println("-------------------------------------------------\n");
        int sum = userNumber + computerNumber;
        System.out.println(userNumber + " + " + computerNumber + " = " + sum);
        boolean oddOrEven;
        if (sum%2 == 0) {
            oddOrEven = true;                               // oddOrEven will be true if sum us even, it will be false if sum is odd
            System.out.println(sum + " is ...even!");
        } else {
            oddOrEven = false;
            System.out.println(sum + " is ...odd!");
        }
        System.out.println("-------------------------------------------------\n");

        // Part 3 - Who won?
        if (((oddOrEven == true) && (choice.equals("E"))) || ((oddOrEven == false) && (choice.equals("O"))))  {
            System.out.println("That means " + name + " wins! :) ");
        } else {
            System.out.println("The computer  wins! ");
        }
        System.out.println("-------------------------------------------------\n");
    }
}
