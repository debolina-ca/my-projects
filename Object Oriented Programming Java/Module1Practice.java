public class Module1Practice {
    public static void main(String[] args) {

        /*int[] anArray = new int[4];
        anArray[0] = 4;
        anArray[1] = 6;
        anArray[2] = 7;
        anArray[3] = 3;
        for(int j = 0; j < anArray.length; j++){
            System.out.print(anArray[j] + " ");
        }*.
        /*int[][] arr = {{0, 1, 2}, {3, 4, 5}, {6, 7, 8}};
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                if (arr[i][j] % 2 == 0) {
                    System.out.println(arr[i][j]);
                }
            }
        }*/
        /*int[][] numbers = {{44, 45, 16, 50}, {16, 12, 66, 9}, {52, 83, 3, 37}, {56, 61, 69, 61}};
        numbers = twoDimensions(numbers);
        for (int i = 0; i < numbers.length - 1; i++){
            for (int j = 0; j < numbers[i].length - 1; j++){
                System.out.print(numbers[i][j] + "  ");
            }
            System.out.println();
        }*/
    }
    /*public static int[][] twoDimensions(int[][] numbers){
        for (int i = 0; i < numbers.length - 1; i++){
            for (int j = 0; j < numbers[i].length - 1; j++){
                if (numbers[i][j] < numbers[i][j + 1]){
                    numbers[i][j] = numbers[i][j] + numbers[i + 1][j];
                    numbers[i + 1][j] = numbers[i + 1][j] / 2;
                }
            }
        }
        return numbers;
    }*/
}
