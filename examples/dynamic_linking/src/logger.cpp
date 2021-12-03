#include <stdio.h>

void reset() {
    printf("\033[0m \n");
}

void logger_info(const char* message) {
    printf("\033[0;34m %s", message);
    reset();
}

void logger_warn(const char* message){
    printf("\033[0;33m %s", message);
    reset();
}

void logger_err(const char* message){
    printf("\033[0;31m %s", message);
    reset();
}