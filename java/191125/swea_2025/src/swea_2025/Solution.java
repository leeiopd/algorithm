package swea_2025;

import java.util.*;

public class Solution {
	static public void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int result = 0;
		for (int i=1; i <= N; i++) {
			result += i;
		}
		System.out.println(result);
	}
}
