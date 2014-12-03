import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    // Instance variable to parse in input
    private static BufferedReader dataStream;
   
    public static void main(String[] args) throws Exception{
        
        // Parsing in the Input
        dataStream = new BufferedReader(new InputStreamReader(System.in));
        int a = Integer.parseInt(dataStream.readLine());
        int b = Integer.parseInt(dataStream.readLine());
        
        // Creating intance of solution class
        Solution s = new Solution();
        
        // Invoking the method that does the solving
        int result = s.sum(a,b);
        
        // Printing out the result
        System.out.println(result);
    }
    
    /**
     * Returns the sum of the integers a and b
     * @param a,b The parameters to be added
     * @returns The sum of a and b
     */
    public int sum(int a,int b){
        return a+b;
    }
}
