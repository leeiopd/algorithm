import java.util.Scanner;

public class Solution {

		public static void main(String[] args) {
			Scanner sc = new Scanner(System.in);
			
			int T = sc.nextInt();
			int N, sec, command, commandSpeed, result, totalSpeed;
			for (int testCase = 1; testCase<=T; testCase++) {
				N = sc.nextInt();
				result = 0;
				totalSpeed = 0;
				for (int i = 0; i < N; i++) {
					command = sc.nextInt();
					if (command != 0)	{
						commandSpeed = sc.nextInt();
						if (command == 1) {
							totalSpeed += commandSpeed; 
						}
						else {
							if (totalSpeed - commandSpeed < 0) {
								totalSpeed = 0;
							}
							else {								
								totalSpeed -= commandSpeed;
							}
						}
					}
					
					result += totalSpeed;
					
				}
				System.out.println("#"+testCase+" "+result);
			}
		}
}
