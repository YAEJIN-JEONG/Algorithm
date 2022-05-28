package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;

//https://www.acmicpc.net/problem/1676
public class Q1676 {
	
	public static void main(String[] args) throws Exception {
		
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(reader.readLine());
		int count = 0;
		while (n >= 5) {
			count += n / 5;
			n = n / 5;
		}
		System.out.println(count);
	}
}
