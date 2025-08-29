class Solution {
public:
    int divide(int dividend, int divisor) {
        
        long long INT_MAX_VAL = (1LL << 31) - 1;
        long long INT_MIN_VAL = -(1LL << 31);

        if (dividend == INT_MIN_VAL && divisor == -1)
            return INT_MAX_VAL;

        bool negative = (dividend < 0) ^ (divisor < 0);

        long long a = llabs(dividend);
        long long b = llabs(divisor);
        long long quotient = 0;

        while (a >= b) {
            long long temp = b, multiple = 1;
            while (a >= (temp << 1)) {
                temp <<= 1;
                multiple <<= 1;
            }
            a -= temp;
            quotient += multiple;
        }

        return negative ? -quotient : quotient;
    }
};
