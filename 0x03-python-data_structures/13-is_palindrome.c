#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * reverse - reverses a listint_t linked list.
 * @head: pointer of the pointer that points to structs.
 *
 * Return: a pointer to the first node of the reversed list.
 */
listint_t *reverse(listint_t **head)
{
	listint_t *tmp = NULL;
	listint_t *hold = NULL;

	while (*head)
	{
		hold = (*head)->next;
		(*head)->next = tmp;
		tmp = *head;
		*head = hold;
	}
	(*head) = tmp;
	return (*head);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to the pointer that point to struct.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *tmp = NULL;
	listint_t *tmp2 = NULL;

	if (!*head)
		return (1);
	while (fast && fast->next && fast->next->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	tmp = reverse(&slow);
	tmp2 = tmp;
	fast = *head;
	while (tmp && fast)
	{
		if (tmp->n != fast->n)
			return (0);
		fast = fast->next;
		tmp = tmp->next;
	}
	reverse(&tmp2);
	return (1);
}
