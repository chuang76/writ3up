# writ3up
My write-ups and notes about computer security.



## Write-up / Walkthrough

| problem                        | source                    | keyword                                                      | writeup                                                      |
| ------------------------------ | ------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| fd                             | pwnable.kr                | file descriptor                                              | [link](https://github.com/chuang76/writ3up/blob/main/pwnable-kr/fd.md) |
| collision                      | pwnable.kr                | MD5                                                          | [link](https://github.com/chuang76/writ3up/blob/main/pwnable-kr/collision.md) |
| bof                            | pwnable.kr                | buffer overflow                                              | [link](https://github.com/chuang76/writ3up/blob/main/pwnable-kr/bof.md) |
| flag                           | pwnable.kr                | UPX packer                                                   | [link](https://github.com/chuang76/writ3up/blob/main/pwnable-kr/flag.md) |
| passcode                       | pwnable.kr                | GOT                                                          | [link](https://chuang76.github.io/posts/passcode/)           |
| input                          | pwnable.kr                | execve, pipe, I/O redirection, socket                        | [link](https://chuang76.github.io/posts/input/)              |
| leg                            | pwnable.kr                | ARM instruction set                                          | [link](https://chuang76.github.io/posts/leg/)                |
| mistake                        | pwnable.kr                | operator priority                                            | [link](https://chuang76.github.io/posts/mistake/)            |
| shellshock                     | pwnable.kr                | shellshock, CVE-2014-6271                                    | [link](https://chuang76.github.io/posts/shellshock/)         |
| payload                        | Practical Binary Analysis | ELF format, basic binary analysis                            | [link](https://chuang76.github.io/posts/payload/)            |
| nebula (level 0 - 2)           | VulnHub                   | permission, Set-UID, env variable                            | [link](https://chuang76.github.io/posts/nebula_p1/)          |
| nebula (level 3)               | VulnHub                   | cron job, crontab                                            | [link](https://chuang76.github.io/posts/nebula_p2/)          |
| nebula (level 4)               | VulnHub                   | symbolic link                                                | [link](https://chuang76.github.io/posts/nebula_p2/)          |
| nebula (level 5)               | VulnHub                   | SSH, public-key cryptography                                 | [link](https://chuang76.github.io/posts/nebula_p2/)          |
| nebula (level 6)               | VulnHub                   | /etc/passwd, /etc/shadow, John the Ripper                    | [link](https://chuang76.github.io/posts/nebula_p3/)          |
| nebula (level 7)               | VulnHub                   | CGI module, thttpd web server                                | [link](https://chuang76.github.io/posts/nebula_p3/)          |
| nebula (level 8)               | VulnHub                   | TCP, packet analysis                                         | [link](https://chuang76.github.io/posts/nebula_p3/)          |
| nebula (level 10)              | VulnHub                   | TOCTOU, race condition vulnerability                         | [link](https://chuang76.github.io/posts/nebula_p4/)          |
| babysuid                       | pwn.college               | abusing Linux SUID                                           | [link](https://github.com/chuang76/writ3up/blob/main/pwn-college/babysuid.md) |
| babyshell                      | pwn.college               | shellcode injection                                          | [link](https://github.com/chuang76/writ3up/blob/main/pwn-college/babyshell.md) |
| babymem                        | pwn.college               | memory corruption                                            | [link](https://github.com/chuang76/writ3up/blob/main/pwn-college/babymem.md) |
| Rocca pia                      | DaVinciCTF 2021           | XOR cipher                                                   | [link](https://github.com/chuang76/writ3up/tree/main/davinci) |
| Beleaf                         | CSAW'19                   | reverse engineering                                          | [link](https://hackmd.io/dIPns5reRB-THaUlh14WPQ?view#03-CSAW%E2%80%9919-Beleaf) |
| Boi                            | CSAW’18 Quals             | stack buffer overflow                                        | [link](https://hackmd.io/dIPns5reRB-THaUlh14WPQ?view#04-CSAW%E2%80%9918-Quals-Boi) |
| Pwn1                           | TAMU'19                   | stack buffer overflow                                        | [link](https://hackmd.io/dIPns5reRB-THaUlh14WPQ?view#04-TAMU%E2%80%9919-Pwn1) |
| JustDoIt                       | TokyoWesterns’17          | stack buffer overflow                                        | [link](https://hackmd.io/dIPns5reRB-THaUlh14WPQ?view#04-TokyoWesterns%E2%80%9917-JustDoIt) |
| Warmup                         | CSAW'16                   | stack buffer overflow                                        | [link](https://hackmd.io/dIPns5reRB-THaUlh14WPQ?view#05-CSAW%E2%80%9916-Warmup) |
| GetIt                          | CSAW’18 Quals             | stack buffer overflow                                        | [link](https://hackmd.io/dIPns5reRB-THaUlh14WPQ?view#05-CSAW%E2%80%9918-Quals-Getit) |
| Vulnchat                       | TUCFT’17                  | stack buffer overflow                                        | [link](https://hackmd.io/dIPns5reRB-THaUlh14WPQ?view#05-TUCFT%E2%80%9917-Vulnchat) |
| Pilot                          | CSAW'17                   | stack buffer overflow, shellcode injection                   | [link](https://hackmd.io/ECOMk9XpTeKypPQ9YiNGpw?view#06-CSAW%E2%80%9917-Pilot) |
| Pwn3                           | TAMU'19                   | stack buffer overflow, shellcode injection                   | [link](https://hackmd.io/ECOMk9XpTeKypPQ9YiNGpw?view#06-TAMU%E2%80%9919-Pwn3) |
| Shella-easy                    | TUCTF’18                  | stack buffer overflow, shellcode injection                   | [link](https://hackmd.io/ECOMk9XpTeKypPQ9YiNGpw?view#06-TUCTF%E2%80%9918-Shella-easy) |
| Free flag                      | ångstromCTF 2021          | reverse engineering                                          | [link](https://github.com/chuang76/writ3up/tree/main/angstrom#%C3%A5ngstromctf-2021---free-flags1-50-points) |
| Tranquil                       | ångstromCTF 2021          | stack buffer overflow                                        | [link](https://github.com/chuang76/writ3up/tree/main/angstrom#%C3%A5ngstromctf-2021---tranquil-70-points) |
| Sanity checks                  | ångstromCTF 2021          | stack buffer overflow                                        | [link](https://github.com/chuang76/writ3up/tree/main/angstrom#%C3%A5ngstromctf-2021---sanity-checks-80-points) |
| Simple calc                    | Boston Key Part’16        | stack buffer overflow, ROP chain                             | [link](https://hackmd.io/ECOMk9XpTeKypPQ9YiNGpw#07-Boston-Key-Part%E2%80%9916-Simple-Calc) |
| Necromancer: level 1 - level 6 | VulnHub                   | port scan (nmap), hash decryption, web content scanner (dirbuster), wireshark/tshark | [link](https://hackmd.io/BbmvwE7fSJq54no4g3SUQA?view#Flag-1---Flag-6) |
| Protostar: heap0               | VulnHub                   | heap overflow                                                | [link](https://hackmd.io/ECOMk9XpTeKypPQ9YiNGpw#24-Protostar-heap0) |
| NullByte                       | VulnHub                   | web, stego (exiftool), SQL injection (sqlmap), crack passwords (hydra), abusing SUID | [link](https://hackmd.io/aOQnJSi2SQmgXCfggWIGQQ?view)        |



## Technical note

| title                                | keyword                                | date    | note                                                       |
| ------------------------------------ | -------------------------------------- | ------- | ---------------------------------------------------------- |
| Lazy Binding                         | lazy binding, PLT, GOT                 | 2020/12 | [link](https://chuang76.github.io/posts/lazy_binding/)     |
| Users and Groups                     | permission, /etc/passwd                | 2020/12 | [link](https://chuang76.github.io/posts/users_and_groups/) |
| Stack Buffer Overflow                | buffer overflow, shellcode             | 2021/01 | [link](https://chuang76.github.io/posts/bof/)              |
| Return-to-libc Attack                | ret2libc                               | 2021/02 | [link](https://chuang76.github.io/posts/return-to-libc/)   |
| Return-Oriented Programming          | skip prologue, leave ret, ROP chain    | 2021/02 | [link](https://chuang76.github.io/posts/rop/)              |
| Firmware: Breaking Encryption Scheme | AES encryption, file system extraction | 2021/04 | [link](https://hackmd.io/XAvS9IuRTD6-HIiQCaOnQA?view)      |
