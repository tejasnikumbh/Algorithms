import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    // Instance Variale to parse in data
    private static BufferedReader dataStream;

    public static void main(String[] args) throws Exception{
        
        // Parsing the input from the data stream
        dataStream  =  new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(dataStream.readLine());
        int[] nums = new int[t];
        for(int i = 0;i < t;i++) {
            nums[i] = Integer.parseInt(dataStream.readLine());
        }
        
        //Creating a new instance of the problem
        Solution soln = new Solution();
        int[] counts = soln.genCounts(nums);
        
        // Printing Output
        for(int i = 0;i < counts.length;i++)
            System.out.println(counts[i]);
        
    }
    
    /**
     * Generates the counts for all the numbers. Algo takes O(n) time where n is no of digits in N
     * @param nums Array of numbers to solve for
     * @returns counts Array of results with repective problem order
     */
    public int[] genCounts(int[] nums){
        int len = nums.length;
        int[] counts = new int[nums.length];
        for(int i = 0;i < len;i++){
            String numStr = String.valueOf(nums[i]);
            int cur = 0;
            for(int j=0;j<numStr.length();j++){
                cur = Integer.parseInt(String.valueOf(numStr.charAt(j)));
                if(cur != 0){ 
                    if(nums[i]%cur == 0 ) counts[i]++;
                }    
            }     
        }
        
        return counts;
    }
}
