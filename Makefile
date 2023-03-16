# the compiler: gcc for C program, define as g++ for C++
CC = g++

# compiler flags:
#  -g     - this flag adds debugging information to the executable file
#  -Wall  - this flag is used to turn on most compiler warnings
CPPFLAGS  = -Wall

# The build target 
TARGET = helloWorld

all: $(TARGET)

$(TARGET): $(TARGET).cpp
	$(CC) $(CPPFLAGS) $(TARGET).cpp -o build/$(TARGET).o 

clean:
	$(RM) build/$(TARGET).o
