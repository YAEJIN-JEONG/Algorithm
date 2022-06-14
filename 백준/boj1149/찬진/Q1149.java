package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

//https://www.acmicpc.net/problem/1149
public class Q1149 {
    static int n;
    static int[][] cost;
    static int[][] visited;
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(reader.readLine());
        // 집의 RGB색칠 비용 저장
        cost = new int[n][3];
        // 각 도착 색깔까지의 비용 저장
        visited = new int[n][3];
        for (int i=0; i<n; i++) {
            int[] ints = Arrays.stream(reader.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            cost[i] = ints;
        }

        // 0번째 집 비용 저장
        visited[0][0] = cost[0][0];
        visited[0][1] = cost[0][1];
        visited[0][2] = cost[0][2];

        int result = Integer.MAX_VALUE;
        for (int i=0; i<3; i++) {
            //시작 색깔 지정해서 더 작은값 저장
            result = Math.min(result ,costRe(i, n-1));
        }

        System.out.println(result);
        for (int[] i : visited) {
            System.out.println(Arrays.toString(i));
        }
    }
    private static int costRe(int start, int depth) {

        // 값이 저장되어 있지 않으면 재귀로 깊이-1 호출 이때 조건은 붙어있는 집은 같은 색깔이면 안된다.
        if (visited[depth][start] == 0) {
            if (start == 0) {
                visited[depth][start] = Math.min(costRe(1, depth - 1), costRe(2, depth - 1)) + cost[depth][0];
            } else if (start == 1) {
                visited[depth][start] = Math.min(costRe(0, depth - 1), costRe(2, depth - 1)) + cost[depth][1];
            } else {
                visited[depth][start] = Math.min(costRe(1, depth - 1), costRe(0, depth - 1)) + cost[depth][2];
            }
        }
        return visited[depth][start];
    }
}
