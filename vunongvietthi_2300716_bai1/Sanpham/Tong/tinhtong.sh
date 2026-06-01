#!/bin/bash
tong=0
while IFS=',' read -r ngay doanhthu; do
    if [[ "$doanhthu" =~ ^[0-9]+$ ]]; then
        tong=$((tong + doanhthu))
    fi
done < ~/vunongvietthi_2300716/Sanpham/Doanhthu/doanhso.csv

echo "Tong doanh thu: $tong"
