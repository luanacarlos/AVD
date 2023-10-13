#!/bin/bash
read -p "Mensagem de commit: " mensagem
git add .
git commit -m "$mensagem"
git push