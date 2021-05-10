package swea_1_D2_1989;

import java.util.*;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		String text;
		String temp;
		for (int testCase = 1; testCase <= T; testCase++) {
			text = sc.next();
			temp = "";
			
			for (int i = text.length()-1; i > -1; i--) {
				temp += text.charAt(i);
			}
			if (text.equals(temp)) {
				System.out.println("#"+testCase+" 1");
			}
			else {
				System.out.println("#"+testCase+" 0");
			}
		}
		
	}
}
