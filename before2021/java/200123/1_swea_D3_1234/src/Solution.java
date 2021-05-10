import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

		for (int tc = 1; tc <= 10; tc++) {
			StringTokenizer st = new StringTokenizer(bf.readLine());

			int N = Integer.parseInt(st.nextToken());

			ArrayList<String> nums = new ArrayList<String>();
			
			String temp = st.nextToken();
			
			for (int i = 0; i < temp.length(); i++) {
				nums.add(String.valueOf(temp.charAt(i)));
			}
			boolean flag = true;
			
			while (flag) {
				flag = false;
				for (int i= 0; i < nums.size()-1; i++) {
					if (nums.get(i).equals(nums.get(i+1))) {
						nums.remove(i);
						nums.remove(i);
						flag = true;
						break;
					}
					
					
				}
			}
			String result = "";
			
			for (int i = 0; i < nums.size(); i++) {
				result += nums.get(i);
			}
			System.out.println("#"+tc+" "+result);

		}
	}
}
