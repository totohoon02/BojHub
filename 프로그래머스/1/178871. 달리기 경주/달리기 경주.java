import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        Map<String, Integer> playerMap = new HashMap<>();
        for (int i = 0; i < players.length; i++) {
            playerMap.put(players[i], i);
        }

        for (String calling : callings) {
            int i = playerMap.get(calling);
            String before = players[i - 1];

            // 자리 교체
            players[i - 1] = calling;
            players[i] = before;

            // 해쉬값 교체
            playerMap.put(calling, i - 1);
            playerMap.put(before, i);
        }
        
        return players;
    }
}