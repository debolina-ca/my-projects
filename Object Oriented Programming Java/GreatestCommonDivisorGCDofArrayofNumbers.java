import java.util.Scanner;
public class GreatestCommonDivisorGCDofArrayofNumbers {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter number of elements");
        int num = input.nextInt();
        int[] arr = new int[num];
        for(int i=0; i<num; i++) {
            arr[i] = input.nextInt();
        }
        System.out.println("The greatest common divisor is: " + generalizedGCD(num, arr));
    }
    public static int gcd2Num(int x, int y) {
        if(x==0) {
            return y;
        }else{
            return(gcd2Num(y%x, x));
        }
    }
    public static int generalizedGCD(int num, int[] arr) {
        int gcdAnswer = arr[0];
        for(int i=0; i<num; i++){
            gcdAnswer = gcd2Num(arr[i], gcdAnswer);
            if (gcdAnswer==1){
                return 1;
            }
        }
        return gcdAnswer;
    }
}
