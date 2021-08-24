#include <stdio.h>
#include <math.h>
int main(void)
{
    float a,b,c,d;
    printf("a*x^2+b*x+c=0\na: ");
    scanf("%f",&a);
    printf("b: ");
    scanf("%f",&b);
    printf("c: ");
    scanf("%f",&c);
    if (a==0)
    {
        printf("This is not the quadratic equation.\n");
        if (b==0)
        {
            if (c==0)
            {
                printf("Infinite number of solutions.");
            }
            else
            {
                printf("No solutions.");
            }
        }
        else
        {
            printf("One solution: %f .",-c/b);
        }
    }
    else
    {
        d=b*b-4*a*c;
        if (d<0)
        {
            printf("No solutions.");
        }
        else
        {
            if (d==0)
            {
                printf("One solution: %f .",-b/(2*a));
            }
            else
            {
                printf("Two solutions: %f and %f .",(-b-sqrt(d))/(2*a),(-b+sqrt(d))/(2*a));
            }
        }
    }
    printf("\nPress Enter to close.\n");
    getchar();
    getchar();
    return 0;
}
