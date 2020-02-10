import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		for (int tc = 1; tc <= 10; tc++) {
			int N = Integer.parseInt(bf.readLine());

//			ºôµù ³ôÀÌ ¹è¿­
			String[] list = bf.readLine().split(" ");
			int result = 0;

//			3¹ø Ä­ºÎÅÍ 98¹ø Ä­ ±îÁö Á¶È¸
			for (int i = 2; i < N-2; i++) {
				
//				±âÁØÁ¡ Ä­
				int position = Integer.parseInt(list[i]);

				
//				¿À¸¥ÂÊ 2Ä­, ¿ÞÂÊ 2Ä­ ³ôÀÌ
				int r1 = Integer.parseInt(list[i+1]);

				if (r1 >= position) {
					continue;
				}
				
				int max = r1;
				

				int r2 = Integer.parseInt(list[i+2]);

				if (r2 >= position) {
					continue;
				}
				if (max < r2) {
					max = r2;
				}
				

				int l1 = Integer.parseInt(list[i-1]);

				if (l1 >= position) {
					continue;
				}
				if (max < l1) {
					max = l1;
				}
				

				int l2 = Integer.parseInt(list[i-2]);

				if (l2 >= position) {
					continue;
				}
				if (max < l2) {
					max = l2;
				}
				
				result += (position-max);
			}
			
			bw.write("#"+tc+" "+result+"\n");
		}
		bw.flush();
		bw.close();
	}
}
