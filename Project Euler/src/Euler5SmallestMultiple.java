import java.util.Arrays;

// Smallest multiple
//2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
//What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
// LCM(a,b) = (a*b)/GCD(a,b);
public class Euler5SmallestMultiple {
    public static void main(String[] args){
        int[] arr = new int[10];
        for(int i=0; i<10; i++){
            arr[i] = i+1;
        }
        System.out.println(Arrays.toString(arr));
        int lcm = lcmArray(arr);
        System.out.println("Smallest multiple LCM is: "+ lcm);
    }
    public static int lcmArray(int[] arr){
        int lcm = 1;
        int divisor = 2;
        for(int i = 0; i<arr.length; i++){
            answer = (arr[i]*answer)/GCD2Num(arr[i], answer);
        }
        return answer;
    }
    public static int GCD2Num(int x, int y){
        if(x==0){
            return y;
        }else{
            return GCD2Num(y%x,y);
        }
    }
}
