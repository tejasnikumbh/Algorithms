import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

/*
 * Simple Brute force algorithms is okay because of the constraints on the
 * input size. Brute force Algorithm has time complexity of O(10^7)
 */
public class Solution {
    
    // Data stream to read the input from
    private static BufferedReader dataStream;
    // Random Class instance that is of use to the core algorithms
    private static Random rand;
    
    
    public static void main(String[] args) throws Exception {
        // Input parsing using dataStream
        dataStream = new BufferedReader(new InputStreamReader(System.in));
        // Parsing total number of test cases
        int t = Integer.parseInt(dataStream.readLine());
        
        // Iterating through each test case
        for(int i = 0;i < t;i++){
            
            // Input Parsing for each test case
            String[] seedRange = dataStream.readLine().split(" ");
            int minS = Integer.parseInt(seedRange[0]);
            int maxS = Integer.parseInt(seedRange[1]);
            int[] core10 = new int[10];   
            for( int j = 0;j < 10;j++){
                core10[j] = Integer.parseInt(dataStream.readLine());
            }
            
            
            
            // Computing the seed
            int seed = getSeed(minS,maxS,core10);
            // Generating next 10 numbers using seed
            int[] next10 = getNums();
            
            // Generating the output and printing it to screen
            String outputStr = seed + " ";
            for(int j = 0;j < 10;j++){
                outputStr += next10[j] + " ";
            }
            System.out.println(outputStr);
        }
    }
    
    public static int[] getNums(){
        int[] cur10 = new int[10];
        for(int i = 0;i < 10; i++){
            cur10[i] = rand.nextInt(1000);
        }
        return cur10;
    }
    
    public static int getSeed(int minS,int maxS,int[] core10){
        
        // Iterating through allseeds
        for(int i = minS;i <= maxS;i++){
            
            // Generating 10 random numbers from current seed
            rand = new Random(i);
            int[] cur10 = new int[10];
            for(int j = 0;j < 10;j++)
                cur10[j] = rand.nextInt(1000);
            
            // Checking if the 10 generated are equalt o core10
            boolean isEqual = true;
            for(int j = 0;j < 10;j++){
                if(cur10[j] != core10[j]) {
                    isEqual = false;
                    break;
                }    
            }
            
            // Returning the seed if they are found to be equal
            if(isEqual) return i;
        }
        
        // Returning -1 if no seed matches
        return -1;
    }
}
