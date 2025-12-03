package bronze.b_2562;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int big = 0;
        int result = 0;
        for (int i = 0; i < 9 ; i++) {
            int n = in.nextInt();
            if(n > big){
                big = n;
                result = i+1;
            }
        }

        System.out.println(big);
        System.out.println(result);
    }
}
