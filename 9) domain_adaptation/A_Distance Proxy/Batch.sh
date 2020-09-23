#!/bin/bash
date '+%d/%m/%Y %H:%M:%S';
echo " > Running..";
python proxy-a-distance-master/main.py mantis_to_erp_next/mantis_en_issues_sentences.txt mantis_to_erp_next/mantis_en_issues_sentences.txt mantis_to_erp_next/erp_next_issues_sentences.txt mantis_to_erp_next/erp_next_issues_sentences.txt mantis_to_erp_next/Vocab_erp_next_issues_mantis_en_issues.txt > outputs/erp_next.txt;

echo " All Done. ";
