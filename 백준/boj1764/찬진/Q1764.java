package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

//https://www.acmicpc.net/problem/1764
public class Q1764 {
	
	public static void main(String[] args) throws Exception {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		String[] str = reader.readLine().split(" ");
		int n = Integer.parseInt(str[0]);
		int m = Integer.parseInt(str[1]);
		Set<String> set = new HashSet<String>();
		for (int i=0; i<n; i++) {
			set.add(reader.readLine());
		}
		List<String> list = new ArrayList<String>();
		int count = 0;
		for (int i=0; i<m; i++) {
			String name = reader.readLine();
			if (set.contains(name)) {
				list.add(name);
				count++;
			}
		}
		Collections.sort(list);
		System.out.println(count);
		for (String s : list) {
			System.out.println(s);
		}
		
	}

}
