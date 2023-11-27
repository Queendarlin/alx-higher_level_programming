#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle.
 * @list: A pointer to the head of the linked list.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		/* If there's a cycle, the pointers will meet at some point */
		if (slow == fast)
			return 1;
	}

	/* If the loop completes without meeting, there is no cycle */
	return 0;
}
