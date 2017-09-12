# Binary Clock

A Binary Watch Presentation in Terminal

### install

```bash
$ pip install bwatch --upgrade
# or
$ sudo install bwatch --upgrade
# if permission issue happened on mac os
$ pip install bwatch --user --upgrade
```

### usage

```bash
bwatch
```

#### i. help

```bash
bwatch -h # bwatch --help
```

#### ii. version

```bash
bwatch -v # bwatch --version
```

#### iii. change theme

```bash
bwatch -t THEME # bwatch --theme THEME
```

check out theme list:

```bash
bwatch -l # bwatch --list-theme
```

eg:

![](https://static.hellflame.net/resource/5cee0ec2048f267969286c887dff210a)

![](https://static.hellflame.net/resource/ad395e206dc6b438bc8fb98b8599a610)

#### iv. show a glimpse

> show present time then stop

```bash
bwatch -g # bwatch --glimpse
```

#### v. supress color display(harder to read)

```bash
bwatch -nc # bwatch --no-color
```

![](https://static.hellflame.net/resource/2b2209f2a82cc7b0e64d97d9cc24e850)

#### vi. show full date and time

> column means can be found by using `bwatch —hint -f`

```bash
bwatch -f # bwatch --full
```

![](https://static.hellflame.net/resource/81f431b429215542ca952edbdbfce00c)

#### vii. show hint(normal digital watch)

```bash
bwatch --hint
```

![](https://static.hellflame.net/resource/66740ccd22ff360f9bdbfb6024b093ab)

#### Combine

```bash
bwatch -f --hint
bwatch -f -t basic
bwatch -g --hint
...
```

For Fun Only!

