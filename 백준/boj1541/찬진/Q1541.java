package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
public class Q1541 {
	
	public static void main(String[] args) throws Exception {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		
		String[] str = reader.readLine().split("-");
		
		for (int i=0; i<str.length; i++) {
			String[] st = str[i].split("\\+");
			int sum = 0;
			for (int j=0; j<st.length; j++) {
				sum += Integer.parseInt(st[j]);
			}
			str[i] = String.valueOf(sum);
 		}
		int sum = Integer.parseInt(str[0]);
		for (int i=1; i<str.length; i++) {
			sum -= Integer.parseInt(str[i]);
		}
		System.out.println(sum);
	}
}
