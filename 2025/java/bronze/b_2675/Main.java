package bronze.b_2675;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int T = in.nextInt();
        for (int i = 0; i < T; i++) {
            int R = in.nextInt();
            String S = in.next();

            for (String s : S.split("")) {
                for (int j = 0; j < R; j++) {
                    System.out.print(s);
                }
            }
            System.out.println();
        }

    }
}
