import java.util.*;
import java.io.*;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int t=Integer.parseInt(br.readLine().trim());
        StringBuilder sb=new StringBuilder();
        while(t-->0){
            StringTokenizer st=new StringTokenizer(br.readLine());
            int n=Integer.parseInt(st.nextToken()),k=Integer.parseInt(st.nextToken());
            int[] a=new int[n];
            st=new StringTokenizer(br.readLine());
            for(int i=0;i<n;i++) a[i]=Integer.parseInt(st.nextToken());
            Arrays.sort(a);
            sb.append(a[k-1]).append(' ').append(a[(n-1)/2]).append('\n');
        }
        System.out.print(sb);
    }
}