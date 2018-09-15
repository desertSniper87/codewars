SELECT actor_table_a.first_name, actor_table_a.last_name,
actor_table_b.first_name, actor_table_b.last_name
FROM actor AS actor_table_a
JOIN 
(
    SELECT a.actor_id AS a, b.actor_id AS b, COUNT(a.film_id) AS c
    FROM film_actor AS a
    JOIN film_actor AS b
    ON a.film_id=b.film_id
    GROUP BY a, b
    ORDER BY c
    LIMIT 1
) AS c
ON a.actor_id=actor_table_a.actor_id
JOIN actor AS actor_table_b
ON a.actor_id=actor_table_b.actor_id;


