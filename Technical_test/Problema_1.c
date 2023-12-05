/* Penguin Squad */
#include <stdio.h>

int main(){

    int v[101];
    // 0-Vasilica castiga
    // 1-Mircea castiga
    for(int i = 1; i <= 100; i++)
        v[i] = 0;
    v[2] = 1;
    v[3] = 1;
    v[4] = 1;
    v[5] = 1;
    v[6] = 1;
    v[9] = 1;
    v[10] = 1;
    v[11] = 1;
    v[12] = 1;
    for(int i = 13; i <= 100; i++){
        if( v[i-2]  == 0 ) v[i] = 1;
        if( v[i-3]  == 0 ) v[i] = 1;
        if( v[i-5]  == 0 ) v[i] = 1;
    }
    int x,n;
    scanf("%d",&n);
    // loop principal
    for(int i = 1; i <= n; i++){
        scanf("%d",&x);
        if(v[x] == 0)
        if(v[x] == 0)printf("Vasilica\n");
        if(v[x] == 1)printf("Mircea\n");
    }

    return 0;
}