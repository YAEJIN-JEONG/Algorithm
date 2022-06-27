package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

//https://www.acmicpc.net/problem/9935
public class Q9935 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String str = reader.readLine();
        String input = reader.readLine();
        Stack<Character> stack = new Stack<>();
        for (int i=0; i<str.length(); i++) {
            stack.push(str.charAt(i));

            if (stack.size() >= input.length()) {
                boolean flag = true;
                for (int j=0; j<input.length(); j++) {
                    if (stack.get(stack.size()-input.length()+j) != input.charAt(j)) {
                        flag = false;
                        break;
                    }
                }
                if (flag) {
                    for (int j=0; j<input.length(); j++) {
                        stack.pop();
                    }
                }
            }
        }
        StringBuilder sb = new StringBuilder();
        for (Character c : stack) {
            sb.append(c);
        }
        System.out.println(sb.length() == 0 ? "FRULA" : sb);

    }
}
