#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int_least8_t x;
int_least8_t foo();

int main(void)
{
	printf("Local variable scope\n");

	x = 42;
	foo(x);
	printf("After calling foo: x = %d\n", x);

	return EXIT_SUCCESS;
}

int_least8_t foo()
{
	x = 101;
	printf("Inside foo: x = %d\n", x);
	return x;
}
