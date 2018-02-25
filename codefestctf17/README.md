# cfctf17

## https://grab-the-fwag.herokuapp.com/

* The `md5` of username is hard coded in js. 
![screenshot](/imgs/grab-the-flag.png)
* Use [md5online](http://www.md5online.org/md5-decrypt.html) to get plain text and get `flag{17_w45_hidd3n_in_p14in_5igh7}`

## http://anonymouscodefest17.pythonanywhere.com/askauth/  

* change the `flag` cookie to false, 
* `Enter`
* Username : `root`
* `md5` of password is cookie pass
* Use [md5online](http://www.md5online.org/md5-decrypt.html) to get password
* Enter to get flag.

![Screenshot](/imgs/cookies.png)

## cr4ck_7hi5_7ce7aa193db6fd41fc3857602e72fc1d

Running `binwalk` will reveal the contents of executable. Run the following commands to get flag:

``` bash
    $ binwalk cr4ck_7hi5_7ce7aa193db6fd41fc3857602e72fc1d
    $ dd if=cr4ck_7hi5_7ce7aa193db6fd41fc3857602e72fc1d of=out.png skip=1536 bs=1
    $ eog out.png
```

## malicious_0a5aca19667459c2b75c384d7a6af48f.zip

Running `binwalk` will reveal the contents of executable. 

```bash
    $ binwalk -e malicious_0a5aca19667459c2b75c384d7a6af48f.zip
    $ cd _malicious_0a5aca19667459c2b75c384d7a6af48f.zip.extracted
    # file.txt contains hex encoded string of flag
    $ python2 -c "print '`cat flag.txt`'.decode('hex')"
    flag{k33p_up_y0ur_zipp3r5}
```

## SimplyBlack_b0c707a6fdf259e468663cebafb84451.png

Title says "50 shades of grey"
Open `gimp` increase brightness and contrast.

![gimp](/imgs/lethal.png)

Flag : `flag{LETHAL}`

## un10ck_m3_a04acef13380d5a9bbc20fddc7dd426c

Run the following commands to get the flag:

```bash
    $ gdb ./un10ck_m3_a04acef13380d5a9bbc20fddc7dd426c
    (gdb) b *0x400686
    (gdb) b *0x400cca
    (gdb) r
    (gdb) set $rip=0x400c8f
    (gdb) c
    (gdb) set $rip=0x400cd0
    (gdb) c
    (gdb) q
```
