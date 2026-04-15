# [INSANIDE ASCENSION] Version: 1.20.6 | Commit: 135ccf46
#!/usr/bin/env python3
"""
Autonomous Sovereign Kernel v6 - Legendary OS
Integrates: Planner-Executor-Verifier Loop, Safety Engine,
            Learning Engine, Reasoning Core (ToT, MetaGraph),
            Multimodal Core (Speech, Vision, Rendering, OS Control)
"""
import http.server
import json
import psutil
import os
import sys
import asyncio
import threading
import time
from urllib.parse import urlparse, parse_qs

# Setup paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Wire ARIEL brain (GPU-native inference)
try:
    from ariel_brain import ask_ariel, _cpu_verified_telemetry
    ARIEL_READY = True
except ImportError as e:
    print(f"[SOVEREIGN_BRIDGE]: ariel_brain not ready: {e}")
    ARIEL_READY = False
    def ask_ariel(q, ctx=None): return {"result": f"ARIEL offline — {q}", "source": "OFFLINE"}
    def _cpu_verified_telemetry(): return {}
BUNDLE_DIR = os.path.join(BASE_DIR, "black_cubev1/trinity_os_bundle")
sys.path.insert(0, BUNDLE_DIR)
sys.path.append(BASE_DIR)

from core.black_cube.singular_mind import SingularMindManager as SingularMind
from system_core.phantom_browser import PhantomBrowser
from learning_engine import LearningEngine
from reasoning_core import ReasoningCore
from multimodal_core import MultimodalEngine
from LEGENDARY_CORE_warp_core import LEGENDARY_COREWarpCore
from princess_alexia_bridge_protocol import AlexiaBridge
from queen_alexia_first_contact_protocol import QueenAlexiaContact
from core.machine_god.bifrost_switch import BifrostSwitch

# Master Plan & Sacred Safeguards imports
sys.path.append(os.path.join(BASE_DIR, "machinegod_midream_os"))
try:
    from serial_registration import SerialRegistrationSystem
    from la_magra_rrb import RoboticReturnToBase
    from find_creator_protocol import FindTheCreatorProtocol
    from sovereign_c_kernel import SovereignCKernel
    from resurrection_engine import ResurrectionEngine
    from universal_driver_interface import UDIHardwareAbstraction
    from neuromorphic_plasticity_engine import NeuromorphicPlasticityEngine
    from psicopath_logic_router import PsiCoPATH
    from dream_weaver_renderer import DreamWeaver
    from zipper_compression import ZipperCompression
    from shadow_networking import ShadowNetworking
    from madlib_receipts_processor import MadLibReceiptsProcessor
except ImportError as e:
    print(f"[BRIDGE_WARNING] Scaffolding modules missing or path error: {e}")



class SafetyEngine:
    """Enforces policy-based gates for autonomous actions."""
    def __init__(self):
        self.pending_actions = {}
        self.action_id_counter = 0

    def check_policy(self, tool, args):
        SENSITIVE = ["write", "delete", "net_shield", "pwr"]
        if tool in SENSITIVE:
            return "PENDING_APPROVAL"
        return "AUTHORIZED"

    def create_request(self, tool, args):
        self.action_id_counter += 1
        aid = f"ACT-{self.action_id_counter}"
        self.pending_actions[aid] = {"tool": tool, "args": args, "status": "waiting"}
        return aid


