package swea_2068;

import java.util.Arrays;
import java.util.Scanner;

public class Solution {
	static public void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		int arr[] = new int[10];
		for (int testCase = 1; testCase <= T; testCase++) {
			for (int i=0; i<10; i++) {
				arr[i] = sc.nextInt();
			}
			Arrays.sort(arr);
			
			System.out.println("#"+testCase+" "+arr[9]);
		}
	}
}
