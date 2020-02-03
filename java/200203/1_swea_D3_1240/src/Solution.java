import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

		HashMap<String, Integer> hm = new HashMap<String, Integer>();
		hm.put("0001101", 0);
        hm.put("0011001", 1);
        hm.put("0010011", 2);
        hm.put("0111101", 3);
        hm.put("0100011", 4);
        hm.put("0110001", 5);
        hm.put("0101111", 6);
        hm.put("0111011", 7);
        hm.put("0110111", 8);
        hm.put("0001011", 9);
		
		
		int T = Integer.parseInt(bf.readLine());

		for (int tc = 1; tc <= 10; tc++) {
			StringTokenizer st = new StringTokenizer(bf.readLine());
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());

			String pass = "";
			int i;
			for (i = 0; i<N; i++) {
				if (bf.readLine().indexOf("1") != -1) {
					pass = bf.readLine();
					break;
				}
			}
			
			for (int j = i+2; j<N; j++) {
				bf.readLine();
			}
			
			int odd = 0;
			int even = 0;
			int checkCode = 0;
			int result = 0;
			
			for (int x = pass.length()-1; x >= 0; x--) {
				if (pass.charAt(x) == '1') {
					int j = x-55;
					for (int k = 0; k<8; k++) {
						String num = pass.substring(j+k*7, j+(k+1)*7);
						result += hm.get(num);
						
						if (k==7) {
							checkCode = hm.get(num);
							break;
						}
						if ((k+1)%2 == 0) {
							even += hm.get(num);
						}
						else {
							odd += hm.get(num);
						}
						
					}
					break;
				}
			}
			
			int check = odd*3 + even + checkCode;
			
			if (check % 10 == 0) {
				System.out.println("#"+tc+" "+result);
			}
			else {
				System.out.println("#"+tc+" "+0);
			}
			
		}
	}
}
