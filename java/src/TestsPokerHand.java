import static org.junit.Assert.*;
import org.junit.Test;
import java.util.*;

public class TestsPokerHand
{
    private PokerHand.Result loss = PokerHand.Result.LOSS;
    private PokerHand.Result win = PokerHand.Result.WIN;
    private PokerHand.Result tie = PokerHand.Result.TIE;

    @Test
    public void PokerHandRankingTest()
    {
//        Test("Highest straight flush wins",        loss, "2H 3H 4H 5H 6H", "KS AS TS QS JS");       /** DONE **/
//        Test("Straight flush wins of 4 of a kind", win,  "2H 3H 4H 5H 6H", "AS AD AC AH JD");       /** DONE **/
//        Test("Highest 4 of a kind wins",           win,  "AS AH 2H AD AC", "JS JD JC JH 3D");       /** DONE **/
//        Test("4 Of a kind wins of full house",     loss, "2S AH 2H AS AC", "JS JD JC JH AD");
//        Test("Full house wins of flush",           win,  "2S AH 2H AS AC", "2H 3H 5H 6H 7H");       /** DONE **/
//        Test("Highest flush wins",                 win,  "AS 3S 4S 8S 2S", "2H 3H 5H 6H 7H");       /** DONE **/
//        Test("Flush wins of straight",             win,  "2H 3H 5H 6H 7H", "2S 3H 4H 5S 6C");
//        Test("Equal straight is tie", 	  	     tie,  "2S 3H 4H 5S 6C", "3D 4C 5H 6H 2S");       /** DONE: Refractor Needed */
//        Test("Straight wins of three of a kind",   win,  "2S 3H 4H 5S 6C", "AH AC 5H 6H AS");
//        Test("3 Of a kind wins of two pair",       loss, "2S 2H 4H 5S 4C", "AH AC 5H 6H AS");
//        Test("2 Pair wins of pair",                win,  "2S 2H 4H 5S 4C", "AH AC 5H 6H 7S");       /* DONE */
//        Test("Highest pair wins",                  loss, "6S AD 7H 4S AS", "AH AC 5H 6H 7S");
//        Test("Pair wins of nothing",               loss, "2S AH 4H 5S KC", "AH AC 5H 6H 7S");
//        Test("Highest card loses",                 loss, "2S 3H 6H 7S 9C", "7H 3C TH 6H 9S");
//        Test("Highest card wins",                  win,  "4S 5H 6H TS AC", "3S 5H 6H TS AC");
//        Test("Equal cards is tie",		         tie,  "2S AH 4H 5S 6C", "AD 4C 5H 6H 2C");
//
//        Test("Randomized Test 1:",		                 loss,  "KC 4H KS 2H 8D", "5S 5D 2C KH KC");
//        Test("Randomized Test 3:",		                 win,  "QH 8H KD JH 8S", "KC 4H KS 2H 8D");
//        Test("Randomized Test 5:",		                 loss,  "KS 8D 4D 9S 4S", "KH KC 3S 3H 3D");
//        Test("Randomized Test 5.5:",		                 loss,  "AS 3C KH AD KC", "QC KH TS JS AH");
//        Test("Randomized Test 6:",		                 win,  "JH 8S TH AH QH", "JS QS 9H TS KH");
//        Test("Randomized Test 7:",		                 win,  "QC KH TS JS AH", "6S 8S 7S 5H 9H");
//        Test("Randomized Test 8:",		                 win,  "2D 6D 3D 4D 5D", "3S 8S 9S 5S KS");
//        Test("Randomized Test 11:",		                 loss,  "KS 8D 4D 9S 4S", "5S 5D 2C KH KC");
        Test("Randomized Test 12:",		                 win,  "JS QS 9H TS KH", "7C 7S KH 2H 7H");

        Test("Randomized Test 2:",		                 win,  "JH 8H AH KH QH", "5C 6C 3C 7C 4C");
        Test("Randomized Test 12:",		                 win,  "JS QS 9H TS KH", "8C 4S KH JS 4D");
        Test("Randomized Test 13:",		                 loss,  "JH 8S TH AH QH", "TS KS 5S 9S AC");
        Test("Randomized Test 14:",		                 win,  "QC KH TS JS AH", "6S 8S 7S 5H 9H");
        Test("Randomized Test 15:",		                 win,  "TS KS 5S 9S AC", "JH 8S TH AH QH");
        Test("Randomized Test 16:",		                 win,  "JC KH JS JD JH", "2D 6D 3D 4D 5D");

    }

    private void Test(String description, PokerHand.Result expected, String playerHand, String opponentHand)
    {
        PokerHand player = new PokerHand(playerHand);
        PokerHand opponent = new PokerHand(opponentHand);
        assertEquals(description + ":", expected, player.compareWith(opponent));
    }
}
