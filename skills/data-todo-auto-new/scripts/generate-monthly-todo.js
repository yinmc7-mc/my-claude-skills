#!/usr/bin/env node

/**
 * Generate monthly todo list HTML for Apple Notes
 * Format: 24px large text for month/week, bold for dates, checklist for items
 */

function getMonthData(year, month) {
    const firstDay = new Date(year, month - 1, 1);
    const lastDay = new Date(year, month, 0);
    const daysInMonth = lastDay.getDate();
    
    // Get the first Monday
    let currentDay = new Date(firstDay);
    while (currentDay.getDay() !== 1) { // 1 = Monday
        currentDay.setDate(currentDay.getDate() + 1);
    }
    
    const weeks = [];
    const weekdayNames = ['日', '一', '二', '三', '四', '五', '六'];
    
    let weekStart = new Date(currentDay);
    let weekNumber = 1;
    
    while (weekStart <= lastDay) {
        const days = [];
        const weekEnd = new Date(weekStart);
        weekEnd.setDate(weekEnd.getDate() + 6); // Sunday
        
        // Generate days for this week
        const tempDay = new Date(weekStart);
        while (tempDay <= weekEnd && (tempDay.getMonth() === month - 1 || tempDay.getMonth() === month)) {
            days.push({
                date: tempDay,
                month: tempDay.getMonth() + 1,
                day: tempDay.getDate(),
                weekday: weekdayNames[tempDay.getDay()]
            });
            tempDay.setDate(tempDay.getDate() + 1);
        }
        
        if (days.length > 0) {
            weeks.push({
                number: weekNumber,
                days: days
            });
            weekNumber++;
        }
        
        // Move to next Monday
        weekStart = new Date(weekEnd);
        weekStart.setDate(weekStart.getDate() + 1);
    }
    
    return weeks;
}

function generateHTML(year, month) {
    const monthNames = ['1月', '2月', '3月', '4月', '5月', '6月', 
                       '7月', '8月', '9月', '10月', '11月', '12月'];
    
    const weeks = getMonthData(year, month);
    
    let html = `<div><b><span style="font-size: 24px">【</span></b><b><span style="font-size: 24px">${monthNames[month - 1]}</span></b><b><span style="font-size: 24px">】</span></b><br></div>`;
    
    weeks.forEach((week, index) => {
        // Week header
        const firstDay = week.days[0];
        const lastDay = week.days[week.days.length - 1];
        const weekRange = `${firstDay.month}.${firstDay.day}-${lastDay.month}.${lastDay.day}`;
        
        html += `<div><br></div>`;
        html += `<div><b><span style="font-size: 24px">第</span></b><b><span style="font-size: 24px">${week.number}</span></b><b><span style="font-size: 24px">周（</span></b><b><span style="font-size: 24px">${weekRange}</span></b><b><span style="font-size: 24px">）</span></b><b><span style="font-size: 24px"><br></span></b></div>`;
        
        // Days
        week.days.forEach(day => {
            html += `<div><b>${day.month}.${day.day}</b><b>（${day.weekday}）</b><b><br></b></div>`;
            html += `<ul>`;
            html += `<li> </li>`;
            html += `<li> </li>`;
            html += `<li> </li>`;
            html += `</ul>`;
        });
    });
    
    return html;
}

function generateAppleScript(month) {
    const currentYear = new Date().getFullYear();
    const html = generateHTML(currentYear, month);
    
    // Escape special characters for AppleScript
    const escapedHtml = html
        .replace(/\\/g, '\\\\')
        .replace(/"/g, '\\"')
        .replace(/\n/g, '\\\n');
    
    const script = `tell application "Notes"
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
                        if noteName is "【${month}月】" then
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
                    set name of newNote to "【${month}月】"
                    set body of newNote to "${escapedHtml}"
                    return "✓ ${month}月待办清单已创建"
                end if
            end repeat
        end if
    end repeat
    
    return "创建失败"
end tell`;

    return script;
}

// CLI interface
const args = process.argv.slice(2);
if (args.length === 0) {
    console.log('Usage: node generate-monthly-todo.js <month>');
    console.log('Example: node generate-monthly-todo.js 4');
    console.log('\nThis will:');
    console.log('1. Generate HTML content for the specified month');
    console.log('2. Create AppleScript to insert into Notes');
    console.log('3. Save to /tmp/create_month_todo.applescript');
    console.log('4. Execute the AppleScript');
    process.exit(1);
}

const month = parseInt(args[0]);
if (isNaN(month) || month < 1 || month > 12) {
    console.error('Invalid month. Please specify a number between 1 and 12.');
    process.exit(1);
}

// Generate and save AppleScript
const appleScript = generateAppleScript(month);
const scriptPath = `/tmp/create_month_todo.applescript`;
const fs = require('fs');
fs.writeFileSync(scriptPath, appleScript, 'utf-8');

console.log(`✓ AppleScript generated: ${scriptPath}`);
console.log(`✓ Executing AppleScript for ${month}月...`);

// Execute AppleScript
const { execSync } = require('child_process');
try {
    const result = execSync(`osascript "${scriptPath}"`, { encoding: 'utf-8' });
    console.log(result);
} catch (error) {
    console.error('✗ Failed to execute AppleScript:', error.message);
    process.exit(1);
}