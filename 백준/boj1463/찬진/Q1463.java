package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Q1463 {
	
	
	public static void main(String[] args) throws Exception {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(reader.readLine());
		int[] dp = new int[n+1];
		dp[0] = dp[1] = 0;
		for (int i=2; i<=n; i++) {
			dp[i] = dp[i-1] + 1;
			if (i % 2 == 0) {
				dp[i] = Math.min(dp[i], dp[i/2]+1);
			}
			if (i % 3 == 0) {
				dp[i] = Math.min(dp[i], dp[i/3]+1);
			}
		}
		System.out.println(dp[n]);
	}
}
