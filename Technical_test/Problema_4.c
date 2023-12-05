/* Penguin Squad */
#include <stdio.h>

struct inter
{
    int Ex,Ey,Sx,Sy,Tx,Ty;
};
struct coada
{
    int x,y;
    int pas;
};
// E = gol
// S = Marcat
// T = iesire

int main(){
    int N,M,K,Q;
    int mat[201][201],matpasi[201][201];
    struct coada coadaDjikstraMare[41000],coadaDjikstraMic[41000];
    int p,u,facut,pasiDrumMare,pasiTotal = 0;
    struct coada drumMare [1000];
    //Djikstra mare = Marcat -> iesire
    //Djikstra mic = gol -> pas

    //citire initiala
    scanf("%d%d%d%d",&N,&M,&K,&Q);
    for(int i = 1; i <= N; i++){
        for(int j = 1; j <= M; j++){
            scanf("%d",&mat[i][j]);
        }
    }

    // test citire

    // printf("%d %d %d %d\n",N,M,K,Q);
    // for(int i = 1; i <= N; i++){
    //     for(int j = 1; j <= M; j++){
    //         printf("%d ",mat[i][j]);
    //     }
    //     printf("\n");
    // }



    // citire interogari
    int x = 0,y = 0;
    struct inter v[Q];
    for(int l = 0; l < Q; l++){
        pasiTotal = 0;
        scanf("%d%d",&v[l].Ex,&v[l].Ey);
        scanf("%d%d",&v[l].Sx,&v[l].Sy);
        scanf("%d%d",&v[l].Tx,&v[l].Ty);
        
        // djikstra marcat->iesire

        for(int i = 1; i <= N; i++)
            for(int j = 1; j <= M; j++)
                matpasi[i][j] = -1;
        
        coadaDjikstraMare[1].x = v[l].Sx;
        coadaDjikstraMare[1].y = v[l].Sy;
        coadaDjikstraMare[1].pas = 0;
        // printf("%d %d\n",coadaDjikstraMare[1].x,coadaDjikstraMare[1].y);
        p = 1;
        u = 1;
        while( p <= u ){
            x = coadaDjikstraMare[p].x;
            y = coadaDjikstraMare[p].y;
            matpasi[x][y] = coadaDjikstraMare[p].pas;
            
            // a gasit iesire
            if( x == v[l].Tx && y == v[l].Ty)break;
            //adaugare in coada

            // stanga
            if(mat[x][y-1] == 1 && matpasi[x][y-1] == -1){
                u++;
                coadaDjikstraMare[u].x = x;
                coadaDjikstraMare[u].y = y-1;
                coadaDjikstraMare[u].pas = coadaDjikstraMare[p].pas + 1;
            }
            // dreapta
            if(mat[x][y+1] == 1 && matpasi[x][y+1] == -1){
                u++;
                coadaDjikstraMare[u].x = x;
                coadaDjikstraMare[u].y = y+1;
                coadaDjikstraMare[u].pas = coadaDjikstraMare[p].pas + 1;
            }
            // sus
            if(mat[x-1][y] == 1 && matpasi[x-1][y] == -1){
                u++;
                coadaDjikstraMare[u].x = x-1;
                coadaDjikstraMare[u].y = y;
                coadaDjikstraMare[u].pas = coadaDjikstraMare[p].pas + 1;
            }
            // jos
            if(mat[x+1][y] == 1 && matpasi[x+1][y] == -1){
                u++;
                coadaDjikstraMare[u].x = x+1;
                coadaDjikstraMare[u].y = y;
                coadaDjikstraMare[u].pas = coadaDjikstraMare[p].pas + 1;
            }
            p++;
        }
        //nu s-a gasit drum
        
        if( x != v[l].Tx || y != v[l].Ty){
            printf("-1\n");
            return 0;
        }
        pasiDrumMare = matpasi[x][y];
        //refacere drum
        while(matpasi[x][y] > 0){
            facut = 0;
            drumMare[ matpasi[x][y] ].pas = matpasi[x][y];
            drumMare[ matpasi[x][y] ].x = x;
            drumMare[ matpasi[x][y] ].y = y;
            //gasire pas anterior
            //stanga
            if( matpasi[x][y-1] == matpasi[x][y] - 1 &&  facut == 0){
                y = y-1;
                facut = 1;
            }
            //dreapta
            if( matpasi[x][y+1] == matpasi[x][y] - 1 &&  facut == 0){
                y = y+1;
                facut = 1;
            }
            //sus
            if( matpasi[x-1][y] == matpasi[x][y] - 1 &&  facut == 0){
                x = x-1;
                facut = 1;
            }
            //jos
            if( matpasi[x+1][y] == matpasi[x][y] - 1 &&  facut == 0){
                x = x+1;
                facut = 1;
            }
        }

        //afisare drumMare
        // printf("Drum mare\n");
        // for(int i = 0; i <= pasiDrumMare; i++){
        //     printf("pas=%d %d %d\n",drumMare[i].pas,drumMare[i].x,drumMare[i].y);
        // }
        // printf("\n\n");


        //apeluri de djikstra gol -> pas din drum mare
        
        //primul apel
        for(int contorDrum = 1; contorDrum <= pasiDrumMare; contorDrum++){
        for(int i = 1; i <= N; i++)
            for(int j = 1; j <= M; j++)
                matpasi[i][j] = -1;

        //blocam locatia marcajului
        matpasi[ drumMare[contorDrum - 1].x ][ drumMare[contorDrum - 1].y ]=50000;
        
        coadaDjikstraMic[1].x = v[l].Ex;
        coadaDjikstraMic[1].y = v[l].Ey;
        coadaDjikstraMic[1].pas = 0;
        // printf("%d %d\n",coadaDjikstraMic[1].x,coadaDjikstraMic[1].y);
        p = 1;
        u = 1;
        while( p <= u ){
            x = coadaDjikstraMic[p].x;
            y = coadaDjikstraMic[p].y;
            matpasi[x][y] = coadaDjikstraMic[p].pas;
            
            // a gasit iesire
            if( x == drumMare[contorDrum].x && y == drumMare[contorDrum].y)break;
            //adaugare in coada

            // stanga
            if(mat[x][y-1] == 1 && matpasi[x][y-1] == -1){
                u++;
                coadaDjikstraMic[u].x = x;
                coadaDjikstraMic[u].y = y-1;
                coadaDjikstraMic[u].pas = coadaDjikstraMic[p].pas + 1;
            }
            // dreapta
            if(mat[x][y+1] == 1 && matpasi[x][y+1] == -1){
                u++;
                coadaDjikstraMic[u].x = x;
                coadaDjikstraMic[u].y = y+1;
                coadaDjikstraMic[u].pas = coadaDjikstraMic[p].pas + 1;
            }
            // sus
            if(mat[x-1][y] == 1 && matpasi[x-1][y] == -1){
                u++;
                coadaDjikstraMic[u].x = x-1;
                coadaDjikstraMic[u].y = y;
                coadaDjikstraMic[u].pas = coadaDjikstraMic[p].pas + 1;
            }
            // jos
            if(mat[x+1][y] == 1 && matpasi[x+1][y] == -1){
                u++;
                coadaDjikstraMic[u].x = x+1;
                coadaDjikstraMic[u].y = y;
                coadaDjikstraMic[u].pas = coadaDjikstraMic[p].pas + 1;
            }
            p++;
        }
        //finalizare djiksra mic
        // nu s-a gasit drum
         if( x != drumMare[contorDrum].x || y != drumMare[contorDrum].y){
            // printf("Trisam!\n");
            pasiTotal += K;
        }
        else pasiTotal += matpasi[x][y];
        //mutarea gauri
        v[l].Ex = drumMare[contorDrum-1].x;
        v[l].Ey = drumMare[contorDrum-1].y;
        // printf("pasiT=%d pasi=%d x = %d y = %d\n",pasiTotal,matpasi[x][y],x,y);
        }
        pasiTotal += pasiDrumMare;
        // printf("solutie=%d\n", pasiTotal);
        printf("%d\n", pasiTotal);
    }
    return 0;
}