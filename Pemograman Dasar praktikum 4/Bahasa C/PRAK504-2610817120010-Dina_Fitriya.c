#include <stdio.h> 

int reverse(int n){
    int results = 0;

    while (n > 0) {
        results = results * 10 + n % 10;
        n = n / 10;
    }

    return results;
}

    int main() { 
        int A, B;
        scanf("%d %d",&A,&B); 
        A=reverse(A);
        B=reverse(B);
        int C = A+B; 
        printf("%d",reverse(C));
}