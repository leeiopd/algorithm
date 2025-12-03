package bronze.b_30802;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        List<Integer> sizeMembers = new ArrayList<>();
        int memberTotal = 0;
        for (int i = 0; i < 6; i++) {
            int member = in.nextInt();
            sizeMembers.add(member);
            memberTotal += member;
        }

        int T = in.nextInt();
        int P = in.nextInt();

        int answer1 = 0;

        for (int s : sizeMembers) {
            answer1 += (s / T);
            if (s % T != 0) {
                answer1 += 1;
            }
        }

        System.out.println(answer1);

        int answer2 = memberTotal/P;
        int answer3 = memberTotal - (answer2*P);

        System.out.println(answer2 + " " + answer3);
    }
}
