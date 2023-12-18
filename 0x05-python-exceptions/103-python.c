#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Print information about a Python list.
 * @p: A pointer to a PyObject representing a Python list.
 */
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		fprintf(stderr, "[*] Invalid List Object\n");
		return;
	}

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", ((PyVarObject *)p)->ob_size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	Py_ssize_t i;

	for (i = 0; i < ((PyVarObject *)p)->ob_size; ++i)
	{
		PyObject *item = ((PyListObject *)p)->ob_item[i];

		printf("Element %ld: ", i);

		if (PyBytes_Check(item))
		{
			print_python_bytes(item);
		}
		else if (PyFloat_Check(item))
		{
			print_python_float(item);
		}
		else if (PyLong_Check(item))
		{
			printf("int\n");
		}
		else if (PyTuple_Check(item))
		{
			printf("tuple\n");
		}
		else if (PyList_Check(item))
		{
			print_python_list(item);
		}
		else if (PyUnicode_Check(item))
		{
			printf("str\n");
		}
		else
		{
			printf("[ERROR] Unknown Object Type\n");
		}
	}
}

/**
 * print_python_bytes - Print information about a Python bytes object.
 * @p: A pointer to a PyObject representing a Python bytes object.
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[.] bytes object info\n  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: ");

	PyObject *bytes_array = PySequence_Fast(p, "[.] bytes object info");
	Py_ssize_t i;

	if (bytes_array != NULL)
		{
		for (i = 0; i < PySequence_Fast_GET_SIZE(bytes_array) && i < 10; ++i)
		{
			printf("%02x ",
					(unsigned char)PyLong_AsLong(PySequence_Fast_GET_ITEM(bytes_array, i)));
		}
		Py_DECREF(bytes_array);
	}

	printf("\n");
}

/**
 * print_python_float - Print information about a Python float object.
 * @p: A pointer to a PyObject representing a Python float object.
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "[.] float object info\n  [ERROR] Invalid Float Object\n");
		return;
	}

	printf("[.] float object info\n");
	printf("  value: %f\n", ((PyFloatObject *)p)->ob_fval);
}