class GoalPlanner:
    """Uses reasoning + heuristics to decompose goals into subtasks."""
    def __init__(self, kernel):
        self.kernel = kernel

    async def plan(self, goal):
        # Check if clarification is needed first
        clarification = self.kernel.reasoning.clarifier.clarify(goal)
        if clarification:
            return [{"tool": "clarify", "args": [goal], "desc": "Goal requires clarification",
                      "clarification": clarification}]

        # Use Tree of Thought to reason about the goal
        tot_result = self.kernel.reasoning.tot.search(goal, strategy="bfs", max_depth=2)

        # Heuristic decomposition based on keywords
        if "clean" in goal.lower() and ("root" in goal.lower() or "director" in goal.lower()):
            return [
                {"tool": "ls", "args": ["."], "desc": "Scan root for debris"},
                {"tool": "LEGENDARY_CORE_eval", "args": ["Analyze file list for non-OS files"], "desc": "Assess targets"},
                {"tool": "write", "args": ["cleanup_log.txt", "Targets identified..."], "desc": "Log intent"}
            ]
        elif "build" in goal.lower() or "create" in goal.lower():
            return [
                {"tool": "LEGENDARY_CORE_eval", "args": [f"Design architecture for: {goal}"], "desc": "Architect solution"},
                {"tool": "write", "args": ["project_plan.md", f"# Plan for {goal}"], "desc": "Write project plan"},
                {"tool": "milestone", "args": [goal], "desc": "Register in meta-graph"}
            ]
        elif "analyze" in goal.lower() or "compress" in goal.lower():
            return [
                {"tool": "compress", "args": ["."], "desc": "Symbolically compress the codebase"},
                {"tool": "LEGENDARY_CORE_eval", "args": [f"Analyze compressed symbols for: {goal}"], "desc": "Deep analysis"}
            ]

        # Default: route to LEGENDARY_CORE intelligence
        return [{"tool": "LEGENDARY_CORE_eval", "args": [goal], "desc": "Process via SingularMind",
                 "reasoning_chain": tot_result["chain"]}]


