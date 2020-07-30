CFLAGS = `pkg-config --cflags opencv4`
LIBS= `pkg-config --libs opencv4`

eyes: eyes.cpp
		g++ $(CFLAGS) -o eyes eyes.cpp $(LIBS)
