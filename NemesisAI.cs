using System;

namespace Umbrella.REEngine.Scripting
{
    public class NemesisAI : SystemObject
    {
        public string ActiveTarget { get; set; }
        public int ThreatAggressionLevel { get; set; }
        private bool isTargetInProximity;

        public NemesisAI(string targetName)
        {
            ActiveTarget = targetName;
            ThreatAggressionLevel = 1; // Default roaming alert state
            isTargetInProximity = false;
        }

        // Simulates the pathfinding coordinate range loop evaluation
        public void UpdateProximityCoordinates(int distanceToTarget)
        {
            if (distanceToTarget <= 5)
            {
                isTargetInProximity = true;
                ThreatAggressionLevel = 3; // Maximum tracking priority
                TriggerScreamAudioAlert();
            }
            else
            {
                isTargetInProximity = false;
                ThreatAggressionLevel = 1;
            }
        }

        private void TriggerScreamAudioAlert()
        {
            Console.WriteLine($"\n👹 [RE_ENGINE_AUDIO]: Nemesis tracks target '{ActiveTarget}'!");
            Console.WriteLine("🗣️ Voice Box Matrix Dispatch: 'S.T.A.R.S...'");
        }

        public void ExecuteTacticalAction()
        {
            if (isTargetInProximity)
            {
                Console.WriteLine("💥 ACTION EXECUTION: Nemesis launches a heavy tentacle strike strike!");
            }
            else
            {
                Console.WriteLine("🏃 ROAMING LOGIC: Nemesis searches the corridor grid structures.");
            }
        }
    }

    class ExecutionHook
    {
        static void Main(string[] args)
        {
            NemesisAI activeScript = new NemesisAI("Jill Valentine");
            activeScript.UpdateProximityCoordinates(12); // Safe roaming
            activeScript.ExecuteTacticalAction();

            activeScript.UpdateProximityCoordinates(3);  // Enters lethal proximity range
            activeScript.ExecuteTacticalAction();
        }
    }
}
