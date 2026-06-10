#!/usr/bin/env bash
# ============================================================
# 我收藏/创作的 Skill — 一键安装脚本
# 用法: bash install.sh
# 效果: 将所有 skill 安装到 ~/.claude/skills/
# ============================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILLS_DIR="$HOME/.claude/skills"

mkdir -p "$SKILLS_DIR"

installed=0
skipped=0

# 安装目录型 skill（符号链接方式，方便 git pull 更新）
echo "📦 安装目录型 Skill..."
for skill_dir in "$SCRIPT_DIR/skills"/*/; do
  name="$(basename "$skill_dir")"
  target="$SKILLS_DIR/$name"

  if [ -e "$target" ]; then
    echo "  ⏭  $name (已存在，跳过)"
    skipped=$((skipped + 1))
    continue
  fi

  ln -s "$skill_dir" "$target"
  echo "  ✅ $name"
  installed=$((installed + 1))
done

# 安装单文件 skill（直接复制）
echo ""
echo "📄 安装单文件 Skill..."
for skill_file in "$SCRIPT_DIR/standalone"/*.md; do
  [ -f "$skill_file" ] || continue
  name="$(basename "$skill_file")"
  target="$SKILLS_DIR/$name"

  if [ -e "$target" ]; then
    echo "  ⏭  $name (已存在，跳过)"
    skipped=$((skipped + 1))
    continue
  fi

  cp "$skill_file" "$target"
  echo "  ✅ $name"
  installed=$((installed + 1))
done

echo ""
echo "🎉 安装完成！新增 $installed 个，跳过 $skipped 个"
echo "   Skill 目录: $SKILLS_DIR"
echo ""
echo "💡 更新所有 skill: cd $SCRIPT_DIR && git pull"
echo "💡 卸载某个 skill: rm ~/.claude/skills/<skill名>"
