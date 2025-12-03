package bronze.b_2475;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a = in.nextInt();
        int b = in.nextInt();
        int c = in.nextInt();
        int d = in.nextInt();
        int e = in.nextInt();
        in.close();

        System.out.println((int)(a*a + b*b + c*c + d*d + e*e) % 10);
    }
}
