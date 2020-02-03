 // Part 2 – FractionCalculator Class
// In this section, you will implement a FractionCalculator class that has a main method and three helper methods.
// The FractionCalculator class is a client class that will allow the user to enter in fractions and operations, calculating and displaying the result.

import java.util.Scanner;

public class FractionCalculator {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Fraction result = new Fraction();
        boolean isFracEqual = false;
        System.out.println("This program is a fraction calculator");
        System.out.println("It will add, subtract, multiply and divide fractions until you type Q to quit.");
        System.out.println("Please enter your fractions in the form a/b, where a and b are integers.");
        System.out.println("-----------------------------------------------------------------------------------------");
        System.out.print("Please enter an operation (+, -, /, *, = or Q to quit): ");
        String operator = getOperation(input);
        while (!operator.equals("Q") && !operator.equals("q")) {
            Fraction fraction1 = getFraction(input);
            Fraction fraction2 = getFraction(input);
            switch (operator) {
                case "+":
                    result = fraction1.add(fraction2);
                    break;
                case "-":
                    result = fraction1.subtract(fraction2);
                    break;
                case "*":
                    result = fraction1.multiply(fraction2);
                    break;
                case "/":
                    result = fraction1.divide(fraction2);
                    break;
                case "=":
                    isFracEqual = fraction1.equals(fraction2);
                    break;
                default:
                    System.exit(1);
                    break;
            }
            if (operator.equals("=")) {
                if (isFracEqual == true) {
                    System.out.println(fraction1.toString() + " " + operator + " " + fraction2.toString() + " is true.");
                } else {
                    System.out.println(fraction1.toString() + " " + operator + " " + fraction2.toString() + " is false.");
                }
            } else {
                System.out.println(fraction1.toString()+" "+operator+" "+fraction2.toString()+" = "+result.toString());
            }
            System.out.println("--------------------------------------------------------------------------------------------");
            operator = getOperation(input);
        }
    }
    // This function prompts the user to enter its choice of operator and validates the same for correctness
    // else prompts the user to enter the correct operator until the correct choice is chosen.
    public static String getOperation(Scanner input) {
        String operator = input.next();
        while (!operator.equals("+") && !operator.equals("-") && !operator.equals("*") && !operator.equals("/") && !operator.equals("=") && !operator.equals("Q") && !operator.equals("q")) {
            System.out.print("Invalid input (+, -, /, *, = or Q to quit): ");
            operator = input.next();
        }
        return operator;
    }
    // This is used to validate the fraction entered by the user.
    public static boolean validFraction(String fraction) {
        if (fraction.indexOf('-') != 0 && fraction.indexOf('-') != -1) {
            return false;
        }
        if (fraction.indexOf('/') == -1) {
            if (isNumber(fraction)) {
                return true;
            } else {
                return false;
            }
        }
        String[] substrings = fraction.split("/", 2);
        if (isNumber(substrings[0]) && isNumber(substrings[1])) {
            return true;
        } else {
            return false;
        }
    }
    // this is a helper function for validFraction() method that checks if the provided string contains an integer.
    private static boolean isNumber(String fraction) {
        if (fraction.isEmpty()) {
            return false;
        }
        try {
            int num = Integer.parseInt(fraction);
            return true;
        }
        catch (NumberFormatException e) {
            return false;
        }
    }
    // this is used to get the fraction from the user and is validated using the result given by validFraction().
    public static Fraction getFraction(Scanner input) {
        System.out.println("Please enter a fraction (a/b) or integer (a): ");
        String frac = input.next();
        while(!validFraction(frac)) {
            System.out.print("Invalid fraction. Please enter (a/b) or (a), where a and b are integers and b is not zero: ");
            frac = input.next();
        }
        int numerator, denominator;
        if (frac.indexOf('/') != -1) {
            String[] substring = frac.split("/", 2);
            numerator = Integer.parseInt(substring[0]);
            if (!substring[1].isEmpty()) {
                denominator = Integer.parseInt(substring[1]);
            } else {
                denominator = 1;
            }
        } else {
            numerator = Integer.parseInt(frac);
            denominator = 1;
        }
        Fraction fraction = new Fraction(numerator, denominator);                   // creating the fraction after all validations
        return fraction;
    }
}