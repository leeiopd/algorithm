package bronze.b_10871;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        int X = in.nextInt();

        StringBuilder result = new StringBuilder();
        for (int i = 0; i < N; i++) {
            int n = in.nextInt();
            if (n < X) {
                result.append(n).append(" ");
            }
        }
        System.out.println(result.substring(0, result.length() - 1));
    }
}
