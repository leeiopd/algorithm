import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Solution {
	public static void main(String[] args) throws Exception{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(bf.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			int peopleN = Integer.parseInt(bf.readLine());
			
			String result = "#"+tc+" ";
			
			for (int i = 0; i < peopleN; i++) {
				result += "1/"+peopleN+" ";
			}
			
			System.out.println(result);
		}
	}
}
