#include "lists.h"

/**
* check_cycle - to check if cycle
* @list: linled list
* Return: 1 if cycle, 0 otherwise
*/

int check_cycle(listint_t *list)
{
	listint_t *hare = head, *tertoise = head;

	while (hare && hare->next)
	{
		tertoise = tertoise->next;
		hare = hare->next->next;
		if (hare == tertoise)
			return (1);
	}
	return (0);
}

