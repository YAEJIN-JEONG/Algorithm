package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

//https://www.acmicpc.net/problem/18111
public class Q18111 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] str = reader.readLine().split(" ");
        int n = Integer.parseInt(str[0]);
        int m = Integer.parseInt(str[1]);
        int b = Integer.parseInt(str[2]);
        int[][] arr = new int[n][m];
        int min_value = 300;
        int max_value = 0;
        //가장 낮은 층에서 가장 높은층 까지 반복문을 돌리기 위해 값을 저장한다.
        for (int i=0; i<n; i++) {
            String[] input = reader.readLine().split(" ");
            for (int j=0; j<m; j++) {
                int value = Integer.parseInt(input[j]);
                arr[i][j] = value;
                if (value < min_value) {
                    min_value = value;
                }
                if (value > max_value) {
                    max_value = value;
                }
            }
        }

        //가장 낮은층에서 가장 높은층일때의 시간을 모두 구한다.
        int min_second = 100000000;
        int result = 0;
        for (int i=min_value; i<=max_value; i++) {
            int second = 0;
            int inven = b;
            for (int j=0; j<n; j++) {
                for (int k=0; k<m; k++) {
                    int now = arr[j][k] - i;
                    if (now < 0) {
                        second -= now;
                        inven += now;
                    } else {
                        second += now * 2;
                        inven += now;
                    }
                }
            }

            //인벤토리가 0 이상일때만 체크한다.
            if (inven >= 0) {
                if (min_second >= second) {
                    min_second = second;
                    result = i;
                }
            }
        }

        System.out.println(min_second + " " + result);
    }
}
