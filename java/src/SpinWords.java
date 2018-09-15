public class SpinWords {

    public String spinWords(String sentence) {
        //TODO: Code stuff here
        int l;

        String[] str_arr = sentence.split(" ");
        int g = 0;

        String[] ret_str_arr = new String[str_arr.length];

        for (String i : str_arr) {
            l = i.length();
            if (l>4){
                char[] char_arr = new char[l];
                char[] ret_word_arr =char_arr;

                char_arr = i.toCharArray();

                for (int k=l-1, j=0; k>=0; k--, j++ ){
                    ret_word_arr[j] = char_arr[k];
                }

                ret_str_arr[g++] = new String(ret_word_arr);
            }
            else {
                ret_str_arr[g++] = i;
            }


        }

        String ret_str = String.join(" ", ret_str_arr);
        //for (String j:ret_str_arr){

        //}

        return ret_str;
        
    }
}

