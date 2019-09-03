#!/bin/bash
for word in ` cat rockyou.txt `
do
    steghide extract -sf stego.jpg -p $word
done
