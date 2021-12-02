#include "logger.h"

int main() {
    log_info("Capacitor is at 5%");
    log_warn("Capacitor is low");
    log_err("Capacitor is empty");
    return 0;
}