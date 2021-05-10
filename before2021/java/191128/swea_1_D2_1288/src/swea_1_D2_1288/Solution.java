package swea_1_D2_1288;

import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		int cnt;
		int N;
		int temp;
		
		
		for (int testCase = 1; testCase <= T; testCase++) {
			boolean Check[] = new boolean[10];
			N  = sc.nextInt();
			cnt  = 0;
			while (!(Check[0]&&Check[1]&&Check[2]&&Check[3]&&Check[4]&&Check[5]&&Check[6]&&Check[7]&&Check[8]&&Check[9])){
				cnt++;
				temp = N * cnt;
				while (temp != 0) {
					Check[temp%10] = true;
					temp = temp/10;
				}
			}
			System.out.println("#"+testCase+" "+N*cnt);
		}
		sc.close();
	}
}
