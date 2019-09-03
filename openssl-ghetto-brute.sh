for pwd in $(cat /rockyou.txt)
    do openssl enc -aes-256-cbc -d -a -in secrets.txt.enc -out file.txt -k $pwd
    if [ $? -eq 0 ]
    then
        echo the password is $pwd
        exit 1
    fi
done
