// Let's say as you are looping over your ArrayList you decided to delete an element. Now the index of the last element is one less than
// when you started the loop- this means if you don't adjust the loop variable you will run off the end and get an ArrayIndexOutOfBounds exception.
//One way to solve this is to store the size of the array as a static variable before your loop, and then to manually adjust the variable
// whenever you change the size of the list. This way you have direct control over what value is being used in your loop test.
import java.util.ArrayList;

public class StaticSize {
    public static void main(String[] args) {
        ArrayList<Integer> myList = new ArrayList<Integer>();
        int staticSize = myList.size();
        for (int i = 0; i < staticSize; i++) {
            if (myList.get(i) == 0) {
                myList.remove(i);
                staticSize--;
            } else if (myList.get(i) == -1) {
                myList.add(-1);
                staticSize++;
            }
        }
    }
}
