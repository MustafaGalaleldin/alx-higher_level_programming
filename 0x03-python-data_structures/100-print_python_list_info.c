#include <Python.h>
/**
 * print_python_list_info - function that prints some basic
 * info about Python lists
 * @p: Python list
 */
void print_python_list_info(PyObject *p)
{
	int elem;

	printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));

	// Use PyList_Size to get the size of the list (same as Py_SIZE)
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	// Loop through the list elements
	for (elem = 0; elem < Py_SIZE(p); elem++)
		printf("Element %d: %s\n", elem, Py_TYPE(PyList_GetItem(p, elem))->tp_name);
}
