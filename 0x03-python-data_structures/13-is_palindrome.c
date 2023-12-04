#include "lists.h"

/**
 * is_palindrome - Find out if a singly linked list is a palindrome
 * @head: pointer to the head
 * Return: 1 if it is a palindrome, else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *reverse, *mid_ptr;
	size_t size = 0, index;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		size++;
		temp = temp->next;
	}

	temp = *head;
	for (index = 0; index < (size / 2) - 1; index++)
		temp = temp->next;

	if ((size % 2) == 0 && temp->n != temp->next->n)
		return (0);

	temp = temp->next->next;
	reverse = reverse_listint(&temp);
	mid_ptr = reverse;

	temp = *head;
	while (reverse)
	{
		if (temp->n != reverse->n)
			return (0);
		temp = temp->next;
		reverse = reverse->next;
	}
	reverse_listint(&mid_ptr);

	return (1);
}

/**
 * reverse_listint - Function to reverse the singly-linked list.
 * @head: A pointer to head.
 *
 * Return: The pointer to the head
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node_ptr = *head, *next, *previous_ptr = NULL;

	while (node_ptr)
	{
		next = node_ptr->next;
		node_ptr->next = previous_ptr;
		previous_ptr = node_ptr;
		node_ptr = next;
	}

	*head = previous_ptr;
	return (*head);
}
