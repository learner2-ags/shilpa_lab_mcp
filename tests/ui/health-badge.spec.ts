import { test, expect } from '@playwright/test';

test('health badge shows OK for the 72 C reading', async ({ page }) => {
  await page.goto('/');
  await expect(page.locator('#reading')).toHaveText('72');
  await expect(page.locator('#health')).toHaveText('OK');
  await expect(page.locator('#health')).toHaveClass(/\bok\b/);
});
