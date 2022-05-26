import java.util.*;

public class Solution {

    public List<Integer> solution(String[] info, String[] query) {
        List<Integer> answer = new ArrayList<>();
        Map<String, List<Integer>> hashTable = new HashMap<>();

        for (String s : info) {
            String[] inf = s.split(" ");

            for (int i=0; i<(1 << 4); i++) {
                StringBuilder key = new StringBuilder();
                for (int j=0; j<4; j++) {
                    if ((i & (1 << j)) > 0)
                        key.append(inf[j]);
                    else
                        key.append("-");
                }
                hashTable.putIfAbsent(key.toString(), new ArrayList<>());
                hashTable.get(key.toString()).add(Integer.parseInt(inf[4]));
            }
        }

        for (String key : hashTable.keySet())
            Collections.sort(hashTable.get(key));

        for (String q : query) {
            String[] inf = q.split(" ");
            List<Integer> list = hashTable.get(inf[0] + inf[2] + inf[4] + inf[6]);
            if (list != null)
                answer.add(list.size() - lowerBound(list, Integer.parseInt(inf[7])));
            else
                answer.add(0);
        }

        return answer;
    }

    public int lowerBound(List<Integer> list, int target) {
        int low = 0;
        int high = list.size();

        while (low < high) {
            int mid = (low + high) / 2;

            if (list.get(mid) >= target)
                high = mid;
            else
                low = mid + 1;
        }

        return high;
    }
}
