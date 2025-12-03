package bronze.b_27866;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String string = in.next();
        int n = in.nextInt();

        String result = string.substring(n-1, n);
        System.out.println(result);
    }
}
