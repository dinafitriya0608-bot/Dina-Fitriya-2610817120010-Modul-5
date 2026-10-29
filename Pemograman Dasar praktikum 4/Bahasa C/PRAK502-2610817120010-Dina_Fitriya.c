#include <stdio.h> 
#include <math.h>

int hitung(int nilai1, int nilai2){
    int difference = nilai1 - nilai2;
    if (difference < 0) {
        difference = -difference;
    }
    return difference;
}

int mutlak(int angka){
    if (angka < 0) {
        return -angka;
    }
    return angka;
}

int main()
    {
    int a,b,c,d;

    int Hasil;
    scanf("%d",&a);
    scanf("%d",&c);
    scanf("%d",&b);
    scanf("%d",&d);

    Hasil = hitung(a,b) + hitung(c,d); 
    printf("%d",mutlak(Hasil));
    
    return 0;
}