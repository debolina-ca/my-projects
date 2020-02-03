import java.util.ArrayList;

// Largest palindrome product
//A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
// 9009 = 91 × 99.
//Find the largest palindrome made from the product of two 3-digit numbers.
public class Euler4LargestPalindromeProduct {
    public static void main(String[] args){
        int product = 1;
        int largestPalindrome = 0;
        boolean numPalindrome = false;
        ArrayList<Integer> listOfPalindromes = new ArrayList<>();
        for(int i = 999; i>99; i--){
            for(int j = i; j>99; j--){
                product = i * j;
                numPalindrome = isPalindrome(product);
                if(numPalindrome){
                    listOfPalindromes.add(product);
                }
            }
        }
        for(int i = 0; i<listOfPalindromes.size(); i++){
            if(listOfPalindromes.get(i) > largestPalindrome){
                largestPalindrome = listOfPalindromes.get(i);
            }
        }
        System.out.println("List of palindromes are: "+listOfPalindromes);
        System.out.println("The largest palindrome from the product of two three-digit numbers is: "+ largestPalindrome);
    }
    // Method/function to check whether a number num is palindrome or not
    public static boolean isPalindrome(int num){
        String numStr = Integer.toString(num);          // Cast integer to String
        int j = numStr.length() - 1;
        for(int i=0; i<j; i++){
            if(numStr.charAt(i) != numStr.charAt(j)){
                return false;
            }
            j--;
        }
        return true;
    }
}