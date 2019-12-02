package swea_1_D2_2007;

import java.util.*;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();
		int cnt;
		String text, temp;
		boolean flag;

		for (int testCase = 1; testCase <= T; testCase++) {
			text = sc.next();
			cnt = 1;
			while (cnt < 10) {
				flag = true;
				temp = "";
				for (int i = 0; i < cnt; i++) {
					temp += text.charAt(i);
				}
				
				for (int j = cnt; j < cnt*2; j++) {
					if (temp.charAt(j-cnt) != text.charAt(j)) {
						flag = false;
						break;
					}
				}
				
				
				if (flag == true) {
					break;
				}
				cnt++;
			}
			System.out.println("#"+testCase+" "+cnt);
		}
		sc.close();
	}
}
