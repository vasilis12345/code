#include <cs50.h>
#include <stdio.h>
#include <string.h>


int main(void)
{

    string input_type = get_string("what type of degree do you want to convert? celcius, farenheit or kelvin ?\n");
    string output_type = get_string("to what should it be converted?\n");

    if (strcmp(input_type, "c") == 0 || strcmp(input_type, "C") == 0 || strcmp(input_type, "celsius") == 0)
    {
        if (strcmp(output_type, "f") == 0 || strcmp(output_type, "F") == 0 || strcmp(output_type, "fahrenheit") == 0)
        {
          float degree = get_float("how many degrees?\n");
          printf("the temprature you gave me results to %f degrees!\n", degree * 9/5 + 32);
        }

         else if (strcmp(output_type, "k") == 0 || strcmp(output_type, "K") == 0 || strcmp(output_type, "kelvin") == 0)
        {
           float degree = get_float("how many degrees?\n");
           printf("the temprature you gave me results to %f degrees!\n", degree + 273.15 );
        }
        else
        {
            printf("unit not supported\n");
        }
        }


    if (strcmp(input_type, "f") == 0 || strcmp(input_type, "F") == 0 || strcmp(input_type, "fahrenheit") == 0)

    {
        if (strcmp(output_type, "c") == 0 || strcmp(output_type, "C") == 0 || strcmp(output_type, "celsius") == 0)
        {
            float degree = get_float("how many degrees?\n");
            printf("the temprature you gave me results to %f degrees!\n", (degree - 32) * 5/9);
        }
          else if (strcmp(output_type, "k") == 0 || strcmp(output_type, "K") == 0 || strcmp(output_type, "kelvin") == 0)
        {
           float degree = get_float("how many degrees?\n");
           printf("the temprature you gave me results to %f degrees!\n", (degree - 32) * 5/9 + 273.15 );

         }
         else
        {
            printf("unit not supported\n");
        }

    }

      if (strcmp(input_type, "k") == 0 || strcmp(input_type, "K") == 0 || strcmp(input_type, "kelvin") == 0)
      {
        if (strcmp(output_type, "c") == 0 || strcmp(output_type, "C") == 0 || strcmp(output_type, "celsius") == 0)
        {
            float degree = get_float("how many degrees?\n");
            printf("the temprature you gave me results to %f degrees!\n", degree - 273.15 );
        }

         if (strcmp(output_type, "f") == 0 || strcmp(output_type, "F") == 0 || strcmp(output_type, "fahrenheit") == 0)
        {
          float degree = get_float("how many degrees?\n");
          printf("the temprature you gave me results to %f degrees!\n", 1.8 * (degree - 273.15) + 32 );

      }
       else
        {
            printf("unit not supported\n");
        }

      }
}
