# Analysis Tools Installation and Verification Report

**Project**: TickTick Functional Research  
**Document**: `research/02_ANALYSIS_TOOLS.md`  
**Date**: November 13, 2026  
**Status**: VERIFIED & OPERATIONAL  

---

## 1. Executive Summary

To enable rigorous, evidence-backed static reverse engineering of the TickTick Android application without executing untrusted code or guessing behavior, a comprehensive suite of static reverse engineering tools has been installed, configured, verified, and integrated into the research environment.

The suite combines:
1. **REA (Reverse Engineer Anything)**: CLI v6.7.0 / Agents v6.9.0 with Model Context Protocol (MCP) server integration for AI coding agents.
2. **Headless JADX MCP Engine**: v0.7.1 fat JAR with cryptographically verified SHA-256 hash.
3. **Azul Zulu OpenJDK 17**: v17.0.14 (Full JDK including `javac` and `jdk.compiler` module required for source bridge compilation).
4. **Standalone JADX Decompiler**: v1.5.1 CLI / Core.
5. **Apktool**: v3.0.3 resource and manifest decoder.
6. **Python Bytecode & Manifest Inspection Stack**: `androguard` v4.1.4, `pyaxmlparser` v0.3.31, `lxml` v6.1.3.

---

## 2. REA (Reverse Engineer Anything) Integration

