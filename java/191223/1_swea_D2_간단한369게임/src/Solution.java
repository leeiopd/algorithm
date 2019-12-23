import java.util.*;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		String textNum;
		
		for (int i = 1; i <= N; i++) {
			textNum = String.valueOf(i);
			
			for (int j = 0; j < textNum.length(); j++) {
				if (textNum.charAt(j) == "3" || textNum.charAt(j) == "6" || textNum.charAt(j) == "9") {
					textNum.charAt(j) = "-";
				}
			}
			
		}
		
		
		

	}
}
