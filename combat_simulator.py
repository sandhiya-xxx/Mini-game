import random
import json
import time

class GameCharacter:
    def __init__(self, name, health, attack, defense, faction):
        self.name = name
        self.max_health = health
        self.health = health
        self.attack = attack
        self.defense = defense
        self.faction = faction
        self.is_alive = True

    def take_damage(self, raw_damage):
        # Game calculation: mitigate raw incoming damage using internal defense values
        mitigated_damage = max(1, raw_damage - (self.defense // 2))
        self.health = max(0, self.health - mitigated_damage)
        if self.health <= 0:
            self.is_alive = False
        return mitigated_damage

class CombatEngine:
    @staticmethod
    def execute_turn_based_battle(hero: GameCharacter, villain: GameCharacter):
        print(f"⚔️ BATTLE INITIATED: {hero.name} vs {villain.name} ⚔️\n")
        round_counter = 1
        
        while hero.is_alive and villain.is_alive:
            print(f"--- Round {round_counter} ---")
            
            # Hero attacks villain with RNG critical calculation
            crit_multiplier = 2 if random.random() < 0.2 else 1
            hero_raw_dmg = random.randint(hero.attack - 3, hero.attack + 3) * crit_multiplier
            absorbed = villain.take_damage(hero_raw_dmg)
            print(f"💥 {hero.name} strikes {villain.name} for {absorbed} damage! {'(CRITICAL!)' if crit_multiplier == 2 else ''}")
            
            if not villain.is_alive:
                print(f"💀 {villain.name} has been vanquished!")
                break
                
            # Villain retaliates
            villain_raw_dmg = random.randint(villain.attack - 2, villain.attack + 2)
            absorbed = hero.take_damage(villain_raw_dmg)
            print(f"👹 {villain.name} counter-attacks {hero.name} for {absorbed} damage!")
            
            if not hero.is_alive:
                print(f"💀 {hero.name} fell in battle...")
                break
                
            print(f"❤️ {hero.name}: {hero.health}/{hero.max_health} HP | {villain.name}: {villain.health}/{villain.max_health} HP\n")
            round_counter += 1
            time.sleep(0.5)

        return {
            "winner": hero.name if hero.is_alive else villain.name,
            "rounds": round_counter,
            "surviving_hp": hero.health if hero.is_alive else villain.health
        }

# Executable demonstration environment setup
if __name__ == "__main__":
    player = GameCharacter("Clay Carter", health=120, attack=18, defense=10, faction="The Resistance")
    boss = GameCharacter("Tevent (Skeleton King)", health=200, attack=14, defense=12, faction="Monsters")
    
    battle_log = CombatEngine.execute_turn_based_battle(player, boss)
    print("\n📊 SUBMISSION LOG FOR REPOSITORY STATE:")
    print(json.dumps(battle_log, indent=2))
