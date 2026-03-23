import { defineMiddleware } from 'astro:middleware';

/**
 * Domain-based routing middleware.
 *
 * When a country-specific domain (e.g. alc.md) hits the root "/",
 * rewrite to serve that branch's page while keeping the URL unchanged.
 */

const DOMAIN_TO_BRANCH: Record<string, string> = {
  'alc.md': '/branches/moldova',
  'alc.ge': '/branches/georgia',
};

export const onRequest = defineMiddleware(async ({ request, rewrite }, next) => {
  const host = request.headers.get('host')?.replace(/:\d+$/, '') ?? '';
  const url = new URL(request.url);

  // Only rewrite root path for mapped domains
  if (url.pathname === '/' && DOMAIN_TO_BRANCH[host]) {
    return rewrite(DOMAIN_TO_BRANCH[host]);
  }

  return next();
});