### 2.1 Tool Overview
- **Repository**: [https://github.com/morluto/rea](https://github.com/morluto/rea)
- **Official Package**: `rea-agents` (npm registry)
- **Installed CLI Version**: `6.7.0` (Binary launcher: `rea`, `rea-agents`)
- **Package Distribution**: `rea-agents@6.9.0`
- **Installation Scope**: Global Node.js environment (`C:\Users\Mahim\AppData\Roaming\npm\node_modules\rea-agents`)
- **Runtime Environment**: Node.js `v24.14.1`, npm `11.11.0`

### 2.2 Model Context Protocol (MCP) Server Configuration
REA was configured for Antigravity via `rea setup --client antigravity -y`.
- **MCP Configuration File**: `C:\Users\Mahim\.gemini\config\mcp_config.json`
- **MCP Registration Entry**:
```json
{
  "mcpServers": {
    "rea": {
      "command": "C:\\Program Files\\nodejs\\node.exe",
      "args": [
        "C:\\Users\\Mahim\\AppData\\Roaming\\npm\\node_modules\\rea-agents\\scripts\\rea.mjs",
        "mcp"
      ],
      "env": {
        "JAVA_HOME": "D:\\tick tick open source\\TICKTICK_FUNCTIONAL_RESEARCH\\tools\\zulu17_jdk",
        "REA_JADX_MCP_JAR": "D:\\tick tick open source\\TICKTICK_FUNCTIONAL_RESEARCH\\tools\\jadx-headless-mcp-0.7.1-all.jar"
      }
    }
  }
}
```
- **Agent Skill Installed**: `C:\Users\Mahim\.gemini\config\skills\reverse-engineer-anything` (Skill Version 42, 207 MCP tools exposed).

### 2.3 Diagnostic Verification (`rea doctor`)
Verification was executed via `rea doctor --provider jadx`:
```
healthy: true
jadx:
  configured: true
  available: true
  detail: "JADX MCP bridge JAR validated at D:\\tick tick open source\\TICKTICK_FUNCTIONAL_RESEARCH\\tools\\jadx-headless-mcp-0.7.1-all.jar"
```

---

## 3. Headless JADX MCP Engine

### 3.1 Source & Version
- **Upstream Repository**: [https://github.com/1013503897/jadx-headless-mcp](https://github.com/1013503897/jadx-headless-mcp)
- **Release Version**: `v0.7.1`
- **Artifact**: `jadx-headless-mcp-0.7.1-all.jar` (Size: 42,619,858 bytes)
- **Local Path**: `TICKTICK_FUNCTIONAL_RESEARCH/tools/jadx-headless-mcp-0.7.1-all.jar`

### 3.2 Cryptographic Hash Verification
The SHA-256 hash was verified against the official upstream release checksum file:
- **Expected SHA-256**: `6e5eacf500b64292bfb73c49797c1958f6ee44646e43e868039ae7feb573ff75`
- **Calculated SHA-256**: `6e5eacf500b64292bfb73c49797c1958f6ee44646e43e868039ae7feb573ff75`
- **Status**: [VERIFIED] Checksum match confirmed.

---

## 4. Java Development Kit (JDK 17)

### 4.1 Specification
- **Vendor**: Azul Systems (Zulu OpenJDK)
- **Release**: `zulu17.56.15-ca-jdk17.0.14-win_x64`
- **Java Version**: `17.0.14` (build 17.0.14+7-LTS)
- **Local Directory**: `TICKTICK_FUNCTIONAL_RESEARCH/tools/zulu17_jdk`
- **Compiler Module**: `jdk.compiler@17.0.14` confirmed present.

---

## 5. Standalone JADX Decompiler

### 5.1 Specification
- **Repository**: [https://github.com/skylot/jadx](https://github.com/skylot/jadx)
- **Release**: `v1.5.1`
- **Artifact**: `jadx-1.5.1-all.jar` (Size: 126,980,139 bytes)
- **Local Path**: `TICKTICK_FUNCTIONAL_RESEARCH/tools/jadx`
- **Execution Test**: `jadx --version` -> `1.5.1` [VERIFIED].

---

## 6. Apktool Resource Decoder

### 6.1 Specification
- **Repository**: [https://github.com/iBotPeaches/Apktool](https://github.com/iBotPeaches/Apktool)
- **Release**: `v3.0.3`
- **Artifact**: `apktool_3.0.3.jar` (Size: 15,478,013 bytes)
- **Local Path**: `TICKTICK_FUNCTIONAL_RESEARCH/tools/apktool.jar`
- **Execution Test**: `java -jar apktool.jar --version` -> `3.0.3` [VERIFIED].
- **Decoded Output**: Successfully decoded base APK resources to `staging_apk/apktool_out/` (decoded manifest, 4,322 string entries, layouts, and menus).

---

## 7. Python Static Inspection Stack

### 7.1 Installed Libraries
- `androguard` (4.1.4): DEX disassembly, call graph analysis, xref tracing.
- `pyaxmlparser` (0.3.31): Android binary XML and manifest parsing.
- `lxml` (6.1.3): Fast XML element tree processing and pretty printing.
- `sqlalchemy` (2.1.8) & `alembic` (1.20.1): Schema modeling dependencies.

---

## 8. REA Functional Capabilities & Verification Test

### 8.1 Verification Test on Uploaded TickTick APK
A live search query was executed against `staging_apk/com.ticktick.task.apk`:
- **Evidence ID**: `ev_a885a345c8e145a1b18b1b42fbb97e27f1ee6f2b4c6c7db5c8a37c411e615862`
- **Target SHA-256**: `f4c4f43b63d0849a4c53e6ed8a2414245805df86f8335d6b76cdf02756b19a6f`
- **Bridge Version**: `rea-jadx-bridge` v4
- **DEX Classes Indexed**: 18,071 classes loaded
- **Resource Count**: 4,196 resources indexed
- **Result Status**: LOADED & FULLY FUNCTIONAL

---

## 9. Tool Usage Guidelines in this Project

1. **High-Level Structural Exploration**: Use `apktool` for resources, strings, layouts, preferences, and manifests.
2. **Class & Member Inspection**: Use REA (`rea search-android-classes`, `rea inspect-android-classes`).
3. **Decompilation & Logic Verification**: Use REA (`rea inspect-android-methods`) and JADX (`jadx-1.5.1-all.jar`).
4. **Reference Tracing**: Use REA (`rea trace-android-references`).
5. **Cross-Validation**: Verify any ambiguous code paths against raw DEX bytecode via `androguard`.
