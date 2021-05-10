import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws Exception {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(bf.readLine());
		int L, U, X;
		String result;
		for (int tc = 1; tc <= T; tc++) {
			StringTokenizer st = new StringTokenizer(bf.readLine());
			L = Integer.parseInt(st.nextToken());
			U = Integer.parseInt(st.nextToken());
			X = Integer.parseInt(st.nextToken());
			
//			L���̻� U�� ������ ��� �ؾ� 
//			�̹��ִ� X�� ����
			
			if (X > U) {
				result = "-1";
			}
			else if (X < L) {
				result = String.valueOf((L-X));
			}
			else {
				result = "0";
			}
			
			System.out.println("#"+tc+" "+result);
		}
	}
}
