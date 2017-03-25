import java.io.*;
import java.util.*;
import java.math.*;

public class Solution {
    // Instance variables
    private static BufferedReader dataStream;
    
    // Main program
    public static void main(String[] args) throws Exception{
        // New Data Stream Instance
        dataStream  = new BufferedReader(new InputStreamReader(System.in));
        // Parsing in Input
        int n = Integer.parseInt(dataStream.readLine());
        int k = Integer.parseInt(dataStream.readLine());
        int[] candies = new int[n];
        for(int i = 0;i < n;i++){
            candies[i] = Integer.parseInt(dataStream.readLine());
        }
        // New solution instance
        Solution soln = new Solution();
        int result = soln.getMinUnfairness(candies,k);
        // Printing the output to the console
        System.out.println(result);
    }
    
    /** Sliding window algorithm on sorted candy array that determines min unfairness
     * Complexity is O(n). Counting sort is done since N has an upper bound (finite). 
     * @param candies Unsorted array of candies
     * @returns minUnfairness
     */
    private int getMinUnfairness(int[] candies,int k){
        // Sorting the candies
        Arrays.sort(candies);
        // Sliding on the window and recording the minUnfairness on all possible
        // windows with the candies array
        int result = candies[k-1] - candies[0];
        for(int i = 1;i < candies.length-k;i++){
            int curUnfairness = candies[i+k-1] - candies[i];
            if(curUnfairness<result)
                result = curUnfairness;
        }
        return result;
    }   
}
