package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Q18870 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        String[] str = reader.readLine().split(" ");
        int[] list = new int[n];
        int[] sortList = new int[n];
        for (int i=0; i<n; i++) {
            list[i] = sortList[i] = Integer.parseInt(str[i]);
        }
        Arrays.sort(sortList);

        Map<Integer, Integer> map = new HashMap<>();
        int count = 0;
        for (int i : sortList) {
            if (!map.containsKey(i)) {
                map.put(i, count);
                count++;
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int i : list) {
            sb.append(map.get(i)).append(" ");
        }
        System.out.println(sb);
    }
}
