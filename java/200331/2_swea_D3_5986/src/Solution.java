import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class Solution {
	static boolean[] Num;
	static ArrayList<Integer> PrimeNum;
	static int result;
	static int L;
	
	public static void main(String[] args) throws IOException{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int T = Integer.parseInt(bf.readLine());

		Num = new boolean[1000];
		PrimeNum = new ArrayList<Integer>();

		for(int i = 2; i <= 999; i++) {
			Num[i] = true;
		}

		for(int i = 2; i <= 999; i++) {
			if (!Num[i]) {
				continue;
			}
			PrimeNum.add(i);
			int cnt = 2;
			
			while(true) {
				if(i*cnt > 999) {
					break;
				}
				Num[i*cnt] = false;
				cnt++;
			}
		}
		
		L = PrimeNum.size();
		

		for (int tc = 1; tc<=T; tc++) {
			int N = Integer.parseInt(bf.readLine());
			result = 0;
			
			fnc(0, N, 0, 0);
			
			bw.write("#"+tc+" "+result+"\n");

		}
		bw.flush();
		bw.close();

	}

	static void fnc(int cnt, int N, int add, int addN) {
		if (addN == 3) {
			if (add == N) {				
				result++;
			}
			return;
		}
		
		for (int i = cnt; i < L; i++) {
			if(add + PrimeNum.get(i) > N) {
				return;
			}
			fnc(i, N, add+PrimeNum.get(i), addN+1);
		}
		
	}

}
