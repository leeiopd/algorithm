import java.util.*;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		String textNum;
		char temp;
		int clapCnt;

		for (int i = 1; i <= N; i++) {
			textNum = String.valueOf(i);
			clapCnt = 0; 

			for (int j = 0; j < textNum.length(); j++) {
				temp = textNum.charAt(j);
				//				"" 와 ''의 차이는 문자열과 문자의 차이 이다
				if (temp == '3'|| temp == '6'|| temp == '9') {
					clapCnt ++;
				}

			}
			if (clapCnt > 0) {
				for (int k = 0; k < clapCnt; k++) {
					System.out.print("-");
				}
			}
			else {
				System.out.print(textNum);
			}
			System.out.print(" ");
		}
		sc.close();	
	}
}