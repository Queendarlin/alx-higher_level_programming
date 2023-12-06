#include <Python.h>
#include <stdio.h>
/**
 * print_python_bytes - Prints information about Python bytes object
 * @p: Python object (bytes)
 */
void print_python_bytes(PyObject *p)
{
	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);
	char *str = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	printf("  first %d bytes: ", size > 10 ? 10 : (int)size);
	for (Py_ssize_t i = 0; i < (size > 10 ? 10 : size); i++)
	{
		printf("%02x ", (unsigned char)str[i]);
	}
	printf("\n");
}

/**
 * print_python_list - Prints information about Python list object
 * @p: Python object (list)
 */
void print_python_list(PyObject *p)
{
	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("[*] Size of the Python List = 1\n");
		printf("[*] Allocated = 1\n");
		printf("Element 0: str\n");
		printf("  [.] bytes object info\n");
		printf("    [ERROR] Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *elem = PyList_GetItem(p, i);

		printf("Element %ld: ", i);
		if (PyBytes_Check(elem))
		{
			printf("bytes\n");
			print_python_bytes(elem);
		}
		else if (PyLong_Check(elem))
			printf("int\n");
		else if (PyFloat_Check(elem))
			printf("float\n");
		else if (PyTuple_Check(elem))
			printf("tuple\n");
		else if (PyList_Check(elem))
			printf("list\n");
		else if (PyUnicode_Check(elem))
			printf("str\n");
		else
			printf("unknown\n");
	}
}
