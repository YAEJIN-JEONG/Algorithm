package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

//https://www.acmicpc.net/problem/7662
public class Q7662 {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(reader.readLine());

        for (int i=0; i<t; i++) {
            TreeMap<Integer, Integer> treeMap = new TreeMap<>();
            int n = Integer.parseInt(reader.readLine());
            for (int j=0; j<n; j++) {
                String[] str = reader.readLine().split(" ");
                int a = Integer.parseInt(str[1]);
                if (str[0].equals("I")) {
                    treeMap.put(a, treeMap.getOrDefault(a, 0) + 1);
                } else {
                    if (treeMap.size() == 0) {
                        continue;
                    }
                    int key;
                    if (a == -1) {
                        key = treeMap.firstKey();
                    } else {
                        key = treeMap.lastKey();
                    }
                    treeMap.put(key, treeMap.get(key) - 1);
                    if (treeMap.get(key) == 0) {
                        treeMap.remove(key);
                    }
                }
            }

            if (treeMap.isEmpty()) {
                System.out.println("EMPTY");
            } else {
                System.out.println(treeMap.lastKey() + " " + treeMap.firstKey());
            }

        }

    }


}
