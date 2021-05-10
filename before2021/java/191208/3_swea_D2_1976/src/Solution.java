import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();
		int hourA, minA, hourB, minB, hourResult, minResult;
		for (int testCase = 1; testCase <= T; testCase++) {
			hourA = sc.nextInt();
			minA = sc.nextInt();
			hourB = sc.nextInt();
			minB = sc.nextInt();
			
			hourResult = hourA + hourB;
			
			if (hourResult >= 12) {
				hourResult -= 12;
			}
			
			minResult = minA + minB;
			
			while (minResult >= 60) {
				minResult -= 60;
				hourResult ++;
			}
			
			System.out.println("#"+testCase+" "+hourResult+" "+minResult);
			
			
			
		}
		sc.close();
	}
}
