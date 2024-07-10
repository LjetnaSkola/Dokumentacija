CC = gcc
CFLAGS = -Wall -Wextra
TARGET = main
SRCDIR = src
OBJDIR = obj

SOURCES = $(SRCDIR)/List.c $(SRCDIR)/Main.c

OBJECTS = $(patsubst $(SRCDIR)/%.c,$(OBJDIR)/%.o,$(SOURCES))

$(TARGET): $(OBJECTS)
	$(CC) $(CFLAGS) $^ -o $@

$(OBJDIR)/%.o: $(SRCDIR)/%.c | $(OBJDIR)
	$(CC) $(CFLAGS) -c $< -o $@

$(OBJDIR):
	mkdir -p $(OBJDIR)

clean:
	rm -f $(OBJDIR)/*.o $(TARGET)

.PHONY: clean