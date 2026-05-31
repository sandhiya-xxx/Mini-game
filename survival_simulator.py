import random
import json
import time

class SurvivorUnit:
    def __init__(self, name, health, attack, defense, classification):
        self.name = name
        self.max_health = health
        self.health = health
        self.attack = attack
        self.defense = defense
        self.classification = classification
        self.is_alive = True

    def receive_viral_strike(self, raw_dmg):
        mitigated = max(2, raw_dmg - (self.defense // 3))
        self.health = max(0, self.health - mitigated)
        if self.health <= 0:
            self.is_alive = False
        return mitigated

class OutbreakSimulationEngine:
    @staticmethod
    def run_bioweapon_encounter(hero: SurvivorUnit, bow: SurvivorUnit):
        print(f"☣️ ALERT: DANGER LEVEL RED // CONTACT RECORDED: {hero.name} vs {bow.name} ☣️\n")
        tick = 1
        
        while hero.is_alive and bow.is_alive:
            print(f"[System Scan Step {tick}]")
            
            # Survivor fires weapon
            headshot_crit = 3 if random.random() < 0.15 else 1
            hero_damage = random.randint(hero.attack - 4, hero.attack + 4) * headshot_crit
            delivered = bow.receive_viral_strike(hero_damage)
            print(f"🔫 {hero.name} discharges weapon at {bow.name} for {delivered} damage! {'(CRITICAL HEADSHOT!)' if headshot_crit == 3 else ''}")
            
            if not bow.is_alive:
                print(f"💀 Target Threat {bow.name} has been neutralized.")
                break
                
            # B.O.W Attacks back
            bow_damage = random.randint(bow.attack - 3, bow.attack + 3)
            delivered = hero.receive_viral_strike(bow_damage)
            print(f"🧟 {bow.name} strikes {hero.name} dealing {delivered} systemic damage!")
            
            if not hero.is_alive:
                print(f"💀 Casualty Warning: Outbreak response unit {hero.name} has died.")
                break
                
            print(f"📊 VITAL METRICS -> {hero.name}: {hero.health}/{hero.max_health} HP | {bow.name}: {bow.health}/{bow.max_health} HP\n")
            tick += 1
            time.sleep(0.4)

        return {
            "surviving_entity": hero.name if hero.is_alive else bow.name,
            "simulation_ticks": tick,
            "remaining_vitality": hero.health if hero.is_alive else bow.health
        }

if __name__ == "__main__":
    player = SurvivorUnit("Leon S. Kennedy", health=100, attack=25, defense=12, classification="S.T.A.R.S.")
    monster = SurvivorUnit("Nemesis T-Type", health=300, attack=22, defense=18, classification="B.O.W.")
    
    report_data = OutbreakSimulationEngine.run_bioweapon_encounter(player, monster)
    print("\n💾 METRIC DISPATCH LOG READY FOR GITHUB TRACKING:")
    print(json.dumps(report_data, indent=2))
