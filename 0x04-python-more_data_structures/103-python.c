#include <Python.h>
#include <listobject.h>
#include <bytesobject.h>
#include <object.h>

void print_python_bytes(PyObject *p)
{
	long int size_obj;
	int itr;
	char *str_obj = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &str_obj, &size_obj);

	printf("  size: %li\n", size_obj);
	printf("  trying string: %s\n", str_obj);
	if (size_obj < 10)
		printf("  first %li bytes:", size_obj + 1);
	else
		printf("  first 10 bytes:");
	for (itr = 0; itr <= size_obj && itr < 10; itr++)
		printf(" %02hhx", str_obj[itr]);
	printf("\n");
}

void print_python_list(PyObject *p)
{
	long int size_obj = PyList_Size(p);
	int itr;
	PyListObject *list = (PyListObject *)p;
	const char *type;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", size_obj);
	printf("[*] Allocated = %li\n", list->allocated);
	for (itr = 0; itr < size_obj; itr++)
	{
		type = (list->ob_item[itr])->ob_type->tp_name;
		printf("Element %i: %s\n", itr, type);
		if (!strcmp(type, "bytes"))
			print_python_bytes(list->ob_item[itr]);
	}
}
