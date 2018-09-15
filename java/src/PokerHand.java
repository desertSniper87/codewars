/*
 ** https://www.codewars.com/kata/ranking-poker-hands/train/java**/

import java.lang.reflect.Array;
import java.util.*;

public class PokerHand
{
    public enum Result { TIE, WIN, LOSS }
    protected int handCode=999;
    protected int handVal = -1;
    public int subVal = 0;

    final Character[] ROYAL_FLUSH = {'A', 'J', 'K', 'Q', 'T'};
    final Character[] STRAIGHT_1 = {'2', '3', '4', '5', '6'};
    final Character[] STRAIGHT_2 = {'3', '4', '5', '6', '7'};
    final Character[] STRAIGHT_3 = {'4', '5', '6', '7', '8'};
    final Character[] STRAIGHT_4 = {'5', '6', '7', '8', '9'};
    final Character[] ALL_CARDS = {'K', 'A', 'T', 'Q', 'J', '2', '3', '4', '5', '6', '7', '8', '9'};

    @SuppressWarnings("unchecked")
    PokerHand(String hand)
    {
        StringTokenizer handData = new StringTokenizer(hand);
        HashMap<Character, ArrayList<Character>> map = new HashMap<Character, ArrayList<Character>>();

        while (handData.hasMoreTokens()){
            String token = handData.nextToken();
            char tokenNumber = token.charAt(0);
            char tokenType = token.charAt(1);
            ArrayList<Character> arrayList = new ArrayList<>();
            arrayList.add(tokenNumber);

            if (map.containsKey(tokenType)) {
                map.get(tokenType).add(tokenNumber);
            } else {
                map.put(tokenType, arrayList);
            }


            //            map.put(tokenType, arrayList);
        }

        for (Map.Entry m:map.entrySet()) {
            System.out.println("m = " + m);
        }

        handVal = handVal(map);
        System.out.println("handVal = " + handVal);

        Set<Character> handSet = new HashSet<>();
        for (Map.Entry m: map.entrySet()) {
            handSet.addAll((ArrayList<Character>) m.getValue());
        }

        if (map.keySet().size() == 1){
//            Character[] flushArray =(Character[]) map.values().toArray()[0];
            if (isRoyalFlush((ArrayList) map.values().toArray()[0])){
                handCode = 0; /* ROYAL FLUSH */
            }
            else if (compareHand((ArrayList) map.values().toArray()[0], STRAIGHT_1) ||
                    compareHand((ArrayList) map.values().toArray()[0], STRAIGHT_2) ||
                    compareHand((ArrayList) map.values().toArray()[0], STRAIGHT_3) ||
                    compareHand((ArrayList) map.values().toArray()[0], STRAIGHT_4)
                    ) {
                handCode = 1; /* STRAIGHT FLUSH */
            } else {
                /* FLUSH */
                handCode = 4;
            }
        } else if (map.keySet().size() == 4) {
            List<Character> common = new ArrayList<Character>(Arrays.asList(ALL_CARDS));
            for (Map.Entry m: map.entrySet()) {
                common.retainAll((ArrayList) m.getValue());
            }

            System.out.println("common = " + common);
            if (common.size() == 1){ /* Four of a kind */
                handCode = 2;
            } else if (handSet.size()==5){
                /* STRAIGHT */
                Character[] handArray =  handSet.toArray(new Character[handSet.size()]);
                Arrays.sort(handArray);
                if (checkFlush(handArray)){
                    handCode = 5;
                }

            } else if( handSet.size() == 4){
                /* ONE PAIR */
                handCode = 9;

            } else if (handSet.size() == 3){
                /* TWO PAIR */
                handCode = 8;
            } else if (handSet.size() == 2){
                /* Full House */
                handCode = 3;
            }

        } else if (map.keySet().size() == 3 & handSet.size()!=2){
            List<Character> common = new ArrayList<Character>(Arrays.asList(ALL_CARDS));
            for (Map.Entry m: map.entrySet()) {
                common.retainAll((ArrayList) m.getValue());
            }

            if (common.size() == 1) { /* Three of a kind */
                handCode = 6;
                return;
            }

            Character[] handArray =  handSet.toArray(new Character[handSet.size()]);
            Arrays.sort(handArray);
            if (checkFlush(handArray)){
                handCode = 5;
                return;
            }

            /** If handCode 8, then TWO PAIR
             * else if handCode 9 then one pair
             * else handCode 10
             */

            if (handSet.size()==3) {
                /* TWO PAIRS */
                handCode = 8;
            } else if (handSet.size() ==4 ){
                /* One Pair */
                handCode = 9;
            } else if (handSet.size() == 5) {
                System.out.println("Arrays.sort(handArray) = " + handArray);
                if (Arrays.equals(ROYAL_FLUSH, handArray)){
                    /* ROYAL */
                    handCode = 5;

                }

            }

//            for (Map.Entry m: map.entrySet()) {
//                ArrayList<Character> c = new ArrayList<>((ArrayList<Character>) m.getValue());
//
//                if (c.size()==3){
//                    /* Not 2 pair */
//                    handCode = 9;
//                    return;
//                }
//
//                /* 2 Pair */
//                if (handSet.size() != 2)
//                    handCode = 8;
//                    return;
//            }
        }
        else {
            if (handSet.size() == 2){
                /* Full House */
                handCode = 3;
            } else if (handSet.size() == 3) {
                /* TWO PAIRS */
                handCode = 8;
            }
            else {
                Character[] handArray =  handSet.toArray(new Character[handSet.size()]);
                Arrays.sort(handArray);
                if (checkFlush(handArray)){
                    handCode = 5;
                }
            }
            System.out.println("handSet = " + handSet);
        }
    }

