import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int MAX = 1000000;
		boolean[] a = new boolean[MAX+1];
		a[0] = a[1] = true;
		for(int i = 2; i <= Math.sqrt(MAX); i++) {
			if( a[i] ) continue;
			for(int j=i*2; j<=MAX; j+=i) a[j] = true;
		}
		
		for(int i=2; i<=MAX; i++) {
			if( !a[i] ) {
				bw.write(i+" ");
			}
		}
		bw.flush();
		bw.close();
		
	}
}
