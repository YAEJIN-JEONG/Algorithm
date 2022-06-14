package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

//https://www.acmicpc.net/problem/1043
public class Q1043 {
    static int n;
    static boolean[][] connect;
    static boolean[] know;
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] str = reader.readLine().split(" ");
        n = Integer.parseInt(str[0]);
        int m = Integer.parseInt(str[1]);

        // 진실을 아는사람 배열
        know = new boolean[n+1];
        int[] input = Arrays.stream(reader.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        for (int i=1; i< input.length; i++) {
            know[input[i]] = true;
        }

        // 파티를 같이 참여한 기록이 있는지 연결시키는 2차원 배열
        connect = new boolean[n+1][n+1];
        // 각 파티와 참여한 사람을 저장시키는 리스트트
        List<int[]> list = new ArrayList<>();
        for (int i=0; i<m; i++) {
            int[] ints = Arrays.stream(reader.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            list.add(ints);
            for (int j=1; j<ints.length; j++) {
                for (int k=j; k<ints.length; k++) {
                    connect[ints[j]][ints[k]] = connect[ints[k]][ints[j]] = true;
                }
            }
        }

        // 진실을 알고있는 사람과 연결된 사람들도 진실을 알기 때문에 dfs를 통해 모두 확인
        for (int i=1; i<=n; i++) {
            if (know[i]) {
                dfs(i);

            }
        }

        // 각 파티에 진실을 알고 있는 사람이 없을때 count++
        int count = 0;
        loop: for (int[] j : list) {
            for (int i=1; i<j.length; i++) {
                if (know[j[i]]) {
                    continue loop;
                }
            }
            count++;
        }
        System.out.println(count);
    }
    private static void dfs(int start) {
        for (int i=1; i<=n; i++) {
            if (connect[start][i] && !know[i]) {
                know[i] = true;
                dfs(i);
            }
        }
    }
}
