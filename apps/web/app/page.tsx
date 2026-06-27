import type { components } from "@/lib/api-types";

type HealthResponse = components["schemas"]["HealthResponse"];

export default async function Home() {
  let data: HealthResponse | null = null;
  let error: string | null = null;

  // Use API_BASE_URL when set (Docker: http://api:8000); fall back to localhost for native dev.
  const apiBase = process.env.API_BASE_URL ?? "http://localhost:8000";

  try {
    const res = await fetch(`${apiBase}/health`, {
      cache: "no-store",
    });
    data = await res.json();
  } catch {
    error = "Could not reach the API. Is the backend running on :8000?";
  }

  return (
    <main style={{ fontFamily: "sans-serif", padding: "3rem" }}>
      <h1>DraftPilot</h1>
      <h2>Backend health check</h2>
      {error ? (
        <p style={{ color: "crimson" }}>{error}</p>
      ) : (
        <pre
          style={{
            background: "#f4f4f4",
            padding: "1rem",
            borderRadius: "8px",
          }}
        >
          {JSON.stringify(data, null, 2)}
        </pre>
      )}
    </main>
  );
}
