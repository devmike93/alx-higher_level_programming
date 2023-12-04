#include "lists.h"

/**
 * reverse - reverses a listint_t linked list.
 * @head: a pointer to the head of the linked list.
 *
 * Return: a pointer to the first node of the reversed list.
 */
listint_t *reverse(listint_t *head)
{
	listint_t *current = head;
	listint_t *prev = NULL;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next; /* Store the next node */
		current->next = prev; /* Reverse the pointer direction */

		/* Move pointers one step ahead */
		prev = current;
		current = next;
	}

	/* Update the new head of the reversed list */
	head = prev;

	return (head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: a double pointer to the head of the linked list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *tortoise, *hare, *middle_node;

	tortoise = hare = *head;

	if (*head == NULL || head == NULL)
		return (1);

	while (hare != NULL && hare->next != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
	}

	middle_node = reverse(tortoise);

	while (middle_node != NULL)
	{
		if ((*head)->n != middle_node->n)
			return (0);
		*head = (*head)->next;
		middle_node = middle_node->next;
	}

	return (1);
}
