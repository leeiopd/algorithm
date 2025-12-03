package bronze.b_2920;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String input = in.nextLine().replace(" ", "");

        if (input.equals("12345678")) {
            System.out.println("ascending");
        } else if (input.equals("87654321")) {
            System.out.println("descending");
        } else {
            System.out.println("mixed");
        }
    }
}
