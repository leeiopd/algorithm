package bronze.b_8958;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int T = in.nextInt();

        for (int i = 0; i < T; i++) {
            String line = in.next();

            int result = 0;
            boolean isContinue = false;
            int continueCount = 0;
            for (String s : line.split("")) {
                if (s.equals("O")) {
                    if(isContinue){
                        continueCount++;
                        result += continueCount;
                    }else{
                        result += 1;
                        continueCount = 1;
                        isContinue = true;
                    }
                }else{
                    isContinue = false;
                    continueCount = 0;
                }
            }
            System.out.println(result);
        }
    }
}
