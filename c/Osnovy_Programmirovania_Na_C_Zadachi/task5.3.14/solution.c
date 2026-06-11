#include <stdio.h>
#include <math.h>

int main(void) {
    int k, T = 5570;
    double N, n0 = 7.5e10;
    scanf("%d", &k);
    
    N = n0 * exp(-k * log(2) / T);
    
    printf("%.2lf", N / 1e9);
    
    return 0;
}