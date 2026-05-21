import { z } from "zod";
import type { KeycloakClientApi } from "../keycloak-client.js";
import { isRiskyRedirectUri } from "../guardrails.js";

export const CheckRedirectUrisArgs = z.object({
  realm: z.string().optional(),
});

export async function checkRedirectUris(api: KeycloakClientApi, args: z.infer<typeof CheckRedirectUrisArgs>) {
  const clients = await api.listClients(args.realm);
  return clients
    .flatMap((client) =>
      (client.redirectUris ?? []).map((uri) => ({
        clientId: client.clientId,
        redirectUri: uri,
        risky: isRiskyRedirectUri(uri),
      })),
    )
    .filter((item) => item.risky);
}
