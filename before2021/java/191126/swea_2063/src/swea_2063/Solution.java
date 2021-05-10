package swea_2063;

import java.util.*;
public class Solution {
	static public void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		
		int arr[] = new int[N];
		int tmp = 0;
		for (int i=0; i < N; i++) {
			tmp = sc.nextInt();
			arr[i] = tmp;
		}
		Arrays.sort(arr);
		System.out.println(arr[N/2]);
	}
}
