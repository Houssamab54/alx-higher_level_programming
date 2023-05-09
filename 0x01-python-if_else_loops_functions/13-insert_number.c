#include <stdlib.h>
#include "lists.h"

#include <stdlib.h>

/**
 * insert_node - inserts a node while keeping the list sorted
 * @head: pointer to a pointer to the first node of the list
 * @number: the number to be inserted
 *
 * Return: the new node or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node = malloc(sizeof(listint_t));
listint_t *current;

if (!new_node)
return (NULL);
new_node->n = number;
new_node->next = NULL;
if (!*head || number < (*head)->n)
{
new_node->next = *head;
*head = new_node;
return (new_node);
}
current = *head;
while (current->next && number > current->next->n)
{
current = current->next;
}
new_node->next = current->next;
current->next = new_node;
return (new_node);
}
