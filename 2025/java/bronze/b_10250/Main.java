package bronze.b_10250;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int T = in.nextInt();
        List<String> result = new ArrayList<>();
        for (int i = 0; i < T; i++) {
            result.add(roomNumber(in));
        }
        result.forEach(System.out::println);
    }

    private static String roomNumber(Scanner in) {
        int H = in.nextInt();
        int W = in.nextInt();
        int N = in.nextInt();

        int Y = N % H == 0 ? H : N % H;
        int X = N % H == 0 ? N / H : N / H + 1;

        return X < 10 ? Y + "0" + X : "" + Y + X;
    }
}
