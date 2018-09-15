public class NextBiggerNumberWithSameDigits
{
    public static long nextBiggerNumber(long n)
    {
        String s = String.valueOf(n);
        char[] r = s.toCharArray();
        System.out.println(r);

        for (int i=s.length()-1; i>=0; i--) {
//            System.out.println(s.charAt(i));
              for (int j=i; j>=0; j--) {
                  if (Character.getNumericValue(s.charAt(i)) > Character.getNumericValue(s.charAt(j))) {
                      System.out.println("i, j, s.charAt(i), s.charAt(j) " + i + " " + j + " " + s.charAt(i) + " "+ s.charAt(j));
                      r[i] = (s.charAt(j));
                      r[j] = (s.charAt(i));

                      return Integer.parseInt(new String(r));
                  }
              }
       
        }
        return Integer.parseInt(s);
    }
}
