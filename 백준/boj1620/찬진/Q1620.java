package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Q1620 {
	
	public static void main(String[] args) throws Exception {
		
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		
		String[] str = reader.readLine().split(" ");
		int n = Integer.parseInt(str[0]);
		int m = Integer.parseInt(str[1]);
		
		Map<String, String> map = new HashMap<String, String>();
		Map<String, String> mapTwo = new HashMap<String, String>();
		for (int i=1; i<=n; i++) {
			String s = reader.readLine();
			map.put(i+"", s);
			mapTwo.put(s, i+"");
		}
		
		
		for (int i=0; i<m; i++) {
			String input = reader.readLine();
			if (map.get(input) == null) {
				System.out.println(mapTwo.get(input));
			} else {
				System.out.println(map.get(input));
			}
		}
		
	}
}
