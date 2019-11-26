package swea_2019;

import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int temp = 1;
		System.out.print(temp+" ");
		for (int i=1; i<=N; i++) {
			temp *= 2;
			System.out.print(temp+" ");
		}
	}
}
