#include <cs50.h>
#include <stdio.h>
#include <string.h>


int main(void)
{

    string type = get_string("what type of degree do you want to convert? celcius or farenheit?\n");

    
    if (strcmp(type, "c") == 0 || strcmp(type, "C") == 0 || strcmp(type, "celsius") == 0)
    {
        float degree = get_float("how many degrees?\n");
    }

    if (strcmp(type, "f") == 0 || strcmp(type, "F") == 0 || strcmp(type, "fahrenheit") == 0)

    {
        float degree = get_float("how many degrees?\n");
        printf("the temprature you gave me results to %f degrees!\n", degree - 32 * 5/9 );
    }
    else
    {
        printf("sorry i dont recognize this temprature unit!\n");
    }


}
