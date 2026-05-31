import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;

public class ResidentEvilEngine {
    
    private HashMap<String, String> bioweaponRegistry;
    private Queue<String> evacuationHelipadQueue;
    private LinkedList<String> systemSecurityAuditLogs;

    public ResidentEvilEngine() {
        this.bioweaponRegistry = new HashMap<>();
        this.evacuationHelipadQueue = new LinkedList<>();
        this.systemSecurityAuditLogs = new LinkedList<>();
        initializeDataArrays();
    }

    private void initializeDataArrays() {
        bioweaponRegistry.put("T_VIRUS", "Tyrant development asset. Causes rapid cellular mutation.");
        bioweaponRegistry.put("NEMESIS", "T-Type organism tracking elite field targets.");
        bioweaponRegistry.put("G_VIRUS", "Golgotha strain. Cellular regeneration asset variant.");
    }

    public void queueSurvivorForEvac(String survivorName) {
        evacuationHelipadQueue.add(survivorName);
        logSystemAction("EVAC", "Subject " + survivorName + " checked into landing bay perimeter.");
    }

    public String liftoffNextChopper() {
        if (!evacuationHelipadQueue.isEmpty()) {
            String extracted = evacuationHelipadQueue.poll();
            logSystemAction("STATUS", "Chopper departed. Extracted unit: " + extracted);
            return extracted;
        }
        return "No targets in loading sector";
    }

    private void logSystemAction(String classification, String executionLog) {
        systemSecurityAuditLogs.addFirst("[" + classification + "] " + executionLog);
        if (systemSecurityAuditLogs.size() > 50) {
            systemSecurityAuditLogs.removeLast();
        }
    }

    public void displayDiagnosticMetrics() {
        System.out.println("=== NESTOR ARCHIVE PIPELINE DIAGNOSTICS ===");
        System.out.println("Tracked Malware Signatures: " + bioweaponRegistry.size());
        System.out.println("Helipad Queue Depth: " + evacuationHelipadQueue.size());
        System.out.println("Latest Sector Feed: " + systemSecurityAuditLogs.peekFirst());
    }

    public static void main(String[] args) {
        ResidentEvilEngine securityCore = new ResidentEvilEngine();
        securityCore.queueSurvivorForEvac("Leon_S_Kennedy");
        securityCore.queueSurvivorForEvac("Jill_Valentine");
        securityCore.displayDiagnosticMetrics();
        securityCore.liftoffNextChopper();
    }
}
