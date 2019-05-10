#include<Python.h>
#include<stdio.h>
/**
 * print_python_list_info - print python list
 * @p: a pointer to an object.
 */
void print_python_list_info(PyObject *p)
{
	size_t i;
	size_t j = Py_SIZE(p);

	PyListObject *a = (PyListObject *)p;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", a->allocated);
	for (i = 0; i < j; i++)
		printf("Element %lu: %s\n", i, Py_TYPE(a->ob_item[i])->tp_name);
}
