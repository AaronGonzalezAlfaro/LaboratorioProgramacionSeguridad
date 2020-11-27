#!/bin/bash

echo "Introduce la Ciudad:"
read a
echo "El clima es: "
curl wttr.in/$a?format=2
