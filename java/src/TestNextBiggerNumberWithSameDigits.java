import org.junit.Test;
import static org.junit.Assert.assertEquals;
import org.junit.runners.JUnit4;

public class TestNextBiggerNumberWithSameDigits {
    @Test
    public void basicTests() {
        assertEquals(21, NextBiggerNumberWithSameDigits .nextBiggerNumber(12));
        assertEquals(531, NextBiggerNumberWithSameDigits .nextBiggerNumber(513));
        assertEquals(2071, NextBiggerNumberWithSameDigits .nextBiggerNumber(2017));
        assertEquals(441, NextBiggerNumberWithSameDigits .nextBiggerNumber(414));
        assertEquals(414, NextBiggerNumberWithSameDigits .nextBiggerNumber(144));
    }
}