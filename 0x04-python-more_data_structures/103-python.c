#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Print information about a Python bytes object
 * @p: Pointer to the Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	char *string;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);

	string = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	printf("  first %ld bytes:", size > 10 ? 10 : size);
	for (Py_ssize_t i = 0; i < (size > 10 ? 10 : size); i++)
		printf(" %02x", (unsigned char)string[i]);
	printf("\n");
}

/**
 * print_python_list - Print information about a Python list object
 * @p: Pointer to the Python list object
 */
void print_python_list(PyObject *p)
{
	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);

	printf("[*] Size of the Python List = %ld\n", size);

	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Allocated = %ld\n", allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *element = PyList_GetItem(p, i);

		printf("Element %ld: ", i);

		if (PyBytes_Check(element))
			print_python_bytes(element);
		else if (PyLong_Check(element))
			printf("int\n");
		else if (PyFloat_Check(element))
			printf("float\n");
		else if (PyTuple_Check(element))
			printf("tuple\n");
		else if (PyList_Check(element))
			printf("list\n");
		else if (PyUnicode_Check(element))
			printf("str\n");
		else
			printf("unknown\n");
	}
}
