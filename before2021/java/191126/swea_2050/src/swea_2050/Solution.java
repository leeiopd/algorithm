package swea_2050;

import java.util.*;

public class Solution {
	static public void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String text = sc.nextLine();
		int N = 65; // �ƽ�Ű �ڵ�
		int tmp = 0;
		for (int i=0; i < text.length(); i++) {
			tmp = text.charAt(i);
			System.out.print(tmp%N+1+" ");
		}
	}
}
