package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

//https://www.acmicpc.net/problem/9251
public class Q9251 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String str1 = reader.readLine();
        String str2 = reader.readLine();

        int[][] dp = new int[str1.length()+1][str2.length()+1];

        for (int i=0; i<str1.length(); i++) {
            for (int j=0; j<str2.length(); j++) {
                //같으면 왼쪽 아래 값 + 1
                if (str1.charAt(i) == str2.charAt(j)) {
                    dp[i+1][j+1] = dp[i][j] + 1;
                //다르면 왼쪽과 위 중 큰값
                } else {
                    dp[i+1][j+1] = Math.max(dp[i][j+1], dp[i+1][j]);
                }
            }
        }
        /*
        dp 배열 결과
        [0, 0, 0, 0, 0, 0, 0]
        [0, 0, 1, 1, 1, 1, 1]
        [0, 1, 1, 1, 2, 2, 2]
        [0, 1, 2, 2, 2, 3, 3]
        [0, 1, 2, 2, 2, 3, 3]
        [0, 1, 2, 2, 2, 3, 4]
        [0, 1, 2, 3, 3, 3, 4]
         */

        System.out.println(dp[str1.length()][str2.length()]);
    }
}
