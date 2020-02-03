// Trip Planner - Module 1 Project Assignment
import java.util.Scanner;
public class TripPlannerModule1ProjectAssignment {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        greeting();
        travelTimeAndBudget();
        timeDifference();
        countryArea();
    }

    public static void greeting() {
        Scanner input = new Scanner(System.in);
        System.out.println("Welcome to Vacation Planner!");
        System.out.print("What is your name? ");
        String name = input.nextLine();
        System.out.print("Nice to meet you " + name + ", where are you travelling to? ");
        String city = input.nextLine();
        System.out.print("Great! " + city + " sounds like a great trip.\n***********\n\n");
    }

    public static void travelTimeAndBudget() {
        Scanner input = new Scanner(System.in);
        System.out.print("How many days are you going to spend travelling? ");
        int days = input.nextInt();
        double hours = days * 24;
        double minutes = hours * 60;
        System.out.print("How much money, in USD, are you planning to spend on your trip? ");
        int budgetUSD = input.nextInt();
        System.out.print("What is the three letter currency symbol for your travel destination? ");
        String destinationCurrency = input.next();
        System.out.print("How many " + destinationCurrency + " are there in 1 USD? ");
        double currencyConversionRate = input.nextDouble();
        System.out.println("");
        double budgetLocalCurr = budgetUSD * currencyConversionRate;
        budgetLocalCurr = Math.round(budgetLocalCurr);
        double perDayBudget = (double) (budgetUSD / days);
        perDayBudget = Math.round(perDayBudget);
        double perDayBudgetLocalCurr = budgetLocalCurr / days;
        perDayBudgetLocalCurr = Math.round(perDayBudgetLocalCurr);
        System.out.println("If you are travelling for " + days + " days that is same as " + hours + " hours or " + minutes + " minutes. ");
        System.out.println("If you are going to spend $" + budgetUSD + " USD that means per day you can spend up to $" + perDayBudget + " USD.");
        System.out.println("Your total budget in " + destinationCurrency + " is " + budgetLocalCurr + " " + destinationCurrency + ", which per day is " + perDayBudgetLocalCurr + " " + destinationCurrency);
        System.out.println("***********\n");
    }

    public static void timeDifference() {
        Scanner input = new Scanner(System.in);
        System.out.print("What is the time difference, in hours, between you and your travel destination? ");
        double timeDiff = input.nextDouble();
        int timeDiffHr = (int)timeDiff;
        int timeDiffMinutes = (int)((timeDiff - timeDiffHr) * 60);
        timeDiffMinutes = Math.abs(timeDiffMinutes);
        double timeThereAtMidnightHr = (24 + timeDiffHr) % 24;
        //timeThereAtMidnight = Math.round(timeThereAtMidnight);
        double timeThereAtNoon = (12 + timeDiff) % 24;
        //timeThereAtNoon = Math.round(timeThereAtNoon);
        System.out.println("That means that when it is midnight at home it will be " + (int)timeThereAtMidnightHr + ":" + timeDiffMinutes + " in your travel destination and when it is noon at home it will be " + (int)timeThereAtNoon + ":" + timeDiffMinutes + "\n***********\n");
    }

    public static void countryArea() {
        Scanner input = new Scanner(System.in);
        System.out.print("What is the square area of your destination country in km2? ");
        int areaInKm2 = input.nextInt();
        double areaInMiles2 = 0.62137 * 0.62137 * areaInKm2;
        areaInMiles2 = Math.round(areaInMiles2);
        System.out.println("In Miles2 that is " + areaInMiles2 + "\n***********\n");
    }
}
