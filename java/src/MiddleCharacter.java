public class MiddleCharacter {
    public static String getMiddle(String word) {
        word = word.trim();
        int l = word.length();
        String ret = "";
        char c1, c2;

        if (l%2==1) {
            ret = String.valueOf(word.charAt(l/2));
        } else {
            c1 = word.charAt(l/2-1);
            c2 = word.charAt(l/2);
            ret = String.valueOf(c1) + String.valueOf(c2);
        }

        return ret;

        //Code goes here!
    }
}

