public class practice {
    public static void main(String[] args) {
        smallest(a, b, c);
        /*String word = "a";
        while (word.length() < 10) {
            word = "b" + word + "b";
        }
        System.out.println(word); */

        /*String a = "";
        a += "0";
        if (a == "0") {
            System.out.println("a is 0!");
        } else if (a == "1") {
            System.out.println("a is 1!");
        } else if (a == "a") {
            System.out.println("a is a!");
        } else {
            System.out.println("a is something else!");
            System.out.println(a);
        }*/

        /*int a = 3;
        int b = -2;
        if((a>0)&&(b>0)){
            if (a>b) {
                System.out.println("A");
            } else {
                System.out.println("B");
            }
        } else if ((b<0)||(a<0)) {
            System.out.println("C");
        } else {
            System.out.println("D");
        }*/
        /*int a = 10;
        int b = 30;
        if (a * 2 < b) {
            a = a * 3;
        }
        if (b < a) {
            b++;
        } else {
            a--;
        }
        System.out.println(a + " " + b);*/

        /*int num = 1;
        for (int i = 0; i < 11; i++) {
            System.out.print(num + " ");
            num += num;
        }*/

        /*int c = 5;
        for (int i = 2; i <= c; i++) {
            for (int j = 0; j < i; j++) {
                System.out.println("Tricky!");
            }
        }*/

        /*int x = 200;
        while (x >= 0) {
            System.out.print(2 * x + " ");
            x /= x;
        }*/

        /*int x = 64;
        int y = 0;
        while (x % 2 == 0) {
            y++;
            x = x / 2;
        }
        System.out.println(x + " " + y);*/

        /*int x;
        for (x = 0;  x <= 7; x += 7) {
            System.out.println("Here");
        }
        System.out.println(x);*/
        //mystery(1);
        //puzzle(22, 11);
    }
    /*public static int mystery (int x) {
        if (x == 5){
            return x;
        } else {
            return mystery(x--) * 5;
        }
    }*/
    /*public static int puzzle(int i, int j) {
        if (i == j) {
            return 0;
        } else {
            return 1 + puzzle(i – 2, j – 1);
        }
    }*/
    public static int smallest(int a, int b, int c) {
        return Math.min(Math.min(a, b), c);
    }
}
