#include <stdio.h>
#include <math.h>
#include <windows.h>
#define max(a,b) ((a) > (b) ? (a) : (b))


void planoCartesiano(void) {
    int vertical, horizontal;
    for (vertical = 14; vertical < 55 ; vertical++) {//Reta que separa o plano na vertical
        irParaXY(118, vertical);
        printf("|");
    }
    for (horizontal = 18; horizontal < 219; horizontal++) {//Reta que separa o plano na horizontal
        irParaXY(horizontal, 34);
        printf("-");
    }
    irParaXY(118, 34);
    printf("X");//Ponto central
}

void imprime_pixel(int x, int y){

    float coordX,coordY;

    coordX = round(x + 118);
    coordY = round(34 - y);

    irParaXY(coordX,coordY);
    printf("*");
}

void irParaXY(int x, int y) {
    COORD coord;
    coord.X = (short) x;
    coord.Y = (short) y;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
}

void DDA(){
    float step,Xinc,Yinc,xd,yd,coordX, coordY;
    int  x1=999,y1=999,x2=999,y2=999;

    while (x1 == 999){
        printf("Defina um valor para x1\n");
        scanf("%i",&x1);
    }

    while (y1 == 999){
        printf("Defina um valor para y1\n");
        scanf("%i",&y1);
    }

    while (x2 == 999){
        printf("Defina um valor para x2\n");
        scanf("%i",&x2);
    }

    while (y2 == 999){
        printf("Defina um valor para y2\n");
        scanf("%i",&y2);
    }

    step = max((fabs(x2-x1)),(fabs(y2-y1)));
    Xinc = (x2 - x1)/step;
    Yinc = (y2 - y1)/step;

    xd = x1;
    yd = y1;


    system("cls");

    planoCartesiano();

    while (xd != x2){

        coordX = round(xd + 118);
        coordY = round(34 - yd);

        irParaXY(coordX,coordY);
        printf("*");

        xd += Xinc;
        yd += Yinc;

    }
}

void bresenham(){

    int dx,dy,p,p2,xy2,x,y,xf,x1 = 999,x2 = 999,y1 = 999,y2 = 999;

    while (x1 == 999){
        printf("Defina um valor para x1\n");
        scanf("%i",&x1);
    }

    while (y1 == 999){
        printf("Defina um valor para y1\n");
        scanf("%i",&y1);
    }

    while (x2 == 999){
        printf("Defina um valor para x2\n");
        scanf("%i",&x2);
    }

    while (y2 == 999){
        printf("Defina um valor para y2\n");
        scanf("%i",&y2);
    }

    planoCartesiano();

    dx = x2-x1;
    dy = y2-y1;
    p = 2 * dy - dx;
    p2 = 2 * dy; //incrementa E
    xy2 = 2 * (dy-dx); //incrementa NE
        if (x1>x2){
            x = x2; y = y2; xf = x1; }
        else{
            x = x1; y = y1; xf = x2; }
    imprime_pixel(x,y);

    while (x<xf){
        x++;
        if (p<0){
            p += p2;
        }
        else{
            y++;
            p += xy2;
        }
    imprime_pixel(x,y);
    }
}

void circBresenham() {

    int xc = 999,yc = 999,r = 999;

    while (xc == 999){
        printf("Defina um valor para xC\n");
        scanf("%i",&xc);
    }
    while (yc == 999){
        printf("Defina um valor para yC\n");
        scanf("%i",&yc);
    }
    while (r == 999){
        printf("Defina um valor para r\n");
        scanf("%i",&r);
    }

    int x = 0, y = r;
    int p = 1 - r;

    planoCartesiano();

    while (x <= y) {
        irParaXY(xc + x + 118, yc + y + 34);
        printf("*");
        irParaXY(xc + x + 118, yc - y + 34);
        printf("*");
        irParaXY(xc - x + 118, yc + y + 34);
        printf("*");
        irParaXY(xc - x + 118, yc - y + 34);
        printf("*");
        irParaXY(xc + y + 118, yc + x + 34);
        printf("*");
        irParaXY(xc + y + 118, yc - x + 34);
        printf("*");
        irParaXY(xc - y + 118, yc + x + 34);
        printf(" *");
        irParaXY(xc - y + 118, yc - x + 34);
        printf("*");

        x++;
        if (p < 0) {
            p += 2 * x + 1;
        } else {
            y--;
            p += 2 * (x - y) + 1;
        }
    }
}

int main(){
    int opcao;
    int continuar = 1;

    printf("Escolha uma opcao:\n[0] Sair\n[1] DDA\n[2] Bresenham (linha)\n[3] Bresenham (circulo)\n");

    while (continuar == 1){

        scanf("%i",&opcao);
            switch(opcao) {
                case 0:
                    exit(0);
                case 1:
                    system("cls");
                    DDA();
                    continuar = 0;
                    break;
                case 2:
                    system("cls");
                    bresenham();
                    continuar = 0;
                    break;
                case 3:
                    system("cls");
                    circBresenham();
                    continuar = 0;
                    break;
                default:
                    printf("Opcao invalida.\n");
                    exit(-1);
            }
        }
    return 0;
}
