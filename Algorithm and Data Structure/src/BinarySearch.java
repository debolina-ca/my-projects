public class BinarySearch {
    public static void main(String[] args) {
        int[] lst = {1,3,4,5,6,7,9};
        boolean presentOrNot = binarySearch(1,lst,0,6);
        System.out.println(presentOrNot);
    }
    // low and high are the indices
    static boolean binarySearch(int v, int[] lst, int low, int high) {
        if (low > high) {
            System.out.println("not found");
            return false;
        }

        int middle = (low+high)/2;

        if (v == lst[middle]) {
            System.out.println("found! It is at " + middle);
            return true;
        }
        else if (v > lst[middle]) {
            return binarySearch(v, lst, middle+1, high);
        }
        else {
            return binarySearch(v, lst, low, middle-1);
        }
    }
}
