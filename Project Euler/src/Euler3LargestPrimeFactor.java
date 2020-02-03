import java.util.ArrayList;

// Largest prime factor
//The prime factors of 13195 are 5, 7, 13 and 29.
//What is the largest prime factor of the number 600851475143 ?
public class Euler3LargestPrimeFactor {
    public static void main(String[] args){
        long num = 600851475143L;
        int largest = 1;
        ArrayList<Integer> prmFactors = PrimeFactors(num);
        System.out.println("The prime factors of "+num+ " are: "+ prmFactors);
        for(int i = 0; i<prmFactors.size(); i++){
            if(prmFactors.get(i) > largest){
                largest = prmFactors.get(i);
            }
        }
        System.out.println("The largest prime factor of "+num+" is: "+largest);
    }
    public static ArrayList<Integer> PrimeFactors(long num){
        ArrayList<Integer> primeFactorsList = new ArrayList<>();
        while(num%2 == 0){
            primeFactorsList.add(2);                      // Adds the number of 2s to the list that divide n
            num = num/2;
        }
        // And after step 1, all remaining prime factor must be odd
        for(int i = 3; i < Math.sqrt(num); i+=2){        // Every composite number has at least one prime factor less than or equal to square root of itself. This property can be proved using counter statement. Let a and b be two factors of n such that a*b = n. If both are greater than √n, then a.b > √n * √n, which contradicts the expression “a * b = n”.
            if(num%i == 0){
                primeFactorsList.add(i);
                num = num/i;
            }
        }
        // For prime factors that is greater than 2
        if(num>2){
            Integer n = (int)(long)num;
            primeFactorsList.add(n);
        }
        return primeFactorsList;
    }
}
