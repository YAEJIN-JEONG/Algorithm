package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;

//https://www.acmicpc.net/problem/1931
public class Q1931 {
	
	public static void main(String[] args) throws Exception {
		
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(reader.readLine());
		int[][] time = new int[n][2];
		for (int i=0; i<n; i++) {
			String[] str = reader.readLine().split(" ");
			time[i][0] = Integer.parseInt(str[0]);
			time[i][1] = Integer.parseInt(str[1]);
		}
		
		Arrays.sort(time, new Comparator<int[]>() {

			@Override
			public int compare(int[] o1, int[] o2) {
				
				if (o1[1] == o2[1]) {
					return o1[0] - o2[0];
				}
				
				return o1[1] - o2[1];
			}});
		
		int a = time[0][1];
		int count = 1;
		for (int i=1; i<n; i++) {
			if (a <= time[i][0]) {
				a = time[i][1];
				count++;
			}
		}
		System.out.println(count);
		
	}

}
