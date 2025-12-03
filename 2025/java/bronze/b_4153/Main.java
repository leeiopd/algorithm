package bronze.b_4153;

import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        while (true) {
            List<Integer> triangle = Arrays.stream(in.nextLine().split(" "))
                    .map(Integer::parseInt)
                    .sorted()
                    .collect(Collectors.toList());

            Integer A = triangle.get(0);
            Integer B = triangle.get(1);
            Integer C = triangle.get(2);

            if (A == 0
                    && B == 0
                    && C == 0
            ) {
                return;
            }

            if (A * A + B * B == C * C) {
                System.out.println("right");
            } else {
                System.out.println("wrong");
            }
        }
    }
}
