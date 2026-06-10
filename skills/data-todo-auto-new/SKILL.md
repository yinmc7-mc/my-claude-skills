---
name: data-todo-auto-new
description: Use this skill when automatically creating monthly todo lists in Apple Notes with proper formatting (24px large text for month/week, bold for dates, checklist format for items). Use for creating structured monthly plans organized by weeks and days, handling cross-month periods correctly.
---

# Main Instructions

This skill automates the creation of monthly todo lists in Apple Notes with standardized formatting based on successful patterns from existing monthly notes.

## Core Format Requirements

### Hierarchy and Styling
- **Month/Week Headers**: `<b><span style="font-size: 24px">` (24px large bold)
- **Date Headers**: `<b>` (bold only)
- **Todo Items**: `<ul><li>` (checklist format)

### HTML Format Pattern
```html
<div><b><span style="font-size: 24px">【X月】</span></b><br></div>
<div><br></div>
<div><b><span style="font-size: 24px">第X周（M.D-M.D）</span></b><br></div>
<div><b>M.D（星期）</b><br></div>
<ul>
<li></li>
<li></li>
<li></li>
</ul>
```

## Step-by-Step Process

### 1. Identify Calendar Details
- Determine month to create (e.g., 4月, 5月)
- Calculate weeks: Monday to Sunday
- Handle cross-month periods correctly (e.g., 4.27-5.3)

### 2. Generate HTML Content
Build note body with proper structure:
- Month header: `【X月】`
- Weekly sections with date ranges
- Daily subsections with weekday indicators
- Empty `<ul><li>` items for user to fill

### 3. Create Apple Note via AppleScript
Use AppleScript to:
1. Locate "我的Mac" account → "Notes" folder
2. Delete existing note with same title (if exists)
3. Create new note with generated HTML content
4. Set title to `【X月】`

## Week Organization Rules

### Standard Week Structure
- **Week 1**: First Monday-Sunday of month
- **Subsequent Weeks**: Each Monday-Sunday
- **Last Week**: May include days from next month

### Weekday Mapping
- 一 (Monday), 二 (Tuesday), 三 (Wednesday)
- 四 (Thursday), 五 (Friday), 六 (Saturday), 日 (Sunday)

### Date Range Format
- Use format: `M.D-M.D` (e.g., 4.1-4.7)
- Week 1 starts on actual Monday (not necessarily 1st)
- Last week ends on Sunday of month

## AppleScript Template

```applescript
tell application "Notes"
    -- Delete existing note if present
    set allAccounts to every account
    repeat with currentAccount in allAccounts
        set accountName to name of currentAccount
        if accountName is "我的Mac" then
            set allFolders to every folder of currentAccount
            repeat with currentFolder in allFolders
                set folderName to name of currentFolder
                if folderName is "Notes" then
                    set allNotes to every note of currentFolder
                    repeat with currentNote in allNotes
                        set noteName to name of currentNote
                        if noteName is "【X月】" then
                            delete currentNote
                        end if
                    end repeat
                end if
            end repeat
        end if
    end repeat
    
    -- Create new note with HTML content
    repeat with currentAccount in allAccounts
        set accountName to name of currentAccount
        if accountName is "我的Mac" then
            set allFolders to every folder of currentAccount
            repeat with currentFolder in allFolders
                set folderName to name of currentFolder
                if folderName is "Notes" then
                    set newNote to make new note at currentFolder
                    set name of newNote to "【X月】"
                    set body of newNote to "[GENERATED_HTML_CONTENT]"
                    return "✓ 月度待办清单已创建"
                end if
            end repeat
        end if
    end repeat
end tell
```

## Month Data Reference

### 2026 Month Calendars

**April 2026** (4月)
- Week 1: 4.1-4.5 (周三-周日)
- Week 2: 4.6-4.12 (周一-周日)
- Week 3: 4.13-4.19 (周一-周日)
- Week 4: 4.20-4.26 (周一-周日)
- Week 5: 4.27-5.3 (周一-周日, cross-month)

**May 2026** (5月)
- Week 1: 5.4-5.10 (周一-周日)
- Week 2: 5.11-5.17 (周一-周日)
- Week 3: 5.18-5.24 (周一-周日)
- Week 4: 5.25-5.31 (周一-周日)

## Examples

### Example 1: Create April 2026 Todo List
```bash
# Invoke skill with month specification
User: "创建4月的待办清单"
```
Generates:
```
【4月】
第1周（4.1-4.5）
4.1（三）
- [ ]
- [ ]
- [ ]
... (full 5 weeks)
```

### Example 2: Cross-Month Week
When month ends mid-week (e.g., April 30 is Thursday), include May dates:
```
第5周（4.27-5.3）
4.27（一）到 5.3（日）
```

## Common Scenarios

### Creating First Month
- Generate complete month with 4-5 weeks
- Handle first month starting mid-week (e.g., Wednesday)

### Updating Existing Month
- Delete existing note before recreating
- Preserve formatting consistency
- Maintain same HTML structure

### Cross-Month Periods
- Include days from next month in last week
- Continue Monday-Sunday pattern regardless of month boundary
- Use correct weekday indicators for each date

## Best Practices

### HTML Escaping
- Always escape special characters: `<` → `&lt;`, `>` → `&gt;`, `"` → `&quot;`
- Ensure proper nesting of tags
- Close all `<div>`, `<b>`, `<span>`, `<ul>` tags

### AppleScript Safety
- Use exact account name matching: "我的Mac"
- Use exact folder name matching: "Notes"
- Handle cases where note doesn't exist (no error)
- Return success/failure status

### Validation After Creation
- Verify note exists in Notes app
- Check HTML renders correctly (not showing raw tags)
- Ensure all weeks and days are present
- Confirm weekday indicators are accurate

## Troubleshooting

### Note Not Visible
- Restart Notes app
- Check "Recently Deleted" folder
- Verify "我的Mac" account and "Notes" folder exist

### Formatting Issues
- HTML tags visible in note: Check for missing `<br>` tags
- Weekday indicators wrong: Verify calendar calculation
- Missing weeks: Ensure complete date range covered

### AppleScript Errors
- Account name mismatch: Use Chinese "我的Mac" not English
- Folder not found: Confirm "Notes" folder exists
- Permission denied: Notes app may be locked/syncing

## Success Indicators

✓ Note appears in Apple Notes under "备忘录" account
✓ Month and week headers display in 24px large text
✓ Dates display as bold
✓ Checklist items show as empty boxes (☐)
✓ Weekday indicators are correct (一, 二, 三, 四, 五, 六, 日)
✓ Week ranges follow Monday-Sunday pattern
✓ Cross-month weeks include next month dates