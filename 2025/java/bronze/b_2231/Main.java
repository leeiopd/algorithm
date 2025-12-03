package bronze.b_2231;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
//        N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미
//        245의 분해합은 256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자가 된다.
//        arr[245] = 256
//
//        N = 256 -> 245
//        N = 216 -> 198
        Scanner in = new Scanner(System.in);
        int target = in.nextInt();

        for (int i = 1; i < target ; i++) {
            String nums = String.valueOf(i);

            int added = i;
            for (int j = 0; j < nums.length(); j++) {
                added += Integer.parseInt(String.valueOf(nums.charAt(j)));
            }

            if(added == target){
                System.out.println(i);
                return;
            }
        }
        System.out.println("0");

    }
}