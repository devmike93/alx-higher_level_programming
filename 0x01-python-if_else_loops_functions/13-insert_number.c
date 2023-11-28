#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a new_node node into a sorted singly linked list
 * @head: is the pointer to a pointer to the head of the linked list
 * @number: the value to be inserted into the new_node node
 *
 * Return: a pointer to the newly inserted node, or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new_node;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	current = *head;
	while (current->next != NULL && current->next->n <= number)
	{
		current = current->next;
	}

	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
