#!/bin/bash
cd ~/Downloads/H3K4me3       
nohup nice -n 19 danpos dtriple WT_ChIP:KO_ChIP -b WT_ChIP:WT_Input,KO_ChIP:KO_Input -o analysis_results >> logs/26_4_23.txt &