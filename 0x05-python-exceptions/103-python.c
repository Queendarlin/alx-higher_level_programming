#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Print information about a Python list
 * @p: A pointer to a PyObject representing a Python list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, allocate, index;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	allocate = list->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocate);

	for (index = 0; index < size; index++)
	{
		type = list->ob_item[index]->ob_type->tp_name;
		printf("Element %ld: %s\n", index, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[index]);
		else if (strcmp(type, "float") == 0)
			print_python_float(list->ob_item[index]);
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

