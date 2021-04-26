#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *ite1 = list;
	listint_t *ite2 = list;

	if (!list)
		return (0);

	while (ite1 && ite2 && ite2->next)
	{
		ite1 = ite1->next;
		ite2 = ite2->next->next;
		if (ite1 == ite2)
			return (1);
	}

	return (0);
}
