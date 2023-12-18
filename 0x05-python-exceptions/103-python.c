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
	Py_ssize_t size, allocated;
	PyObject *item;

	if (!PyList_Check(p)) {
		printf("[ERROR] Not a list object\n");
		return;
	}

	size = PyList_Size(p);
	allocated = PyList_GET_SIZE(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (int i = 0; i < size; i++) {
		item = PyList_GetItem(p, i);
		printf("Element %d: ", i);

		if (PyBytes_Check(item)) {
			print_python_bytes(item);
		} else if (PyLong_Check(item)) {
			printf("%ld\n", PyLong_AsLong(item));
		} else if (PyFloat_Check(item)) {
			printf("%g\n", PyFloat_AsDouble(item));
		} else if (PyTuple_Check(item)) {
			printf("tuple\n");
		} else if (PyList_Check(item)) {
			printf("list\n");
		} else if (PyUnicode_Check(item)) {
			printf("str\n");
		} else {
			printf("[UNKNOWN TYPE]\n");
		}
	}
}

void print_python_bytes(PyObject *p) {
	Py_ssize_t size;
	char *str;

	if (!PyBytes_Check(p)) {
		printf("[ERROR] Not a bytes object\n");
		return;
	}

	size = PyBytes_GET_SIZE(p);
	str = PyBytes_AS_STRING(p);

	printf("[.] bytes object info\n");
	printf("  size: %zd\n", size);

	if (size > 0) {
		printf("  trying string: %s\n", str);
	}

	if (size > 10) {
		size = 10;
	}

	printf("  first %zd bytes: ", size);
	for (int i = 0; i < size; i++) {
		printf("%02hhx ", (unsigned char)str[i]);
	}
	printf("\n");
}

void print_python_float(PyObject *p) {
	double value;

	if (!PyFloat_Check(p)) {
		printf("[ERROR] Not a float object\n");
		return;
	}

	value = PyFloat_AsDouble(p);

	printf("[.] float object info\n");
	printf("  value: %g\n", value);
}

