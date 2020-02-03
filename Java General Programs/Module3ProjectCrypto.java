// Module 3 Project Writing methods of encrypting and decrypting text.
import java.util.Scanner;

public class Module3ProjectCrypto {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter text: ");
        String text = input.nextLine();
        System.out.print("Enter shift value: ");
        int shift = input.nextInt();
        System.out.print("Enter no. of letters per group for encryption: ");
        int n = input.nextInt();
        encryptString(text, shift, n);
    }
    // Part 1 - Normalize Text
    public static String normalizeText(String text) {
        text = text.replaceAll("\\s+", "");              // remove all whitespaces and \n from text
        text = text.replaceAll("\\p{Punct}", "");        // remove all punctuation from text
        text = text.toUpperCase();
        return text;
    }
    // Obify Method - Turn normalized string into obfuscated string i.e. add OB in front of every vowel including Y
    public static String obify(String text) {
        String result = "";
        for (int i = 0; i < text.length(); i++) {
            int start = text.charAt(i);
            if (start=='A'||start=='E'||start=='I'||start=='O'||start=='U'||start=='Y') {
                result = result + "OB" + (char) start;
            } else {
                result = result + (char) start;
            }
        }
        return result;
    }
    // Part 2 - Caesar Cipher
    // a function called shiftAlphabet. This function takes one argument, an integer to specify the shift value, and returns a string,
    // which is the uppercase alphabet shifted by the shift value. So if you call shiftAlphabet(2), you will get back the following string:
    // “CDEFGHIJKLMNOPQRSTUVWXYZAB”
    public static String shiftAlphabet(int shift) {
        int start = 0;
        if (shift < 0) {
            start = (int) 'Z' + shift + 1;
        } else {
            start = 'A' + shift;
        }
        String result = "";
        char currChar = (char) start;
        for(; currChar <= 'Z'; ++currChar) {
            result = result + currChar;
        }
        if(result.length() < 26) {
            for(currChar = 'A'; result.length() < 26; ++currChar) {
                result = result + currChar;
            }
        }
        return result;
    }
    // A Caesar encryption "shifts" each individual character forward by a certain number or "key". Each letter in the alphabet is shifted to
    // the letter in the alphabet that is "key" places past the original letter.
    public static String caesarify(String text, int shift) {
        String result = "";
        String alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String shiftedAlphabet = shiftAlphabet(shift);
        for (int i = 0; i < text.length(); i++) {
            int letter = text.charAt(i);
            char currChar = (char) letter;
            int indx = alphabet.indexOf(currChar);
            char newChar = shiftedAlphabet.charAt(indx);
            result = result + newChar;
        }
        return result;
    }
    public static String groupify(String text, int n) {
        String result = "";
        while (text.length()%n != 0) {
            text = text + "x";
        }
        for (int i = 0; i < text.length(); i++) {
            int letter = text.charAt(i);
            if(i > 0 && i%n == 0) {
                result = result + " " + (char) letter;
            } else {
                result = result + (char) letter;
            }
        }
        return result;
    }
    public static String encryptString(String text, int shift, int n) {
        Scanner input = new Scanner(System.in);
        text = normalizeText(text);
        System.out.println("Normalized text: \n" + text);
        text = obify(text);
        System.out.println("Obified text: \n" + text);
        text = caesarify(text, shift);
        System.out.println("Ceasarified text: \n" + text);
        text = groupify(text, n);
        System.out.println("Final encrypted text: \n" + text);
        return text;
    }
}
