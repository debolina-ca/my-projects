// Eight houses, represented as cells, are arranged in a straight line. Each day every cell competes with its adjacent cells(neighbors).
// An integer value of 1 represents an active cell and a value of 0 represents an inactive cell. If the neighbors on both sides of a cell
// are either active or inactive, the cell becomes inactive on the next day, otherwise the cell becomes active. The two cells on each end
// have a single adjacent cell, so assume that the unoccupied space on the opposite side is an inactive cell. Even after updating the cell
// state, consider its previous state when updating the state of other cells. The state information of all cells should be updated simultaneously.
// WAP to output the state of the cells after the given number of days. The input to the function/method consists of two arguments states,
// a list of integers representing the current state of cells, days an integer representing the number of days.
// The program should output a list of integers representing the state of the cells after the given number of days.
// The elements of the list states contains 0's and 1's only.

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
public class EightHousesArray {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        //int[] states = new int[8];
        /*for( int i=0; i<8; i++){
            states[i] = (input.nextInt());
        }*/
        int[] states = {1, 0, 1, 0, 0, 1, 1, 1};
        System.out.println(cellCompete(states, 5));
    }
    public static List<Integer> cellCompete(int[] states, int days) {
        List<Integer> list = new ArrayList<>();
        // Initializing day 1
        int[][] statesDay1ToDayEnd = new int[days+1][10];
        for(int i=0; i<days; i++){
            statesDay1ToDayEnd[i][0] = 0;
            statesDay1ToDayEnd[i][9] = 0;
        }
        for(int i=0; i<days; i++) {
            for (int j = 1; j < 9; j++) {
                statesDay1ToDayEnd[0][j] = states[j-1];
            }
        }
        // Calculating states for the next days
        for(int i=0; i<days; i++) {
            for (int j = 1; j < 9; j++) {
                if(statesDay1ToDayEnd[i][j-1] == statesDay1ToDayEnd[i][j+1]){
                    statesDay1ToDayEnd[i+1][j] = 0;
                }else{
                    statesDay1ToDayEnd[i+1][j] = 1;
                }
            }
        }
        // Convert array to list for states after the last day
        for (int j = 1; j < 9; j++) {
            list.add(statesDay1ToDayEnd[days][j]);
        }
        return list;
    }
}
