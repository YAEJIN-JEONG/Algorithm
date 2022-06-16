package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

//https://www.acmicpc.net/problem/1865
// 음의 간선도 포함해서 벨만포드로 진행
public class Q1865 {
    static List<List<Node>> list;
    static int n;
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(reader.readLine());
        for (int i=0; i<t; i++) {
            String[] str = reader.readLine().split(" ");
            n = Integer.parseInt(str[0]);
            int m = Integer.parseInt(str[1]);
            int w = Integer.parseInt(str[2]);
            list = new ArrayList<>();
            for (int j=0; j<=n; j++) {
                list.add(new ArrayList<>());
            }

            // 일반 도로 양방향 가능
            for (int j=0; j<m; j++) {
                int[] ints = Arrays.stream(reader.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
                list.get(ints[0]).add(new Node(ints[1], ints[2]));
                list.get(ints[1]).add(new Node(ints[0], ints[2]));
            }
            // 웜홀 단방향
            for (int j=0; j<w; j++) {
                int[] ints = Arrays.stream(reader.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
                list.get(ints[0]).add(new Node(ints[1], -1 * ints[2]));
            }

            // 출발지점이 어디든 음의 간선 사이클만 찾으면 됨
            if (bellman(3)) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
    }

    private static boolean bellman(int start) {
        int[] distances = new int[n+1];
        // 출발지점이 어디든 사이클을 찾으려면 최대값을 주어진 문제에 넘지 않을 정도로 주어야한다.
        // 끊어져 있는 경우도 찾을수 있기 때문
        Arrays.fill(distances, 1000000000);
        distances[start] = 0;

        // n-1번 노드까지 돌면서 최단거리를 갱신하고 n번째에도 최단거리가 갱신되면 음의 사이클이 존재한다.
        for (int i=1; i<=n; i++) {
            for (int j=1; j<=n; j++) {
                for (Node node : list.get(j)) {
                    // 만약 최대값이 Integer.MAX_VALUE면, 뒤에 조건이 초과하기 때문에 에러가난다.
                    if (distances[node.index] > distances[j] + node.distance) {
                        distances[node.index] = distances[j] + node.distance;
                        // n번째에도 최단거리가 갱신되면 음의 사이클이 존재하므로 true 반환
                        if (i == n) {
                            return true;
                        }
                    }
                }
            }
        }
        return false;
    }

    static class Node {
        int index, distance;
        public Node(int index, int distance) {
            this.index = index;
            this.distance = distance;
        }
    }
}
