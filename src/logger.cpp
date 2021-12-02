#include "logger.h"

void reset() {
    printf("\033[0m \n");
}

void log_info(const char* message) {
    printf("\033[0;34m [INFO] %s", message);
    reset();
}

void log_warn(const char* message) {
    printf("\033[0;33m [WARN] %s", message);
    reset();
}

void log_err(const char* message) {
    printf("\033[0;31m [ERROR] %s", message);
    reset();
}