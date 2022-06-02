package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

//https://www.acmicpc.net/problem/5430
public class Q5430 {

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(reader.readLine());
        loop: for (int i=0; i<t; i++) {
            String p = reader.readLine();
            int n = Integer.parseInt(reader.readLine());
            String str = reader.readLine();;
            String[] xArr = str.substring(1, str.length()-1).split(",");
            Deque<Integer> deque = new LinkedList<>();
            if (n > 0) {
                for (int j=0; j<xArr.length; j++) {
                    deque.add(Integer.parseInt(xArr[j]));
                }
            }
            boolean flag = true;
            for (int j=0; j<p.length(); j++) {
                if (p.charAt(j) == 'R') {
                    if (flag) {
                        flag = false;
                    } else {
                        flag = true;
                    }
                } else {
                    if (deque.size() == 0) {
                        System.out.println("error");
                        continue loop;
                    }

                    if (flag) {
                        deque.pollFirst();
                    } else {
                        deque.pollLast();
                    }
                }
            }
            StringBuilder sb = new StringBuilder();
            sb.append("[");
            int b = deque.size();
            if (flag) {
                for (int j=0; j<b; j++) {
                    if (j == b-1) {
                        sb.append(deque.pollFirst());
                    } else {
                        sb.append(deque.pollFirst()).append(",");
                    }
                }
            } else {
                for (int j=0; j<b; j++) {
                    if (j == b-1) {
                        sb.append(deque.pollLast());
                    } else {
                        sb.append(deque.pollLast()).append(",");
                    }
                }
            }
            sb.append("]");
            System.out.println(sb);
        }

    }
}
