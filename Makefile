##
## EPITECH PROJECT, 2020
## tmp_evalexpr
## File description:
## Makefile
##


CC	=	python

NAME	=	challenge01 challenge02 challenge03 challenge04 challenge05 challenge07 challenge08 challenge09

all:	$(NAME)

first:
	cp hex_to_base64.py challenge01
	chmod 777 challenge01

second:
	cp hex_to_xor.py challenge02
	chmod 777 challenge02

third:
	cp challenge03.py challenge03
	chmod 777 challenge03

forth:
	cp challenge04.py challenge04
	chmod 777 challenge04

fifth:
	cp challenge05.py challenge05
	chmod 777 challenge05

seventh:
	cp challenge07.py challenge07
	chmod 777 challenge07

eigth:
	cp challenge08.py challenge08
	chmod 777 challenge08

nineth:
	cp challenge09.py challenge09
	chmod 777 challenge09

$(NAME): first second third forth fifth seventh eigth nineth

clean:
	rm $(NAME)

fclean:	clean
	rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re