import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		int N, input, range, result;
		for (int testCase = 1; testCase <= T; testCase++) {
			N = sc.nextInt();
			range = 100000;
			result = 0;
			for (int i = 0; i < N; i++) {
				input = sc.nextInt();
				
				if (input < 0) {
					input = -input;
				}
				
				if (range > input) {
					range = input;
					result = 1;
				}
				else if (range == input) {
					result++;
				}
			}
			System.out.println("#"+testCase+" "+range+" "+result);
		}
		sc.close();
	}
}
