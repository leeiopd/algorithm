package swea_2070;

import java.util.*;

public class Solution {
	static public void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		
		for (int testCase=1; testCase <= T; testCase++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			
			System.out.print("#"+testCase);
			
			if (a > b) {
				System.out.print(" >\n");
			}
			else if(a<b) {
				System.out.print(" <\n");
			}
			else {
				System.out.print(" =\n");
			}
		}
	}
}
