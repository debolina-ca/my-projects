import java.util.Scanner;
public class IsVowelOrNot {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.print("Enter a single letter: ");
        String str = input.next();
        System.out.println(isVowel(str));
    }
    public static boolean isVowel(String str) {
        boolean result = false;
        str = str.toLowerCase();
        if ((str.equals("a"))||(str.equals("e"))||(str.equals("i"))||(str.equals("o"))||(str.equals("u"))) {
            result = true;
        } else {
            result = false;
        }
        return result;
    }
}