    public Boolean checkFlush(Character[] handArray) {
        System.out.println("handArray = " + handArray);
        Character[] highFlush = {'A', 'J', 'K', 'Q', 'T'};
        Arrays.sort(handArray);
        if (isFlushArray(highFlush, handArray)) {
            return true;
        }

        for (int i = 0; i < handArray.length - 1; i++) {
            if (handArray[i] == '9') {
                if (handArray[i + 1] != 'J') {
                    return false;
                }
            } else if (handArray[i] == 'J') {
                if (handArray[i + 1] != 'K') {
                    return false;
                }
            } else if (handArray[i] == 'K') {
                if (handArray[i + 1] != 'Q') {
                    return false;
                }
            } else if (handArray[i] == 'Q') {
                if (handArray[i + 1] != 'T') {
                    return false;
                }
            } else if (handArray[i + 1] != handArray[i] + 1) {
                return false;
            }
        }
        return true;
    }

    public Boolean isFlushArray(Character[] highFlush, Character[] handArray) {
        for (int i = 0; i < handArray.length; i++) {
            if (handArray[i] != highFlush[i]) {
                return false;
            }
        }

        return true;
    }

    public Boolean isRoyalFlush(ArrayList<Character> a) {
        Set<Character> aSet = new HashSet<>(a);

        for (Character i :
                ROYAL_FLUSH) {
            if (!aSet.contains(i)) {
                return false;
            }
        }

        return true;

    }


    @SuppressWarnings("unchecked")
    public Boolean compareHand(ArrayList a, Character[] b) {
        Collections.sort(a);
        for (int i = 0; i < b.length; i++) {
            if (a.get(i) != b[i]) {
                return false;
            }
        }
        return true;
    }

    @SuppressWarnings("unchecked")
    public int handVal(HashMap<Character, ArrayList<Character>> map) {
        int val = 0;
        subVal = 0;
        for (Map.Entry m:map.entrySet()) {
            for (Character c : (ArrayList<Character>) m.getValue()
                    ) {
                switch (c) {
                    case 'A':
                        val =  13;
                        subVal += 13;
                        break;
                    case 'K':
                        val = val < 12 ? 12 : val;
                        subVal += 12;
                        break;
                    case 'Q':
                        val = val < 11 ? 11 : val;
                        subVal += 11;
                        break;
                    case 'J':
                        val = val < 10 ? 10 : val;
                        subVal += 10;
                        break;
                    case 'T':
                        val = val < 9 ? 9 : val;
                        subVal += 9;
                        break;
                    default :
                        int v = Character.getNumericValue(c);
                        subVal += v;
                        val = val < v ? v : val;
                }
            }
        }

        return val;
    }

    public Result compareWith(PokerHand hand) {
        String[] handCodes = {"ROYAL_FLUSH", "STRAIGHT_FLUSH", "FOUR OF A KIND", "FULL HOUSE", "FLUSH", "STRAIGHT", "THREE OF A KIND", "", "TWO PAIR", "ONE PAIR"};
        try{
            System.out.println("handCode = " + handCode + " " + handCodes[handCode]);
            System.out.println("hand.handCode = " + hand.handCode + " " + handCodes[hand.handCode]);
        } catch (ArrayIndexOutOfBoundsException a) {
            System.out.println("a = " + a);
            System.out.println("handCode = " + handCode);
            System.out.println("hand.handCode = " + hand.handCode);
        }
        System.out.println("subVal = " + subVal);
        System.out.println("subVal = " + hand.subVal);
        if (handCode==hand.handCode) {
            //            if (handCode == 002 ){
            if (handVal>hand.handVal) {
                return Result.WIN;
            } else if (handVal<hand.handVal){
                return Result.LOSS;
            } else {
                if (subVal>hand.subVal) {
                    return Result.WIN;
                } else if (subVal<hand.subVal) {
                    return Result.LOSS;
                }
                return Result.TIE;
            }
            //            }
            //            return Result.TIE;
        }
        else if (handCode < hand.handCode) {
            System.out.println("Winning");
            return Result.WIN;
        }
        else {
            System.out.println("Losing");
            return Result.LOSS;
        }
    }
}
