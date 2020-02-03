// Print first 25 numbers in the Fibonacci series starting with
// 1, 2, 3, 5, .... using FOR LOOP without using recursion.
import java.util.Arrays;
public class FibonacciForLoop {
    public static void main(String[] args){
        int[] arr = new int[25];
        arr[0] = 1;
        arr[1] = 2;
        for(int i=2; i<25; i++){
            arr[i] = arr[i-2] + arr[i-1];
        }
        System.out.println(Arrays.toString(arr));
    }
}