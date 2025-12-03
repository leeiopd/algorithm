package bronze.b_2884;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int hh = in.nextInt();
        int mm = in.nextInt();

        //45분 일찍 알람 설정하기
        if(mm >= 45){
            mm -= 45;
        }else{
            mm += 15;
            if(hh > 0){
                hh -= 1;
            }else{
                hh = 23;
            }
        }

        System.out.println(hh + " " + mm);
    }
}
