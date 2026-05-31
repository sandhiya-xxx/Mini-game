import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;

public class ThroneLoreEngine {
    
    // Core Data Structure Mappings for highly visual indexing lookups
    private HashMap<String, String> loreFactSheet;
    private Queue<String> dynamicMatchmakingQueue;
    private LinkedList<String> historicalCommandHistory;

    public ThroneLoreEngine() {
        this.loreFactSheet = new HashMap<>();
        this.dynamicMatchmakingQueue = new LinkedList<>();
        this.historicalCommandHistory = new LinkedList<>();
        initializeDataArrays();
    }

    private void initializeDataArrays() {
        // Fast indexing mapping via hashing structures
        loreFactSheet.put("LASLAN", "Kastleton is protected by the Pledge of Resistance.");
        loreFactSheet.put("STONEGARD", "The desert conceals ancient Star Fragment elements.");
        loreFactSheet.put("TEVENT", "Resurrected Skeleton King bound to environmental sandstorms.");
    }

    // Pipeline Logic: FIFO Data Tracking Structure for Player Entry Matches
    public void enqueuePlayerToDungeon(String gamerTag) {
        dynamicMatchmakingQueue.add(gamerTag);
        logSystemAction("QUEUE", "Player " + gamerTag + " entered the lobby dungeon queue.");
    }

    public String popNextMatchmakingGroup() {
        if (!dynamicMatchmakingQueue.isEmpty()) {
            String primaryPlayer = dynamicMatchmakingQueue.poll();
            logSystemAction("MATCH", "Instance spun up for operational team lead: " + primaryPlayer);
            return primaryPlayer;
        }
        return "Lobby Empty";
    }

    // Pipeline Logic: LIFO Data Management for Tracking State Logs
    private void logSystemAction(String classification, String executionLog) {
        historicalCommandHistory.addFirst("[" + classification + "] " + executionLog);
        if (historicalCommandHistory.size() > 50) {
            historicalCommandHistory.removeLast(); // Keep memory clear
        }
    }

    public void displayDiagnosticMetrics() {
        System.out.println("=== SYSTEM GRAPH MEMORY DIAGNOSTICS ===");
        System.out.println("Cached Lore Nodes: " + loreFactSheet.size());
        System.out.println("Active Queue Depth: " + dynamicMatchmakingQueue.size());
        System.out.println("Latest Audit Entry: " + historicalCommandHistory.peekFirst());
    }

    public static void main(String[] args) {
        ThroneLoreEngine coreEngine = new ThroneLoreEngine();
        coreEngine.enqueuePlayerToDungeon("Vanguard_Clay");
        coreEngine.enqueuePlayerToDungeon("Shadow_Evelyn");
        coreEngine.displayDiagnosticMetrics();
        coreEngine.popNextMatchmakingGroup();
    }
}
