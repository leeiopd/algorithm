package swea_2058;

import java.util.*;

public class Solution {
	static public void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int result = 0;
		int temp = 0;
		while (N > 0) {
			temp = N%10;
			N /= 10;
			result += temp;
		}
		
		System.out.println(result);
		
	}
}
