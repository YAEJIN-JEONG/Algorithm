package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

//https://www.acmicpc.net/problem/1932
public class Q1932 {
    static Integer[][] dp;
    static int[][] tri;
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        tri = new int[n][n];
        dp = new Integer[n][n];
        for (int i=0; i<n; i++) {
            int[] ints = Arrays.stream(reader.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            for (int j=0; j<ints.length; j++) {
                tri[i][j] = ints[j];
            }
        }
        dp[0][0] = tri[0][0];
        int result = 0;
        for (int i=0; i<n; i++) {
            // 마지막 열들의 dp를 구한다.
            dp[n-1][i] = check(n-1, i);
            // 마지막 열들의 최대값을 구한다
            result = Math.max(result, dp[n-1][i]);
        }
        System.out.println(result);
    }

    private static int check(int x, int y) {
        if (x == 0) {
            return dp[0][0];
        }
        // dp[x][y] == null인 경우 재귀로 값을 찾는다.
        if (dp[x][y] == null) {
            //y = 0이거나 x = y 는 한가지의 경우밖에 없다.
            if (y == 0) {
                dp[x][y] = check(x-1, y) + tri[x][y];
                return dp[x][y];
            } else if(x == y) {
                dp[x][y] = check(x-1, y-1) + tri[x][y];
                return dp[x][y];
            } else {
                // (x-1, y-1), (x-1, y)중에서 큰값과 원래 삼각형 배열의 값을 더한다.
                dp[x][y] = Math.max(check(x-1, y-1),check(x-1, y)) + tri[x][y];
                return dp[x][y];
            }
        } else {
            return dp[x][y];
        }
    }
}
