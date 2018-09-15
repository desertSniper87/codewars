import java.util.*;

public class Minimum{

	public static int minValue(int[] values){

		Set<Integer> s = new HashSet<>();
		for (int i:values) {
			s.add(i);
		}

		List l = new ArrayList(s);
		Collections.sort(l);
		Collections.reverse(l);

        System.out.println("l = " + l);

        int sum = 0;
        for (int i=0;i<l.size();i++){
            System.out.println("i = " + i);
            System.out.println("l.get() = " + l.get(i));
            System.out.println("sum = " + sum);
            sum += (int) l.get(i) * (Math.pow(10, i));
        }

		return sum;
	}

}