import java.util.*;

public class ProjectBattleshipCopied {
    static char[][] leMap = new char[10][10];

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Random guess = new Random();
        System.out.println("Welcome to Battleship: the classic naval combat game!");
        //making a blank map for the actual map
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                leMap[i][j] = ' ';
            }
        }
        leMapdispaly();
        acquire();

        //This is going to be making the game
        int ships = 5, aiships = 5, x, y;
        while (ships != 0 && aiships != 0) {
            System.out.println("\nIt's Your Turn");
            do {
                System.out.print("Enter the X coordinate: ");
                x = input.nextInt();
                System.out.print("Enter the Y coordinate: ");
                y = input.nextInt();
                if (x < 0 || x > 9 || y < 0 || y > 9) {
                    System.out.println("Please Enter a Valid Input!");
                } else if (leMap[x][y] == '-') {
                    System.out.println("Please choose a space you haven't already selected!");
                } else if (leMap[x][y] == 'x') {
                    System.out.println("Your ship had sunk here, try again.");
                } else if (leMap[x][y] == '!') {
                    System.out.println("You have sunk computer's ship here, try again.");
                }
            } while (x < 0 || x > 9 || y < 0 || y > 9 || leMap[x][y] == '-' || leMap[x][y] == 'x' || leMap[x][y] == '!'); //This is making it so you can find what happened to your move

            if (leMap[x][y] == '2') {
                System.out.println("You have sunk a ship Admiral!");
                leMap[x][y] = '!';
                aiships--;
            } else if (leMap[x][y] == '1') {
                System.out.println("You shot your own ship...");
                leMap[x][y] = 'x';
                ships--;
            } else {
                System.out.println("You have missed");
                leMap[x][y] = '-';
            }

            System.out.println("\nAI's Turn");
            do {
                x = guess.nextInt(10);
                y = guess.nextInt(10);
            } while (leMap[x][y] == '#' || leMap[x][y] == '!' || leMap[x][y] == 'x');

            if (leMap[x][y] == '1') {
                System.out.println("The Computer sunk one of your ships!");
                ships--;
                leMap[x][y] = 'x';
            } else if (leMap[x][y] == '2') {
                System.out.println("The Computer sunk one of its own ships!");
                aiships--;
                leMap[x][y] = '!';
            } else {
                System.out.println("Computer missed");
                leMap[x][y] = '#'; // if computer misses the guess
            }
            leMapdispaly();
            System.out.println("Your ships: " + ships + " | Computer ships: " + aiships);
        }
        if (ships == 0)
            //losing screen
            System.out.println("We may have lost the battle, but not the war!(You lost)");
        else
            //The VICTORY screen
            System.out.println("You won the battle!");
        System.out.println("----------------------------------------");
    }

    //This shows the map
    public static void leMapdispaly() {
        System.out.println("\n   0-1-2-3-4-5-6-7-8-9   ");
        for (int i = 0; i < 10; i++) {
            System.out.print(i + "| ");
            for (int j = 0; j < 10; j++) {
                if (leMap[i][j] == '1')
                    System.out.print("@ "); // displaying user's ships with '@' symbol.
                else if (leMap[i][j] == '2') //all these 'else ifs' are what I like to call the hiding
                    System.out.print("  ");
                else if (leMap[i][j] == '#')
                    System.out.print("  ");
                else
                    System.out.print(leMap[i][j] + " ");
            }
            System.out.print("|" + i + "\n");
        }
        System.out.println("   0-1-2-3-4-5-6-7-8-9   ");
    }

    //This acquires the ships from the user
    public static void acquire() {
        //User deploying ships
        Scanner input = new Scanner(System.in);
        System.out.println("\nDeploy your ships:");
        int x, y;
        //this looks for your input coords
        boolean isXAndYCorrect;

        for (int i = 0; i < 5; i++) {
            do {
                isXAndYCorrect = true;
                //this is finding the ships
                System.out.print("Enter X coordinate of ship " + (i + 1) + ": ");
                x = input.nextInt();
                System.out.print("Enter Y coordinate of ship: " + (i + 1) + ": ");
                y = input.nextInt();
                if (x < 0 || x > 9 || y < 0 || y > 9) {
                    System.out.println("Choose coordinates between 0 and 9");
                    isXAndYCorrect = false;
                } else if (leMap[x][y] == '1') {
                    System.out.println("You cannot place two ships at one place");
                    isXAndYCorrect = false;
                }
            } while (!isXAndYCorrect);
            leMap[x][y] = '1';
        }
        //computer deploying ships
        Random rand = new Random();
        System.out.println("\nThe computer is deploying ships:");
        //this is making a randomized finder for the computer
        for (int i = 0; i < 5; i++) {
            do {
                x = rand.nextInt(10); // generates random number
                y = rand.nextInt(10); // from 0 to 9
            } while (leMap[x][y] == 1);
            leMap[x][y] = '2';
            System.out.println("Ship " + (i + 1) + " DEPLOYED");
        }
        //The split
        System.out.println("----------------------------------------");
        leMapdispaly();
    }
}