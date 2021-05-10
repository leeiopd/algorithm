import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int T = Integer.parseInt(bf.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			String str = " ";
			str += bf.readLine();
			
			int[] nums = new int[str.length()];
			
			int H = Integer.parseInt(bf.readLine());
			
			StringTokenizer st = new StringTokenizer(bf.readLine());
			
			for (int i = 0; i < H; i++) {
				int j = Integer.parseInt(st.nextToken());
				
				nums[j]++;
			}
			
			bw.write("#"+tc);
			
			
			for (int i = 0; i < str.length(); i++) {
				bw.write(String.valueOf(str.charAt(i)));
				for (int j = 1; j <= nums[i]; j++) {
					bw.write("-");
				}
			}
			bw.write("\n");
		}
		bw.flush();
		bw.close();
	}
}
