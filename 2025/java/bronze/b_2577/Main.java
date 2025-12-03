package bronze.b_2577;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int A = in.nextInt();
        int B = in.nextInt();
        int C = in.nextInt();

        int ABC = A * B * C;
        String ABCString = String.valueOf(ABC);

        Map<String, Integer> resultMap = new HashMap<>();
        for (int i = 0; i < 10; i++) {
            resultMap.put(String.valueOf(i), 0);
        }

        for (String s : ABCString.split("")) {
            resultMap.compute(s, (k, i) -> i + 1);
        }

        resultMap.forEach((key, value)->{
            System.out.println(value);
        });
    }
}
