import { chromium } from '/mnt/storage/xibalba/Projects/worktrees/xibalba-cortex/knowledge-graph-connectors/viewer/node_modules/@playwright/test/index.mjs'
import { resolve } from 'node:path'

async function validate() {
  console.log('Launching Chromium for xibalba-solutions-site...')
  const browser = await chromium.launch({
    executablePath: '/usr/bin/google-chrome',
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage', '--headless=new'],
  })

  const context = await browser.newContext({
    viewport: { width: 1440, height: 900 },
  })

  const siteDir = '/mnt/storage/xibalba/Projects/xibalba-solutions-site'
  const artifactDir = '/home/xibalba/.gemini/antigravity-cli/brain/915d42e0-a7ed-43f0-a667-f2078843f480'

  const pages = [
    { file: 'index.html', out: 'screen_solutions_site_navigational_ai.png', fullPage: false },
    { file: 'about.html', out: 'screen_solutions_site_about.png', fullPage: false },
    { file: 'integrity-protocol.html', out: 'screen_solutions_site_integrity_protocol.png', fullPage: false },
  ]

  for (const p of pages) {
    const page = await context.newPage()
    const filePath = 'file://' + resolve(siteDir, p.file)
    console.log(`Navigating to ${filePath}...`)
    await page.goto(filePath, { waitUntil: 'load' })
    await page.waitForTimeout(1000)

    const outPath = resolve(artifactDir, p.out)
    await page.screenshot({ path: outPath, fullPage: p.fullPage })
    console.log(`Saved screenshot to ${outPath}`)
    await page.close()
  }

  await browser.close()
  console.log('Render validation complete!')
}

validate().catch(err => {
  console.error(err)
  process.exit(1)
})
