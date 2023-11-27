#include "lists.h"

/**
 * check_cycle - Checks if a linked list has a cycle
 * @list: is the pointer to the head of the linked list
 *
 * Return: 1 if a cycle is detected, otherwise 0
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise = list;
	listint_t *hare = list;

	while (tortoise != NULL && hare != NULL && hare->next != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;

		if (tortoise == hare)
			return (1);
	}
	return (0);
}
