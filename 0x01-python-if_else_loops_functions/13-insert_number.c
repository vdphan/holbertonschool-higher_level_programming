#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 *insert_node - inserts a number into a sorted singly linked list.
 *@head: pointer to the pointer of head.
 *@number: the number that need to insert.
 *
 *Return: the address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp;
	listint_t *s = NULL;

	tmp = *head;
	s = malloc(sizeof(listint_t));
	if (!s)
		return (NULL);
	s->n = number;
	s->next = NULL;
	if(!*head)
	{
		*head = s;
		return (*head);
	}
	if (tmp->n > number)
	{
		s->next = tmp;
		*head = s;
		return (*head);
	}
	while (tmp->next && tmp->next->n < number)
		tmp = tmp->next;
	s->next = tmp->next;
	tmp->next = s;
	return (tmp);
}
