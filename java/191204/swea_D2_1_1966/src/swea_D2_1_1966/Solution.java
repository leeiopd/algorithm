package swea_D2_1_1966;

import java.util.*;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();
		int N;
		for (int testCase = 1; testCase <= T; testCase++) {
			N = sc.nextInt();
			
			int numbers[] = new int[N];
			
			for (int i = 0; i < N; i++) {
				numbers[i] = sc.nextInt();
			}
			Arrays.parallelSort(numbers);
			
			System.out.print("#"+testCase+" ");
			for (int j = 0; j < N; j++) {
				System.out.print(numbers[j]+" ");
			}
			System.out.print("\n");
		}
	}
}
