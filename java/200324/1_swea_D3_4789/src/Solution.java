import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Solution {
	public static void main(String[] args) throws IOException{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int T = Integer.parseInt(bf.readLine());
		
		for (int tc = 1; tc<= T; tc++) {
			String[] peoples = bf.readLine().split("");
			
			int cnt = 0;
			int result = 0;
			
			
			for (int i = 0; i < peoples.length; i++) {
				int people = Integer.parseInt(peoples[i]);
								
				if (cnt < i) {
					result += (i-cnt);
					cnt += (i-cnt);
				}
				cnt += people;
				
			}
			
			bw.write("#"+tc+" "+result+"\n");
			
			
		}
		bw.flush();
		bw.close();
	}
}
