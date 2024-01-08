#include "Python.h"

/**
 * print_python_string - Prints information about a Python string object.
 * @p: A pointer to a Python string object (PyObject *).
 */
void print_python_string(PyObject *p)
{
	long int length;

	fflush(stdout);

	printf("[.] string object info\n");

	/* Check if the object is a valid string by comparing its type name */
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	/* Obtain the length of the string using the PyASCIIObject */
	length = ((PyASCIIObject *)(p))->length;

	/* Check if the string is a compact ASCII or a compact Unicode object*/
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	printf("  length: %ld\n", length);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}
