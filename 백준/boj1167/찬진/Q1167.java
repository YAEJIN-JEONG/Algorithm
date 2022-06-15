package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

//https://www.acmicpc.net/problem/1167
public class Q1167 {

    static int n;
    static List<List<int[]>> list = new ArrayList<>();
    static boolean[] visited;
    static int result;
    static int node;
    public static void main(String[] args) throws IOException {
        // 다익스트라로 풀면 시간초과남 dfs로 진행
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(reader.readLine());
        // 인접행렬로 하면 메모리 초과, 따라서 인접리스트로 진행
        for (int i=0; i<=n; i++) {
            list.add(new ArrayList<>());
        }
        visited = new boolean[n+1];
        for (int i=0; i<n; i++) {
            int[] ints = Arrays.stream(reader.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            for (int j=1; j<ints.length-1; j+=2) {
                list.get(ints[0]).add(new int[] {ints[j], ints[j+1]});
            }
        }
        // 어느 곳에서 진행해도 가장 거리가 먼 노드는 동일하다. 임의의 숫자 1로 가장 먼 노드를 구한다.
        visited[1] = true;
        dfs(1, 0);

        visited = new boolean[n+1];
        visited[node] = true;
        // 가장 먼 노드에서 각 노드까지의 거리중 가장 큰 값을 찾는다.
        dfs(node, 0);
        System.out.println(result);

    }
    private static void dfs(int start, int sum) {
        if (sum > result) {
            result = sum;
            // 거리가 먼 노드를 저장
            node = start;
        }
        for (int[] l : list.get(start)) {
            if (!visited[l[0]]) {
                visited[l[0]] = true;
                dfs(l[0], sum+l[1]);
            }
        }
    }
}
