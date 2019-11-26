package swea_2056;

import java.util.*;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		int N = 0;
		int year = 0;
		int month = 0;
		int day= 0;
		boolean flag = false;
		for (int testCase = 1; testCase <= T; testCase++) {
			flag = false;
			N = sc.nextInt();
			day = N%100;
			N /= 100;
			month = N%100;
			N /= 100;
			year = N;
			if (year < 1000) {
				flag = true;
			}
			
			if (1<= month && month <= 12 ) {
				if (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) {
					if (1<= day && day<=31) {
						if (flag) {
							System.out.print("#"+testCase+" "+year+"/"+month+"/");
							System.out.print("0");
							System.out.print(day+"\n");
						}
						else {
							System.out.println("#"+testCase+" "+year+"/"+month+"/"+day);
						}
					}
					else {
						System.out.println("#"+testCase+" -1");
					}
				}
				else if(month == 4 || month == 6 || month==8 || month == 9 || month == 11) {
					if (1<= day && day <= 30) {
						if (flag) {
							System.out.print("#"+testCase+" "+year+"/"+month+"/");
							System.out.print("0");
							System.out.print(day+"\n");
						}
						else {
							System.out.println("#"+testCase+" "+year+"/"+month+"/"+day);
						}
					}
					else {
						System.out.println("#"+testCase+" -1");
					}
				}
				else {
					if (1<= day && day <= 28) {
						if (flag) {
							System.out.print("#"+testCase+" "+year+"/"+month+"/");
							System.out.print("0");
							System.out.print(day+"\n");
						}
						else {
							System.out.println("#"+testCase+" "+year+"/"+month+"/"+day);
						}
					}
					else {
						System.out.println("#"+testCase+" -1");
					}
				}
			}
			else {
				System.out.println("#"+testCase+" -1");
			}
			
			
		}
	}
}
