#include "lists.h"

/**
* insert_node - inserts a number into a sorted singly linked list
* @head: h
* @number: data
* Return: the address of the new node, or NULL if it failed
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head, *make = *head;
	listint_t *nod = malloc(sizeof(listint_t));

	if (!(nod))
		return (NULL);
	nod->n = number;
	nod->next = NULL;
	if (!(temp->next))
	{
		if (temp->n > number)
			nod->next = *head;
		else
			(*head)->next = nod;
	}
	while (temp->next)
	{
		if (temp->n <= number)
		{
			make = temp;
			temp = temp->next;
			if (temp->n > number)
			{
				make->next = nod;
				nod->next = temp;
				return (nod);
			}
		}
		else
		{
			nod->next = temp;
			make = temp;
			temp = temp->next;
			if (temp->n < number)
				
			temp = temp->next;
	}
	if (temp->n > number)
		nod->next = *head;
	else
		(*head)->next = nod;
	return (nod);
}
