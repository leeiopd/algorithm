import java.util.*;
public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		
//		중간 35, 기말 45, 과제20
		String[] grade = {"A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"}; 
		
		for (int testCase = 1; testCase <= T; testCase++) {
			int N, K, A, B, C;
			double checkScore;
			int gradeNumPosition, gradeLimit;
			N = sc.nextInt();
			K = sc.nextInt();
			double[] scores = new double[N];
			gradeNumPosition = 0;
			
			checkScore = 0;
			
			for (int i = 0; i < N; i++) {
				A = sc.nextInt();
				B = sc.nextInt();
				C = sc.nextInt();
				
				scores[i] = (A*0.35) + (B*0.45) + (C*0.20);
				
				if (i + 1 == K) {
					checkScore = scores[i];
				}
			}
			
			Arrays.sort(scores);;
			
			gradeLimit = 0;
			for (int i = N-1; i >= 0; i--) {
				gradeLimit ++;
				
				if (scores[i] == checkScore) {
					System.out.println("#"+testCase+" "+grade[gradeNumPosition]);
					break;
				}
				
				
				if (gradeLimit == N/10) {
					gradeLimit = 0;
					gradeNumPosition ++;
				}
			}
			
		}
		sc.close();
	}
}
