import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Solution2 {
//	throws IOException - BufferedReader�� �޼ҵ��� readLine()�� IOException�� �߻� ��Ŵ
	public static void main(String[] args) throws IOException {
//		�Է� ��� ����
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
//		��� ��� ����
		StringBuilder builder = new StringBuilder();
		
//		���� ��� �迭
		String[] grade = {"A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"}; 
		
//		�׽�Ʈ ���̽��� ������ "10"�� string���� �޾� ���� ������
//		int�� ��ȯ �޼ҵ带 ���
		int tc = Integer.parseInt(bf.readLine());
		
		for (int i = 1; i <= tc; i++) {
			
//			"�� �ο���, Ư�� �л� ��ȣ ��" �� �� �Է� ��ü�� �о� ��
			String str = bf.readLine();
			
//			�о�� ������ " " ������ ��� st�� ����
			StringTokenizer st = new StringTokenizer(str, " ");
			
//			nextToken() - �޼ҵ带 �̿��Ͽ� ������ ���� ���ʷ� �о��
			int studentNum[] = new int[Integer.parseInt(st.nextToken())];
			int checkNum = Integer.parseInt(st.nextToken());
			
			
			int A, B, C;
			
//			key�� �̿��Ͽ� value�� �о� ���� ���� HashMap �ڷᱸ���� ����
			HashMap<Integer, Double> scoreMap = new HashMap<Integer, Double>();
			
			for(int j = 0; j < studentNum.length; j++) {
				str = bf.readLine();
				st = new StringTokenizer(str, " ");
				
				A = Integer.parseInt(st.nextToken());
				B = Integer.parseInt(st.nextToken());
				C = Integer.parseInt(st.nextToken());
				
//				scoreMap �� �л���ȣ�� key�� ������ value�� ������ ����
				scoreMap.put((j+1), A*0.35+B+0.45+C*0.2);
			}
			
//			�����ϱ� ���� ArrayList �� scoreMap�� value������ �̾� ����
			ArrayList<Double> list = new ArrayList<Double>(scoreMap.values());
//			����
			Collections.sort(list);
//			������
			Collections.reverse(list);
			
//			��� �л��� ������ ���° ���� Ȯ��
//			1. �л��� ���� ã��
//			2. ������ index Number ã��
			int index = list.indexOf(scoreMap.get(checkNum));
			
//			builder ������ string�� append() �޼ҵ带 �̿��Ͽ� �߰�
			builder.append("#").append(i).append(" ").append(grade[index/(studentNum.length/10)]).append("\n");
		}
		System.out.println(builder);
	}
}
