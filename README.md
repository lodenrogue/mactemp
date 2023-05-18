## Mac M1/M2 Sensors

### How to build

```
clang -Wall -v temp_sensor.m -framework IOKit -framework Foundation -o temp_sensor
```

### How to get average CPU temperature

```
./temp_sensor | ./cpu_temp.py
```