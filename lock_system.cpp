#include <iostream>
#include <string>

class SecurityDoorSystem {
private:
    bool hasSpadeKey;
    bool hasEmblemCrest;
    std::string currentSector;

public:
    // Initializer constructor mapping structural states
    SecurityDoorSystem(std::string sector) {
        hasSpadeKey = false;
        hasEmblemCrest = false;
        currentSector = sector;
    }

    void pickUpSpadeKey() {
        hasSpadeKey = true;
        std::cout << "[ITEM_PICKUP] Obtained: Old Iron Spade Key.\n";
    }

    void pickUpEmblemCrest() {
        hasEmblemCrest = true;
        std::cout << "[ITEM_PICKUP] Obtained: Gold Umbrella Crest.\n";
    }

    // Engine loop routine simulating conditional gate access evaluations
    bool checkLockAuthentication() {
        std::cout << "\n[SECURITY SCAN] Checking authorization for sector: " << currentSector << "...\n";
        
        if (hasSpadeKey && hasEmblemCrest) {
            std::cout << "🔓 ACCESS GRANTED: Electronic deadbolts retracted. Door clicks open.\n";
            return true;
        } else {
            std::cout << "🔒 ACCESS DENIED: The mechanism requires the Spade Key and the Gold Crest.\n";
            return false;
        }
    }
};

int main() {
    // Execute tactical check inside the Spencer Mansion sub-sector
    SecurityDoorSystem mansionDoor("East Wing Corridor");
    
    mansionDoor.checkLockAuthentication(); // Will fail initially
    mansionDoor.pickUpSpadeKey();
    mansionDoor.pickUpEmblemCrest();
    mansionDoor.checkLockAuthentication(); // Will succeed
    
    return 0;
}
