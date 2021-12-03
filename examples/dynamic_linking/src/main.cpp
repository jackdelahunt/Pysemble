#include "logger/logger.h"

int main() {
    logger_info("Capacitor is at 10%");
    logger_warn("Capacitor is low");
    logger_err("Capacitor is empty");
    return 0;
}