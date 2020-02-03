import java.util.Scanner;
public class days_In_Month {
    public static void main (String[] args) {
        Scanner input = new Scanner(System.in);
        System. out. print("Enter a month from 1 - 12 where 1 is Jan and 12 is Dec: ");
        int month = input.nextInt();
        daysInMonth(month);
    }
    public static int daysInMonth(int month) {

        int days;
        if ((month == 1)||(month == 3)||(month == 5)||(month == 7)||(month == 8)||(month == 10)||(month == 12)){
            days = 31;
        } else if (month == 2) {
            days = 28;
        } else {
            days = 30;
        }
        System.out.println(days + " days");
        return days;
    }
}
