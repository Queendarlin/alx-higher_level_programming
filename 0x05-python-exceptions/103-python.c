#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
 * print_python_list - Prints information about Python lists
 * @p: PyObject (list)
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, alloc, i;
	PyObject *item;

	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - Prints information about Python bytes
 * @p: PyObject (bytes)
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str ? str : "(null)");

	printf("  first 10 bytes: ");
	for (i = 0; i < size && i < 10; i++)
		printf("%02hhx ", str[i]);
	printf("\n");
}

/**
 * print_python_float - Prints information about Python float
 * @p: PyObject (float)
 */
void print_python_float(PyObject *p)
{
	PyFloatObject *float_obj = (PyFloatObject *)p;

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	printf("  value: %f\n", float_obj->ob_fval);
}

