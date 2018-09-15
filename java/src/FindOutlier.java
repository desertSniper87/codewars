import java.util.ArrayList;

public class FindOutlier{
  static int find(int[] integers){
      ArrayList<Integer> even = new ArrayList<>();
      ArrayList<Integer> odd = new ArrayList<>();
      for (int i : integers) {
          if (i%2==0) {
              even.add(i);
          } else {
              odd.add(i);
          }
      }

      if (even.size() == 1) {
          return even.get(0);
      } else {
          return odd.get(0);
      }
}}
