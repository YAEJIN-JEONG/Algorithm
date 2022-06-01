package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

//https://www.acmicpc.net/problem/2579
public class Q2579 {
	public static void main(String[] args) throws Exception {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(reader.readLine());
		int[] arr = new int[n+1];
		for (int i=1; i<=n; i++) {
			arr[i] = Integer.parseInt(reader.readLine());
		}
		
		int[] dp = new int[n+1];
		dp[1] = arr[1];
		if (n > 1) {
			dp[2] = arr[1] + arr[2];			
		}
		
		for (int i=3; i<=n; i++) {
			dp[i] = Math.max(dp[i-2], dp[i-3] + arr[i-1]) + arr[i];
		}
		System.out.println(dp[n]);
	}
}
