package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

//https://www.acmicpc.net/problem/1753
public class Q1753 {

    static List<List<Node>> list = new ArrayList<>();
    static int[] distances;
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] str = reader.readLine().split(" ");
        int v = Integer.parseInt(str[0]);
        int e = Integer.parseInt(str[1]);
        int k = Integer.parseInt(reader.readLine());
        distances = new int[v+1];
        for (int i=0; i<v+1; i++) {
            list.add(new ArrayList<>());
        }

        Arrays.fill(distances, Integer.MAX_VALUE);

        for (int i=0; i<e; i++) {
            int[] input = Arrays.stream(reader.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            list.get(input[0]).add(new Node(input[1], input[2]));
        }

        dijkstra(k);

        for (int i=1; i<distances.length; i++) {
            System.out.println(distances[i] == Integer.MAX_VALUE ? "INF" : distances[i]);
        }

    }

    private static void dijkstra(int start) {
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

                if (cost < distances[n.index]) {
                    distances[n.index] = cost;
                    q.offer(new Node(n.index, cost));
                }
            }
        }
    }
    static class Node implements Comparable<Node> {
        int index, distance;
        public Node(int index, int distance) {
            this.index = index;
            this.distance = distance;
        }
        public int compareTo(Node node) {
            return this.distance - node.distance;
        }
    }
}
