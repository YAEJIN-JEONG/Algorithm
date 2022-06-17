package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

//https://www.acmicpc.net/problem/1918
public class Q1918 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String input = reader.readLine();
        char[] arr = input.toCharArray();
        StringBuilder sb = new StringBuilder();
        Stack<Character> stack = new Stack<>();
        for (int i=0; i<arr.length; i++) {
            // 알파벳은 sb에 바로 넣기
            if (arr[i] >= 'A' && arr[i] <= 'Z') {
                sb.append(arr[i] + "");
                // 여는 괄호 stack에 바로 넣기
            } else if (arr[i] == '(') {
                stack.push(arr[i]);
            } else if (arr[i] == ')') {
                // 닫는 괄호면 여는괄호 만날때까지 sb에 추가
                while (!stack.isEmpty() && stack.peek() != '(') {
                    sb.append(stack.pop());
                }
                // 여는괄호 stack에서 삭제
                if (!stack.isEmpty()) {
                    stack.pop();
                }
            } else {
                // 우선순위가 앞에꺼보다 높으면 sb에 넣고 같거나 낮으면 stack에 추가
                while (!stack.isEmpty() && check(stack.peek(), arr[i])) {
                    sb.append(stack.pop());
                }
                stack.push(arr[i]);
            }
        }
        // 남은 stack에 있는 값 sb에 추가
        while (!stack.isEmpty()) {
            sb.append(stack.pop());
        }
        System.out.println(sb);
    }
    private static boolean check(char a, char b) {
        // 우선순위 체크
        if ((a == '+' || a == '-') && (b == '+' || b == '-')) {
            return true;
        } else if ((a == '*' || a == '/') && ((b == '+' || b == '-') || (b == '*' || b == '/'))) {
            return true;
        } else {
            return false;
        }
    }
}
