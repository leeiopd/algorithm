import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		int T = 10;

		for (int tc = 1; tc <= 10; tc++) {
			int N = Integer.parseInt(bf.readLine());
			StringTokenizer passLine = new StringTokenizer(bf.readLine());
			ArrayList<String> passList = new ArrayList<String>();

			for (int i = 0; i < N; i++) {
				passList.add(passLine.nextToken());
			}

			int orderN = Integer.parseInt(bf.readLine());
			StringTokenizer orderLine = new StringTokenizer(bf.readLine());
			
			String order;
			int readN = 0;
			int position;
			String orderTemp;

			for (int i = 0; i < orderN; i++) {
				order = orderLine.nextToken();

				if (order.equals("I")) {
					position = Integer.parseInt(orderLine.nextToken());
					readN = Integer.parseInt(orderLine.nextToken());

					for (int j = 0; j  < readN; j++) {
						orderTemp = orderLine.nextToken();

						passList.add(position+j, orderTemp);
					}
				}
				
				else if(order.equals("D")) {
					position = Integer.parseInt(orderLine.nextToken());
					readN = Integer.parseInt(orderLine.nextToken());

					for (int j = 0; j  < readN; j++) {
						passList.remove(position+1);
					}
				}
				
				else if(order.equals("A")) {
					readN = Integer.parseInt(orderLine.nextToken());

					for (int j = 0; j  < readN; j++) {
						orderTemp = orderLine.nextToken();

						passList.add(orderTemp);
					}
				}
			}
			
			
			System.out.print("#"+tc);
			
			for (int i = 0; i < 10; i++) {
				System.out.print(" "+passList.get(i));
			}
			System.out.println();
		}
	}
}