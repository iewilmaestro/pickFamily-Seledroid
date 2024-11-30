# pickFamily-Seledroid

## NOTE
- only works in termux

## Register

- [x] [litepick](https://litepick.io/?ref=anjim128)
- [x] [bnbpick](https://bnbpick.io/?ref=iewilmaestro)
- [x] [tronpick](https://tronpick.io/?ref=iewilmaestro)
- [x] [tonpick](https://tonpick.game/?ref=iewilmaestro)

## Add More Url
- you can add url here, but you need to clear output.json after adding url so that new url is detected
```python
hosts = [
"https://litepick.io/",
"https://tronpick.io/",
"https://bnbpick.io/",
"https://tonpick.game/",
"xxx", #new url
"xxx" #new url
]
```

## Download

- Termux -> [F-Droid](https://f-droid.org/packages/com.termux/).

## Requirements

| Step | Command                                                               |
| ---- | --------------------------------------------------------------------- |
| 1    | Open Termux                                                           |
| 2    | Allow access to storage memory                                        |
| 3    | <pre><code>termux-setup-storage</code></pre>                          |
| 4    | Force exit Termux                                                     |
| 5    | Reopen Termux                                                         |
| 6    | Update & Upgrade package (Opsional)                                              |
| 7    | <pre><code>yes \| pkg update -y && yes \| pkg upgrade -y</code></pre> |
| 8    | Install python                       |
| 9    | <pre><code>yes \| pkg install python -y</code></pre>              |
| 10   | Install seledroid                                                      |
| 11   | <pre><code>pip install seledroid</code></pre>                   |
| 12   | Download & Install Chromium Seledroid                |
| 13   | [Chromium Seledroid](https://github.com/luanon404/Seledroid-Chromium/releases/tag/v2.0.3)               |
| 14   | Install git                      |
| 15   | <pre><code>pkg install git</code></pre>                   |
| 16   | Clone Script                   |
| 17   | <pre><code>git clone https://github.com/iewilmaestro/pickFamily-Seledroid</code></pre>                   |
| 18   | <pre><code>cd pickFamily-Seledroid</code></pre>                   |
| 19   | <pre><code>python pickFamily.py</code></pre>                   |


