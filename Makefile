# the compiler: gcc for C program, define as g++ for C++
CC = g++

# compiler flags:
#  -g     - this flag adds debugging information to the executable file
#  -Wall  - this flag is used to turn on most compiler warnings
CPPFLAGS  = -Wall

# The build target 
TARGET = helloWorld
FUNC1 = other

all: $(TARGET)

$(TARGET): src/$(TARGET).cpp
	$(CC) $(CPPFLAGS) src/$(TARGET).cpp src/$(FUNC1).cpp -o build/$(TARGET).o 

clean:
	$(RM) build/$(TARGET).o
