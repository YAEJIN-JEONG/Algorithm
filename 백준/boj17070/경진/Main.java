package boj17070;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    static int n;
    static int[][] arr;
    static int answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        arr = new int[n][n];

        for (int i=0; i<n; i++) {
            String[] line = br.readLine().split(" ");
            for (int j = 0; j < n; j++)
                arr[i][j] = Integer.parseInt(line[j]);
        }
        // 행, 열, 방향
        // 방향 = 가로: 0, 세로: 1, 대각선: 2
        backtrack(0, 1, 0);
        System.out.println(answer);
    }

    public static void backtrack(int x, int y, int d) {
        if (x == n - 1 && y == n - 1)
            answer++;
        else {
            int[][] steps = {{0, 1}, {1, 0}, {1, 1}};

            for (int i=0; i<steps.length; i++) {
                // 현재 방향에 따라 이동할 수 없는 경우는 스킵
                if ((d == 0 && i == 1) || (d == 1 && i == 0))
                    continue;

                int nx = x + steps[i][0];
                int ny = y + steps[i][1];

                if (nx >= 0 && nx < n && ny >= 0 && ny < n && arr[nx][ny] == 0) {
                    // 대각선 방향이면 벽 추가 확인
                    if (i == 2 && (arr[nx - 1][ny] != 0 || arr[nx][ny - 1] != 0))
                        continue;
                    backtrack(nx, ny, i);
                }
            }
        }
    }
}
