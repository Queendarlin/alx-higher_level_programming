#include <Python.h>

/**
 * print_python_list_info - Prints information about a Python list.
 * @p: A pointer to a PyObject representing a Python list.
 *
 * Description:
 * This function prints information about the given Python list, including
 * its size, allocated space, and the type of each element.
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;

	Py_ssize_t size = PyList_Size(p);

	Py_ssize_t allocated = list->allocated;

	PyObject *item;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (Py_ssize_t i = 0; i < size; ++i)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
