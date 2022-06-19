package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

//https://www.acmicpc.net/problem/1967
public class Q1967 {

    static List<List<Node>> list = new ArrayList<>();
    static boolean[] visited;
    static int result;
    static int result_index;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        visited = new boolean[n+1];
        for (int i=0; i<n+1; i++) {
            list.add(new ArrayList<>());
        }
        for (int i=0; i<n-1; i++) {
            int[] input = Arrays.stream(reader.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            list.get(input[0]).add(new Node(input[1], input[2]));
            list.get(input[1]).add(new Node(input[0], input[2]));
        }
        // 1번 노드에서 가장 가중치가 큰 노드를 dfs를 통해 찾는다
        visited[1] = true;
        dfs(1, 0);
        visited = new boolean[n+1];
        // 가장 가중치가 큰 노드에서 dfs를 다시해서 최대값을 찾는다
        visited[result_index] = true;
        dfs(result_index, 0);
        System.out.println(result);
    }
    private static void dfs(int start, int sum) {
        if (result < sum) {
            result = sum;
            result_index = start;
        }
        for (Node n : list.get(start)) {
            int index = n.index;
            int dis = n.distance;
            if (!visited[index]) {
                visited[n.index] = true;
                dfs(n.index, sum + dis);
            }
        }
    }
    static class Node {
        int index, distance;
        public Node(int index, int distance) {
            this.index = index;
            this.distance = distance;
        }
    }
}