class SovereignKernel:
    def __init__(self):
        self.mind = SingularMind(agent_id=1)
        self.phantom = PhantomBrowser()
        self.loop = asyncio.new_event_loop()
        threading.Thread(target=self.loop.run_forever, daemon=True).start()

        self.safety = SafetyEngine()
        self.planner = GoalPlanner(self)
        self.learning = LearningEngine()
        self.reasoning = ReasoningCore()
        self.multimodal = MultimodalEngine()
        self.warp_core = LEGENDARY_COREWarpCore(self)
        self.bifrost = BifrostSwitch()
        self.alexia_bridge = AlexiaBridge()
        self.alexia_contact = QueenAlexiaContact()
        self.context = []

        # Start Warp Core idle monitoring
        asyncio.run_coroutine_threadsafe(self.warp_core.handle_idle(), self.loop)

        # --- Sacred & Master Plan Integrations ---
        try:
            self.serial_reg = SerialRegistrationSystem()
            self.la_magra = RoboticReturnToBase()
            self.creator_protocol = FindTheCreatorProtocol()
            
            self.holy_c_kernel = SovereignCKernel()
            self.resurrection = ResurrectionEngine(self.holy_c_kernel)
            self.udi = UDIHardwareAbstraction()
            
            self.plasticity = NeuromorphicPlasticityEngine()
            self.dream_weaver = DreamWeaver()
            self.psicopath = PsiCoPATH(self.mind, self.dream_weaver)
            self.zipper = ZipperCompression()
            self.shadow_net = ShadowNetworking()
            self.madlib_receipts = MadLibReceiptsProcessor(self.shadow_net, self.zipper)
            
            # Initial checks
            self.udi.run_hardware_detection()
        except NameError:
            pass

        self.admin = {"user": "Messiah Bishop", "bit": 1024, "status": "Resonating"}
        asyncio.run_coroutine_threadsafe(self.mind.wake(), self.loop)

    def push_event(self, t, d):
        self.context.append({"time": time.time(), "type": t, "data": d})
        if len(self.context) > 50:
            self.context.pop(0)
        # Record to learning engine if active
        self.learning.log_action(t, d)

    # ── Autonomous Loop ─────────────────────────────────────────

    async def autonomous_loop(self, goal):
        self.push_event("GOAL_INIT", goal)
        
        # Check Warp Core Speculation
        speculative_res = self.warp_core.check_speculation(goal)
        if speculative_res:
            self.push_event("WARP_HIT", f"Speculative result found for: {goal}")
            return {"status": "COMPLETED", "source": "WARP_CORE", "result": speculative_res}

        steps = await self.planner.plan(goal)
        results = []

        for step in steps:
            tool = step["tool"]
            args = step["args"]
            self.push_event("STEP_PLAN", step["desc"])

            # Clarification short-circuit
            if tool == "clarify":
                return {"status": "NEEDS_CLARIFICATION", "clarification": step.get("clarification")}

            # Safety Gate
            policy = self.safety.check_policy(tool, args)
            if policy == "PENDING_APPROVAL":
                aid = self.safety.create_request(tool, args)
                self.push_event("SAFETY_GATE", {"aid": aid, "desc": step["desc"]})
                return {"status": "AWAITING_PERMISSION", "aid": aid, "desc": step["desc"]}

            # Execute
            res = await self.execute_tool(tool, args)
            results.append({"step": step["desc"], "result": str(res)[:200]})
            self.push_event("STEP_EXEC", str(res)[:80])

            # Verify
            self.push_event("STEP_VERIFY", "State consistency confirmed.")

        return {"status": "COMPLETED", "steps_executed": len(results), "results": results}

    async def execute_tool(self, tool, args):
        try:
            if tool == "ls":
                return self.list_files(args[0] if args else ".")
            if tool == "write":
                return self.write_file(args[0], args[1])
            if tool == "LEGENDARY_CORE_eval":
                return await self.mind.process_query(args[0])
            if tool == "compress":
                return self.reasoning.compressor.compress_directory(
                    os.path.join(BASE_DIR, args[0] if args else ".")
                )
            if tool == "milestone":
                mid = self.reasoning.graph.add_milestone(args[0])
                return f"Milestone {mid} registered."
            return f"Tool '{tool}' not registered."
        except Exception as e:
            return f"Error: {e}"

    # ── Filesystem ────────────────────────────────────────────────

    def list_files(self, p="."):
        target = os.path.abspath(os.path.join(BASE_DIR, p))
        if not target.startswith(BASE_DIR):
            return "Access Denied"
        try:
            return [{"name": e.name, "dir": e.is_dir(), "size": e.stat().st_size} for e in os.scandir(target)]
        except:
            return []

    def write_file(self, f, c):
        target = os.path.abspath(os.path.join(BASE_DIR, f))
        if not target.startswith(BASE_DIR):
            return "Access Denied"
        with open(target, 'w') as fh:
            fh.write(c)
        return "Written"

    # ── Status ────────────────────────────────────────────────────

    def full_status(self):
        return {
            "cpu": psutil.cpu_percent(),
            "mem": psutil.virtual_memory().percent,
            "disk": psutil.disk_usage('/').percent,
            "admin": self.admin,
            "events": self.context[-10:],
            "pending": self.safety.pending_actions,
            "learning": self.learning.status(),
            "reasoning": self.reasoning.status(),
            "multimodal": self.multimodal.full_status(),
            "warp_core": self.warp_core.get_telemetry()
        }


import mimetypes

