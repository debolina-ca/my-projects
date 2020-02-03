public class LinearSearch {
    public static void main(String[] args) {
        int[] lst = {4, 9, 7, 1, 3, 6, 5, 2, 0, 8};
        int v = 5;
        linearSearch(lst, v);
    }
    static void linearSearch(int[] lst, int v) {
        int n = lst.length;
        for (int i = 0; i < n; i++) {
            if (lst[i] == v) {
                System.out.println("found! It is at " + i);
                return;
            }
        }
        System.out.println("the element is not in the array");
        return;
    }
}
