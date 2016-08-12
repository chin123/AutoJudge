import java.io.*;
import java.util.*;


public class sum_2 {

	public static void main(String[] args) {
        BufferedReader reader = new BufferedReader(
                new InputStreamReader(System.in));

           try {

               while (true) {
            
                    String[] line = reader.readLine().split(" ");
                    int num1 = Integer.parseInt(line[0]);
                    int num2 = Integer.parseInt(line[1]);

                    if (num1 == 0 && num2 == 0)
                        break;

                    System.out.println(num1 + num2); 
               } 
           }
           catch (Exception e) { }
	}

}

