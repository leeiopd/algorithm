package swea_2056;

import java.util.*;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int daysOfMonth[] = {31,28,31,30,31,30,31,31,30,31,30,31};
		int T = sc.nextInt();
		
		String result;
		
		int monthInt;
		int dayInt;
		
		String year;
		String month;
		String day;
		
		for (int testCase = 1; testCase <= T; testCase++) {
			String N = sc.next();
			year = N.substring(0, 4);
			month = N.substring(4, 6);
			day = N.substring(6, 8);
			monthInt = Integer.valueOf(month);
			dayInt = Integer.valueOf(day);
			result = "-1";
			if (1<=monthInt && monthInt<=12) {
				if (1<= dayInt && dayInt <= daysOfMonth[monthInt-1]) {
					result = year + "/"+month+"/"+day;
				}
			}
			
			System.out.println("#"+testCase+" "+result);
			
		
		}
	}
}