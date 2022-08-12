for n in $(echo | nc mercury.picoctf.net 21135); do
    printf "\\$(printf %03o "$n")";
done
