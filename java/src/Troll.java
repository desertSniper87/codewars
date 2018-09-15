import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Troll {
    public static String disemvowel(String str) {
        List<Character> vowels = Arrays.asList('a', 'e', 'i', 'o', 'u');
        ArrayList<String> ret = new ArrayList<>();
        for (int i = 0; i < str.length(); i++) {
            if (!(vowels.contains(Character.toLowerCase(str.charAt(i))))){
                ret.add(String.valueOf(str.charAt(i)));
            }
        }
        
        return String.join("", ret);
    }
}
