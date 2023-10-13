#!/bin/bash
read -p "Digite a mensagem de commit: " mensagem
git add .
git commit -m "$mensagem"
git push