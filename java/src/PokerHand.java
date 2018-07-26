/*
 ** https://www.codewars.com/kata/ranking-poker-hands/train/java**/

import java.util.*;

public class PokerHand
{
    public enum Result { TIE, WIN, LOSS }

    PokerHand(String hand)
    {
        StringTokenizer handData = new StringTokenizer(hand);
        int hearts = 0;
        int ace = 0;
        int joker = 0;
            if (handData.hasMoreTokens()){
                String token = handData.nextToken();
                char tokenNumber = token.charAt(0);
                char tokenType = token.charAt(1);
//                if (tokenType=='H')
//                    hearts++;

                switch(tokenNumber) {
                    case 'A':
                        ace++;
                    case 'J':
                        joker++;

                }

//                switch (tokenType) {
//                    case 'H':
//                        hearts++;
//                        break;
//                    case '':
//                }
        }
    }

    public Result compareWith(PokerHand hand) {
        return Result.TIE;
    }
}