#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the linked list
 * Return: 1 if it is a palindrome, else 0
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	listint_t *slow_ptr = *head;
	listint_t *fast_ptr = *head;
	listint_t *prev_slow = NULL;
	listint_t *second_half = NULL;
	listint_t *temp;

	while (fast_ptr != NULL && fast_ptr->next != NULL)
	{
		fast_ptr = fast_ptr->next->next;

		temp = slow_ptr->next;
		slow_ptr->next = prev_slow;
		prev_slow = slow_ptr;
		slow_ptr = temp;
	}

	if (fast_ptr != NULL)
		slow_ptr = slow_ptr->next;

	second_half = slow_ptr;

	while (second_half != NULL)
	{
		if (prev_slow->n != second_half->n)
			return (0);

		prev_slow = prev_slow->next;
		second_half = second_half->next;
	}

	return (1);
}
