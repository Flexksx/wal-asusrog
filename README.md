# wal-asusrog
A simple script that combines asusctl for ROG and TUF Asus laptops and pywal to get a nice keyboard backlight according to your background
# WIP
Please note that this is a work in progress project, it has just 3 functions, but this is my first time trying to build something for the open source community and contribute. Any help would be highly appreciated.
# Requirements
```pywal``` and ```asusctl```. Install them using your distro's package manager.
# How to run
Until I implement a way of automatic setup:
```
git clone https://github.com/Flexksx/wal-asusrog.git
cd wal-asusrog
chmod +x rogwal.sh
./rogwal.sh help
```

Use ```./rogwal.sh help``` for help. There are currently 3 modes: ```static```, ```breathe``` and ```strobe```. Breathing mode has 3 speed modes ```low, med, high```.
# Limitations
The ```asusctl``` package does not have yet the ability to create custom color gradients like on Windows, but we hope for some updates.
