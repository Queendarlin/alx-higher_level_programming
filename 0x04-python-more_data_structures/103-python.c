#include <Python.h>
#include <stdio.h>
#include <time.h>

/**
 * print_python_bytes - Prints information about Python bytes object
 * @p: Python object (bytes)
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", PyBytes_Size(p));

	if (PyBytes_AsStringAndSize(p, &str, &size) != -1)
	{
		printf("  trying string: %s\n", str);
		printf("  first 10 bytes:");
		for (i = 0; i < size && i < 10; ++i)
			printf(" %02x", (unsigned char)str[i]);
		printf("\n");
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}

/**
 * print_python_list - Prints information about Python list object
 * @p: Python object (list)
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *elem;

	printf("[*] Python list info\n");
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; ++i)
	{
		elem = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(elem)->tp_name);
		if (PyBytes_Check(elem))
			print_python_bytes(elem);
	}
}
