import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim());
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < t; i++) {
            String s = br.readLine().trim();
            int x = 0, y = 0;
            for (int j = 0; j < s.length(); j++) {
                char c = s.charAt(j);
                if (c == 'E') x++;
                else if (c == 'W') x--;
                else if (c == 'N') y++;
                else if (c == 'S') y--;
            }
            out.append("Position = (").append(x).append(", ").append(y).append("), Distance = ").append(Math.abs(x) + Math.abs(y));
            if (i + 1 < t) out.append('
');
        }
        System.out.print(out.toString());
    }
}