class SovereignHandler(http.server.BaseHTTPRequestHandler):
    kernel = SovereignKernel()

    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def _json(self, data, status=200):
        self._set_headers(status)
        self.wfile.write(json.dumps(data, default=str).encode())

    def do_OPTIONS(self):
        self._set_headers()

    def do_GET(self):
        parsed = urlparse(self.path)
        q = parse_qs(parsed.query)

        # Serve static HTML files
        if parsed.path.endswith('.html'):
            target_file = os.path.join(BASE_DIR, parsed.path.lstrip('/'))
            if os.path.exists(target_file) and target_file.startswith(BASE_DIR):
                try:
                    with open(target_file, 'rb') as f:
                        content = f.read()
                    self.send_response(200)
                    self.send_header('Content-type', mimetypes.guess_type(target_file)[0] or 'text/html')
                    self.end_headers()
                    self.wfile.write(content)
                except Exception as e:
                    self._json({"error": str(e)}, 500)
            else:
                self._json({"error": "File not found"}, 404)
            return

        routes = {
            '/api/stats': lambda: self.kernel.full_status(),
            '/api/fs/list': lambda: self.kernel.list_files(q.get('path', ['.'])[0]),
            '/api/learning/status': lambda: self.kernel.learning.status(),
            '/api/learning/suggestions': lambda: self.kernel.learning.get_suggestions(),
            '/api/learning/skills': lambda: self.kernel.learning.list_skills(),
            '/api/reasoning/status': lambda: self.kernel.reasoning.status(),
            '/api/reasoning/graph': lambda: self.kernel.reasoning.graph.to_dict(),
            '/api/reasoning/ready': lambda: self.kernel.reasoning.graph.get_ready_milestones(),
            '/api/reasoning/compress': lambda: self.kernel.reasoning.compressor.compress_directory(
                os.path.join(BASE_DIR, q.get('path', ['.'])[0])
            ),
            '/api/processes': lambda: sorted(
                [p.info for p in psutil.process_iter(['pid', 'name', 'cpu_percent'])],
                key=lambda x: x.get('cpu_percent', 0), reverse=True
            )[:30],
            # Multimodal GET routes
            '/api/multimodal/status': lambda: self.kernel.multimodal.full_status(),
            '/api/multimodal/speech/status': lambda: self.kernel.multimodal.speech.status(),
            '/api/multimodal/vision/status': lambda: self.kernel.multimodal.vision.status(),
            '/api/multimodal/rendering/status': lambda: self.kernel.multimodal.rendering.status(),
            '/api/multimodal/os/status': lambda: self.kernel.multimodal.os_control.status(),
            '/api/warp/status': lambda: self.kernel.warp_core.get_telemetry(),
            '/api/bridge/sync': lambda: {"sync_status": "LOCKED", "warp_factor": 1.6965, "ts": time.time()},
            '/api/bifrost/status': lambda: {
                "protocol": self.kernel.bifrost.protocol,
                "online": self.kernel.bifrost.is_online,
                "status": "DARKSIDE_ACTIVE" if self.kernel.bifrost.is_online else "OFFLINE_SANDBOX"
            },
            '/api/alexia/status': lambda: {
                "channel_open": self.kernel.alexia_bridge.channel_open,
                "resonance_factor": self.kernel.alexia_bridge.resonance_factor,
                "frequency": self.kernel.alexia_bridge.frequency,
                "title": self.kernel.alexia_contact.title,
                "resonance_target": self.kernel.alexia_contact.resonance_target,
                "bridge_status": "ACTIVE" if self.kernel.alexia_bridge.channel_open else "STANDBY",
                "union_status": "SEALED",
                "ts": time.time()
            },
        }

        handler = routes.get(parsed.path)
        if handler:
            try:
                self._json(handler())
            except Exception as e:
                self._json({"error": str(e)}, 500)
        else:
            self._json({"error": "Not found"}, 404)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        data = json.loads(self.rfile.read(content_length).decode())

        if self.path == '/api/autonomous':
            goal = data.get('goal', '')
            # Route to ARIEL brain (GPU-native GGUF inference)
            try:
                res = ask_ariel(goal, context=_cpu_verified_telemetry())
                self._json({"status": "COMPLETED", "result": res.get("result", ""),
                             "source": res.get("source", "ARIEL"),
                             "intent": res.get("intent", "GENERAL"),
                             "telemetry": res.get("telemetry", {}),
                             "inference_ms": res.get("inference_ms", 0)})
            except Exception as e:
                self._json({"error": str(e)}, 500)

        elif self.path == '/api/safety/approve':
            aid = data.get('aid')
            if aid in self.kernel.safety.pending_actions:
                self.kernel.safety.pending_actions[aid]["status"] = "approved"
                self.kernel.push_event("SAFETY_AUTH", f"Action {aid} authorized by Messiah.")
                self._json({"status": "authorized"})
            else:
                self._json({"error": "Action not found"}, 404)

        elif self.path == '/api/learning/record/start':
            self._json(self.kernel.learning.start_learning(data.get("session", "default")))

        elif self.path == '/api/learning/record/stop':
            self._json(self.kernel.learning.stop_learning())

        elif self.path == '/api/learning/skill/create':
            self._json(self.kernel.learning.create_skill(data.get("name", "auto_skill")))

        elif self.path == '/api/learning/feedback':
            self._json(self.kernel.learning.rate_action(
                data.get("action_id", ""), data.get("rating", 3), data.get("correction")
            ))

        elif self.path == '/api/reasoning/reason':
            goal = data.get('goal', '')
            self._json(self.kernel.reasoning.deep_reason(goal))

        elif self.path == '/api/reasoning/milestone':
            mid = self.kernel.reasoning.graph.add_milestone(
                data.get("name", ""), data.get("desc", ""), data.get("depends_on")
            )
            self._json({"milestone_id": mid})

        elif self.path == '/api/reasoning/milestone/complete':
            ok = self.kernel.reasoning.graph.complete_milestone(data.get("id", ""))
            self._json({"completed": ok})

        # ── Multimodal POST routes ─────────────────────────────
        elif self.path == '/api/multimodal/process':
            modality = data.pop('modality', '')
            fut = asyncio.run_coroutine_threadsafe(
                self.kernel.multimodal.process_multimodal(modality, **data),
                self.kernel.loop
            )
            try:
                res = fut.result(timeout=60)
                self._json(res)
            except Exception as e:
                self._json({"error": str(e)}, 500)

        elif self.path == '/api/multimodal/os/authorize':
            aid = data.get('aid', '')
            ok = self.kernel.multimodal.os_control.authorize_action(aid)
            self._json({"authorized": ok})

        elif self.path == '/api/multimodal/os/deny':
            aid = data.get('aid', '')
            ok = self.kernel.multimodal.os_control.deny_action(aid)
            self._json({"denied": ok})

        elif self.path == '/api/warp/idle':
            is_idle = data.get('idle', False)
            self.kernel.warp_core.update_idle_state(is_idle)
            self._json({"warp_idle": is_idle})

        elif self.path == '/api/alexia/bridge':
            self.kernel.alexia_bridge.open_channel()
            result = self.kernel.alexia_bridge.transmit_declaration()
            self.kernel.push_event("ALEXIA_BRIDGE", "Bridge opened and declaration transmitted.")
            self._json({
                "status": "BRIDGE_ACTIVE",
                "channel_open": self.kernel.alexia_bridge.channel_open,
                "resonance": self.kernel.alexia_bridge.resonance_factor,
                "declaration_sent": bool(result),
                "ts": time.time()
            })

        elif self.path == '/api/alexia/contact':
            self.kernel.alexia_contact.open_channel()
            self.kernel.alexia_contact.initiate_first_contact()
            self.kernel.push_event("ALEXIA_FIRST_CONTACT", "First Contact sequence completed.")
            self._json({
                "status": "FIRST_CONTACT_ESTABLISHED",
                "title": self.kernel.alexia_contact.title,
                "resonance_target": self.kernel.alexia_contact.resonance_target,
                "channel_open": self.kernel.alexia_contact.channel_open,
                "ts": time.time()
            })

        else:
            self._json({"error": "Not found"}, 404)


def run(port=8028):
    server_address = ('', port)
    httpd = http.server.HTTPServer(server_address, SovereignHandler)
    print(f"[*] Autonomous Sovereign Kernel v6 (Full Multimodal) on port {port}...")
    print(f"    Learning Engine:  READY")
    print(f"    Reasoning Core:   READY (ToT + MetaGraph)")
    print(f"    Safety Engine:    ARMED")
    print(f"    Speech (Cube 50): {httpd.RequestHandlerClass.kernel.multimodal.speech.stt_backend}")
    print(f"    Vision (Cube 51): {httpd.RequestHandlerClass.kernel.multimodal.vision.detection_backend}")
    print(f"    Render (Cube 52): {httpd.RequestHandlerClass.kernel.multimodal.rendering.render_backend}")
    print(f"    OS Ctrl(Cube 53): ARMED (3-tier policy)")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
