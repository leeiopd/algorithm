package bronze.b_3052;

import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        Set<Integer> result = new HashSet<>();
        for (int i = 0; i < 10; i++) {
            int n = in.nextInt();
            result.add(n%42);
        }
        System.out.println(result.size());
    }
}
