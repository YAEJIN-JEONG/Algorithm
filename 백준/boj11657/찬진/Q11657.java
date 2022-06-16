package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

//https://www.acmicpc.net/problem/11657
public class Q11657 {
    static List<List<Node>> list = new ArrayList<>();
    static boolean flag;
    static int n;
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] str = reader.readLine().split(" ");
        n = Integer.parseInt(str[0]);
        int m = Integer.parseInt(str[1]);
        for (int i=0; i<=n; i++) {
            list.add(new ArrayList<>());
        }

        for (int i=0; i<m; i++) {
            int[] ints = Arrays.stream(reader.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            list.get(ints[0]).add(new Node(ints[1], ints[2]));
        }

        long[] d = bellman(1);

        if (flag) {
            System.out.println(-1);
        } else {
            for (int i=2; i<n+1; i++) {
                if (d[i] == Integer.MAX_VALUE) {
                    System.out.println(-1);
                } else {
                    System.out.println(d[i]);
                }
            }
        }
    }

    private static long[] bellman(int start) {
        //int 배열로 하니까 오버플로우 생김
        long[] distances = new long[n+1];
        Arrays.fill(distances, Integer.MAX_VALUE);
        distances[start] = 0;

        for (int i=1; i<=n; i++) {
            for (int j=1; j<=n; j++) {
                if (distances[j] == Integer.MAX_VALUE) continue;
                for (Node node : list.get(j)) {
                    if (distances[node.index] > distances[j] + node.distance) {
                        distances[node.index] = distances[j] + node.distance;
                        if (i == n) {
                            flag = true;
                        }
                    }
                }
            }
        }
        return distances;
    }
    static class Node {
        int index, distance;

        public Node(int index, int distance) {
            this.index = index;
            this.distance = distance;
        }
    }
}
