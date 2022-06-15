package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

//https://www.acmicpc.net/problem/1504
public class Q1504 {
    static List<List<Node>> list = new ArrayList<>();
    static int n;
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] str = reader.readLine().split(" ");
        n = Integer.parseInt(str[0]);
        int e = Integer.parseInt(str[1]);
        for (int i=0; i<n+1; i++) {
            list.add(new ArrayList<>());
        }

        for (int i=0; i<e; i++) {
            int[] ints = Arrays.stream(reader.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            list.get(ints[0]).add(new Node(ints[1], ints[2]));
            list.get(ints[1]).add(new Node(ints[0], ints[2]));
        }

        str = reader.readLine().split(" ");
        int u = Integer.parseInt(str[0]);
        int v = Integer.parseInt(str[1]);

        // u,v는 반드시 거쳐야 하는 정점이기에 1->u->v->n or 1->v->u->n 2가지의 경우중 더 작은 값을 출력시키면 된다.

        // result는 1->u->v->n
        int result = dijkstra(1)[u];
        result += dijkstra(u)[v];
        result += dijkstra(v)[n];

        // result2는 1->v->u->n
        int result2 = dijkstra(1)[v];
        result2 += dijkstra(v)[u];
        result2 += dijkstra(u)[n];

        // 더 작은값을 출력시키는데 최대값보다 클 경우 못가는 경우이기 때문에 -1 출력 그 외 정답 출력
        int result3 = Math.min(result, result2);
        if (result3 >= 200000000) {
            System.out.println(-1);
        } else {
            System.out.println(result3);
        }
    }

    private static int[] dijkstra(int start) {
        int[] distances = new int[n+1];
        // 간선의 개수 20만 거리 최대1000이라서 최대값 2억 Integer.MAX_VALUE 쓸 경우 위에 값 더하다가 초과됨
        Arrays.fill(distances, 200000000);
        Queue<Node> q = new PriorityQueue<>();
        distances[start] = 0;
        q.offer(new Node(start, 0));

        while (!q.isEmpty()) {
            Node node = q.poll();
            int index = node.index;
            int dis = node.distance;

            if (distances[index] < dis) {
                continue;
            }

            for (Node n : list.get(index)) {
                int cost = distances[index] + n.distance;

                if (distances[n.index] > cost) {
                    distances[n.index] = cost;
                    q.offer(new Node(n.index, cost));
                }
            }
        }

        return distances;
    }

    static class Node implements Comparable<Node> {
        int index, distance;

        public Node (int index, int distance) {
            this.index = index;
            this.distance = distance;
        }

        public int compareTo(Node node) {
            return this.distance - node.distance;
        }
    }
}
