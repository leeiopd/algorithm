package bronze.b_1152;

import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        String line = in.nextLine();
        if (line.equals(" ")) {
            System.out.println(0);
        } else {
            String[] words = line.strip().split(" ");
            System.out.println(words.length);
        }

    }
}