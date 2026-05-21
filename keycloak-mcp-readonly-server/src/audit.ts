export type AuditEvent = {
  tool: string;
  realm?: string;
  status: "start" | "success" | "error";
  message?: string;
};

export function audit(event: AuditEvent): void {
  const payload = {
    time: new Date().toISOString(),
    ...event,
  };

  // MCP stdio transport uses stdout for protocol messages.
  // Write operational logs to stderr only.
  console.error(JSON.stringify(payload));
}
