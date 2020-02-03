/* Write a method called inputBirthday that accepts a Scanner for the console as a parameter and prompts the user to enter
a month, day, and year of birth, then prints the birthdate in a suitable format. */

import java.util.Scanner;
public class Date_of_birth_withscanner {
    public static void main (String[] args) {
        inputBirthday();
    }
    public static void inputBirthday() {
        Scanner input = new Scanner(System.in);
        System.out.print("On what day of the month were you born? ");
        String day = input.next();
        System.out.print("What is the name of the month in which you were born? ");
        String month = input.next();
        System.out.print("During what year were you born? ");
        String year = input.next();
        System.out.println("You were born on " + month + " " + day + ", " + year + ". You're mighty old!");
    }
}
