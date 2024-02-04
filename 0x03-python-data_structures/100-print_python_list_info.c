/*#include <stdlib.h>
#include <stdio.h>
#include <Python.h>
**
 * print_python_list_info -  function that prints some basic
 *						info about Python lists
 * @p: python list
 *
void print_python_list_info(PyObject *p)
{
	int elem;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (elem = 0; elem < Py_SIZE(p); elem++)
		printf("Element %d: %s\n", elem, Py_TYPE(PyList_GetItem(p, elem))->tp_name);
}*/
#include <stdlib.h>
#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - function that prints some basic
 * info about Python lists
 * @p: Python list
 */
void print_python_list_info(PyObject *p)
{
    if (!PyList_Check(p))
    {
        printf("[*] Failed to retrieve the list!\n");
        return;
    }

    printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));

    // Use PyList_Size to get the size of the list (same as Py_SIZE)
    printf("[*] Allocated = %ld\n", PyList_Size(p));

    // Loop through the list elements
    for (int i = 0; i < PyList_Size(p); i++)
    {
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %d: %s\n", i, item ? Py_TYPE(item)->tp_name : "<NULL>");
    }
}

