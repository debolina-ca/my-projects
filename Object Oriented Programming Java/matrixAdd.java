import java.util.Arrays;
import java.util.Scanner;

// Write a method named matrixAdd that accepts a pair of two-dimensional arrays of integers as parameters,
// treats the arrays as 2D matrices and adds them, returning the result. The sum of two matrices A and B is a matrix C
// where for every row i and column j, Cij = Aij + Bij. You may assume that the arrays passed as parameters have the same dimensions.
public class matrixAdd {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Please enter no. of rows in matrix: ");
        int rows = input.nextInt();
        System.out.println("Please enter no. of columns in matrix: ");
        int cols = input.nextInt();
        int[][] A = new int[rows][cols];
        int[][] B = new int[rows][cols];
        System.out.println("Please enter elements of first matrix:\n");
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                System.out.print("["+i+","+j+"]: ");
                A[i][j] = input.nextInt();
            }
        }
        System.out.print("Matrix A: ");
        System.out.println(Arrays.toString(A));
        System.out.println("Please enter elements of second matrix:\n");
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                System.out.println("["+i+","+j+"]: ");
                B[i][j] = input.nextInt();
            }
        }
        System.out.print("Matrix B: ");
        System.out.println(Arrays.toString(B));
        int[][] C = matrixAdd(A, B);
        System.out.println(Arrays.toString(C));
    }
    public static int[][] matrixAdd(int[][]A, int[][]B) {
        int[][] C = Arrays.copyOf(A, A.length);
        for(int i = 0; i < A.length; i++) {
            for(int j = 0; j < A[0].length; j++) {
                C[i][j] = A[i][j] + B[i][j];
            }
        }
        return C;
    }
}