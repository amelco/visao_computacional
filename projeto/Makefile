CFLAGS = `pkg-config --cflags opencv4`
LIBS= `pkg-config --libs opencv4`

face: face.cpp
		g++ $(CFLAGS) -o face face.cpp $(LIBS)
