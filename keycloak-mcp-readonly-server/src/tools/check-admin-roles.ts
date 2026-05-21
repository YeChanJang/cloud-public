import { z } from "zod";
import type { KeycloakClientApi } from "../keycloak-client.js";

export const CheckAdminRolesArgs = z.object({
  realm: z.string().optional(),
});

const adminRolePatterns = [/admin/i, /manage-/i, /realm-management/i];

export async function checkAdminRoles(api: KeycloakClientApi, args: z.infer<typeof CheckAdminRolesArgs>) {
  const roles = await api.listRealmRoles(args.realm);
  return roles
    .filter((role) => adminRolePatterns.some((pattern) => pattern.test(role.name)))
    .map((role) => ({
      name: role.name,
      description: role.description,
      note: "Review this role and its assignments in Keycloak before granting to users or groups.",
    }));
}
