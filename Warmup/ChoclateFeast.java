import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    // Instance variable for Data Stream
    private static BufferedReader dataStream;
    
    // Main Function
    public static void main(String[] args) throws Exception {
        // Instantiating the data Stream
        dataStream = new BufferedReader(new InputStreamReader(System.in));
        // Parsing the input and calling the static method for computing the output
        int t = Integer.parseInt(dataStream.readLine());
        
        // Iterating through all cases
        for(int j = 0;j < t;j++){
            // Parsing the input
            String[] inputArr = dataStream.readLine().split(" ");
            int[] inputArrInt = new int[3];
            for(int i = 0;i < 3;i++)
                inputArrInt[i] = Integer.parseInt(inputArr[i]);
            
            // Calling the main function that computes the optimum CHoclates
            int chocs = getMaxChocs(inputArrInt[0],inputArrInt[1],inputArrInt[2]);
            
            // Printing the output for this case
            System.out.println(chocs);
        }
    }
    
    /**
     * Returns teh max amount of choclates that a person can get given n,c,m
     * @param n,c,m The initial money in $ - n, the Cost of Choclate $ - c, and Wrappers to Chochlate m
     * @returns chocs the maximum amount of choclates that can be bought with the n,c,m
     */ 
    public static int getMaxChocs(int n ,int c,int m){
        int wraps = 0;
        int chocs = 0;
        chocs += n/c;
        wraps += chocs;
        while(wraps/m != 0 ){
            chocs += wraps/m;
            wraps = wraps/m + wraps%m;
        }
        return chocs;
    }
    
    
}
