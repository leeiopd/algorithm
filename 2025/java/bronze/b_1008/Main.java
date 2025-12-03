package bronze.b_1008;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        //두 정수 A와 B를 입력받은 다음, A/B를 출력하는 프로그램을 작성하시오.

        Scanner in = new Scanner(System.in);

        double a = in.nextDouble();
        double b = in.nextDouble();

        in.close();
        System.out.print(a / b);
    }
}
