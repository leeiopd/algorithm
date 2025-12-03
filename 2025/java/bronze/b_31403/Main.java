package bronze.b_31403;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a = in.nextInt();
        int b = in.nextInt();
        int c = in.nextInt();

        System.out.println(a+b-c);

        String result = "";
        result += a;
        result += b;
        System.out.println(Integer.parseInt(result) - c);
    }
}
