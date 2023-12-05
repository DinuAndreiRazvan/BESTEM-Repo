/* Penguin Squad */
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, i, sum = 0;
    int *dog, *prize;

    // check if 0
    scanf("%d", &n);
    if(n == 0) {
        printf("0");
        return 0;
    }

    // allocate mem
    dog = (int*)calloc(n, sizeof(int));
    prize = (int*)calloc(n, sizeof(int));

    /// read first
     scanf("%d", &dog[0]);
     prize[0] = 1;

    for(i = 1; i < n; i++) {
        scanf("%d", &dog[i]);
        prize[i] = 1;
        if(dog[i] > dog[i-1]) {
            prize[i] = prize[i-1] + 1;
        }
    }

    sum += prize[n-1];
    for(i = n-2; i >= 0; i--) {
        if(dog[i] > dog[i+1] && prize[i] <= prize[i+1])
            prize[i] = prize[i+1] + 1;
        sum += prize[i];
    }

    printf("%d", sum);

    free(dog);
    free(prize);

    return 0;
}