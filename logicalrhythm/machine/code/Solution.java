import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt(); sc.nextLine();
        while (t-- > 0) {
            int n = Integer.parseInt(sc.nextLine().trim());
            Queue<String> vip = new LinkedList<>(), normal = new LinkedList<>();
            for (int i = 0; i < n; i++) {
                String[] p = sc.nextLine().trim().split(" ");
                if (p[1].equals("VIP")) vip.add(p[0]);
                else normal.add(p[0]);
            }
            while (!vip.isEmpty())    System.out.println(vip.poll());
            while (!normal.isEmpty()) System.out.println(normal.poll());
        }
    }
}