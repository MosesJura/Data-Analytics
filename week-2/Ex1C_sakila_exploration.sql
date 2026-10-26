/*
a)The actor table stores each actor's unique ID, first name, last name, and last-update timestamp.
b) The film table stores each film's ID, title, description,
 release year, language, rental details (duration, rate, length, replacement cost), 
 rating, special features, and last-update timestamp.
c) The film_actor table contains both actor_id and film_id, 
acting as a bridge to resolve the many-to-many relationship between films and actors.
d) The rental table records each rental transaction:
 rental_id, rental_date, inventory_id, customer_id, return_date, staff_id, last_update. 
 It's hard to read because it uses surrogate IDs, so you can't tell which film or
 customer without joining other tables.
e) The inventory table lists each physical copy of a film (inventory_id),
 which film it is (film_id), and which store holds it (store_id), plus last_update.
f) To find the names of all films rented on a specific date, 
  I need rental, inventory, and film. rental holds rental_date and 
  inventory_id; inventory maps inventory_id to film_id; film maps film_id to title. 
 They are related by foreign keys: rental.inventory_id → inventory.inventory_id, and 
inventory.film_id → film.film_id.
*/


USE sakila;
SELECT rental_date, inventory_id FROM rental;
SELECT inventory_id, film_id FROM inventory;
SELECT film_id, title FROM film;
