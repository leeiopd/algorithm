import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int T = Integer.parseInt(bf.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			int K = Integer.parseInt(bf.readLine());
			
			ArrayList<Integer> nums = new ArrayList<Integer>();
			
			for (int i = 0; i < K; i++) {
				int num = Integer.parseInt(bf.readLine());
				
				if (num == 0) {
					nums.remove(nums.size()-1);
				}
				else {
					nums.add(num);
				}
			}
			
			int result = 0;
			
			for (int i = 0; i < nums.size(); i++) {
				result += nums.get(i);
			}
			
			bw.write("#"+tc+" "+result+"\n");
		}
		bw.flush();
		bw.close();
	}
}
