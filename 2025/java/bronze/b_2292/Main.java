package bronze.b_2292;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();

        for (int i = 1; i <= 100000; i++) {
            int count = 1 + 6*(i*(i-1)/2);

            if(N <= count){
                System.out.println(i);
                return;
            }
        }
    }
}
