import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        int prev = -1;
        List<Integer> nums = new ArrayList<>();
        for (int num : arr) {
            if (nums.isEmpty()) {
                nums.add(num);
            } else {
                if (num != prev) {
                    nums.add(num);
                }
            }
            prev = num;
        }
        return nums.stream()
            .mapToInt(Integer::intValue)
            .toArray();
    }
}