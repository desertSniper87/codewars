public class DnaStrand {
    public static String makeComplement(String dna) {
        //Your code
        char[] result = new char[dna.length()];
        
        for (int i=0;i<dna.length();i++){
            switch(dna.charAt(i)){
                case 'A':
                    result[i] = 'T';
                    break;
                case 'T':
                    result[i] = 'A';
                    break;
                case 'C':
                    result[i] = 'G';
                    break;
                case 'G':
                    result[i] = 'C';
                    break;
            }
        }

        return new String(result);
    }
}
