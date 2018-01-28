public class NumberFun {
    public static long findNextSquare(long sq){
        double root = Math.sqrt(sq);

        int rootInt = (int) root;
        double over = root-rootInt;
        if (over!=0)
            return -1;
        else
            return (long) Math.pow(rootInt+1,2);
    }
}