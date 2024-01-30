#include "lists.h"

/**
* insert_node - inserts a number into a sorted singly linked list
* @head: h
* @number: data
* Return: the address of the new node, or NULL if it failed
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *nod = malloc(sizeof(listint_t));

	if (!(nod))
		return (NULL);
	nod->n = number;
	nod->next = NULL;
	if (!(temp->next) || number < temp->n)
	{
		nod->next = temp;
		return (*head = nod);
	}
	while (temp)
	{
		if (temp->n <= number && temp->next->n > number)
		{
			nod->next = temp->next;
			temp->next = nod;
			return (nod);
		}
		temp = temp->next;
	}
	return (NULL);
}
