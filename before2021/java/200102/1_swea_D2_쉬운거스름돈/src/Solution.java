import java.util.*;
public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();
		int N, a, b, c, d, e, f, g, h;
		//		a 5만
		//		b 만
		//		c 5천
		//		d 천
		//		e 5백
		//		f 백
		//		g 5십
		//		h 십

		for (int testCase = 1; testCase <= T; testCase++) {
			N = sc.nextInt();
			a = b = c = d = e = f = g = h = 0;
			while (N != 0) {
				if (N >= 50000) {
					a += (N/50000);
					N %= 50000;
				}
				else if (N >= 10000) {
					b+= (N/10000);
					N %= 10000;
				}
				else if (N >= 5000) {
					c += (N/5000);
					N %= 5000;
				}
				else if (N >= 1000) {
					d+= (N/1000);
					N %= 1000;
				}
				else if (N >= 500) {
					e+=(N/500);
					N %= 500;
				}
				else if (N >= 100) {
					f+=(N/100);
					N %= 100;
				}
				else if (N >= 50) {
					g+=(N/50);
					N %= 50;
				}
				else {
					h+=(N/10);
					N /= 10;
				}
			}
			System.out.println("#"+testCase+"\n"+a+" "+b+" "+c+" "+d+" "+e+" "+f+" "+g+" "+h);
		}
		sc.close();
	}
}
