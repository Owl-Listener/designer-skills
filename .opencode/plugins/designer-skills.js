/**
 * Designer Skills plugin for OpenCode.ai
 *
 * Registers all design skill directories so OpenCode discovers them
 * without symlinks or manual config. Injects pipeline awareness via
 * system prompt transform.
 */

import path from 'path';
import fs from 'fs';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.resolve(__dirname, '../..');

// Simple frontmatter extraction (no external deps needed for bootstrap)
const extractAndStripFrontmatter = (content) => {
  const match = content.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/);
  if (!match) return { frontmatter: {}, content };

  const frontmatterStr = match[1];
  const body = match[2];
  const frontmatter = {};

  for (const line of frontmatterStr.split('\n')) {
    const colonIdx = line.indexOf(':');
    if (colonIdx > 0) {
      const key = line.slice(0, colonIdx).trim();
      const value = line.slice(colonIdx + 1).trim().replace(/^["']|["']$/g, '');
      frontmatter[key] = value;
    }
  }

  return { frontmatter, content: body };
};

// All skill directories in the repo
const SKILL_DIRS = [
  'design-research/skills',
  'design-systems/skills',
  'ux-strategy/skills',
  'ui-design/skills',
  'interaction-design/skills',
  'prototyping-testing/skills',
  'design-ops/skills',
  'designer-toolkit/skills',
  'workflow/skills',
];

export const DesignerSkillsPlugin = async ({ client, directory }) => {

  const getBootstrapContent = () => {
    const skillPath = path.join(repoRoot, 'workflow', 'skills', 'using-designer-skills', 'SKILL.md');
    if (!fs.existsSync(skillPath)) return null;

    const fullContent = fs.readFileSync(skillPath, 'utf8');
    const { content } = extractAndStripFrontmatter(fullContent);

    return `<DESIGNER_SKILLS>
You have designer skills — a comprehensive collection of 63 design skills for product designers.

**IMPORTANT: The using-designer-skills skill content is included below. It is ALREADY LOADED — do NOT use the skill tool to load "using-designer-skills" again.**

${content}
</DESIGNER_SKILLS>`;
  };

  return {
    // Register all skill directories so OpenCode discovers them automatically
    config: async (config) => {
      config.skills = config.skills || {};
      config.skills.paths = config.skills.paths || [];

      for (const dir of SKILL_DIRS) {
        const fullPath = path.resolve(repoRoot, dir);
        if (fs.existsSync(fullPath) && !config.skills.paths.includes(fullPath)) {
          config.skills.paths.push(fullPath);
        }
      }
    },

    // Inject pipeline awareness into every session
    'experimental.chat.system.transform': async (_input, output) => {
      const bootstrap = getBootstrapContent();
      if (bootstrap) {
        (output.system ||= []).push(bootstrap);
      }
    }
  };
};
