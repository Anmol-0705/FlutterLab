# -*- coding: utf-8 -*-
import os
import json

from generate_experiments import EXP_DATA

# Create docs directory and root web folders
os.makedirs("docs", exist_ok=True)
for i in range(1, 13):
    os.makedirs(f"docs/exp{i}", exist_ok=True)
    os.makedirs(f"exp{i}", exist_ok=True)

# Prepare JSON data for the experiments
web_exp_data = {}
for num, data in EXP_DATA.items():
    # Extract code files
    code_dict = {}
    for fpath, code in data["files"].items():
        code_dict[fpath] = code
    web_exp_data[num] = {
        "num": num,
        "title": data["title"],
        "aim": data["aim"],
        "description": data["description"],
        "folder": data["folder"],
        "code": code_dict
    }

web_exp_json = json.dumps(web_exp_data)

def get_html_content(default_exp=1, is_standalone=False):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Flutter Lab - Experiments 1 to 12 | Anmol-0705</title>
  <!-- Google Fonts & Material Icons -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
  <style>
    :root {{
      --primary: #6750A4;
      --primary-container: #EADDFF;
      --on-primary: #FFFFFF;
      --surface: #FEF7FF;
      --surface-variant: #E7E0EC;
      --background: #F4F5F9;
      --card-bg: #FFFFFF;
      --text-main: #1D1B20;
      --text-sub: #49454F;
      --border: #CAC4D0;
      --sidebar-width: 310px;
    }}
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      font-family: 'Roboto', sans-serif;
      background: var(--background);
      color: var(--text-main);
      display: flex;
      height: 100vh;
      overflow: hidden;
    }}

    /* Sidebar */
    .sidebar {{
      width: var(--sidebar-width);
      background: #FFFFFF;
      border-right: 1px solid #E0E2EC;
      display: flex;
      flex-direction: column;
      flex-shrink: 0;
      z-index: 10;
    }}
    .sidebar-header {{
      padding: 20px;
      border-bottom: 1px solid #E0E2EC;
      background: linear-gradient(135deg, #6750A4 0%, #4F378B 100%);
      color: white;
    }}
    .sidebar-header h1 {{
      font-size: 1.25rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .sidebar-header p {{
      font-size: 0.85rem;
      opacity: 0.9;
      margin-top: 5px;
    }}
    .exp-list {{
      flex: 1;
      overflow-y: auto;
      padding: 10px;
    }}
    .exp-item {{
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 12px 14px;
      margin-bottom: 6px;
      border-radius: 12px;
      text-decoration: none;
      color: var(--text-main);
      cursor: pointer;
      transition: all 0.2s ease;
      font-size: 0.9rem;
      font-weight: 500;
    }}
    .exp-item:hover {{
      background: #F2EEFB;
    }}
    .exp-item.active {{
      background: var(--primary-container);
      color: var(--primary);
      font-weight: 700;
    }}
    .exp-badge {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 28px;
      height: 28px;
      border-radius: 50%;
      background: #ECE6F0;
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--primary);
      flex-shrink: 0;
    }}
    .exp-item.active .exp-badge {{
      background: var(--primary);
      color: white;
    }}

    /* Main Container */
    .main-content {{
      flex: 1;
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }}
    .top-bar {{
      height: 64px;
      background: #FFFFFF;
      border-bottom: 1px solid #E0E2EC;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 24px;
    }}
    .top-title {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .top-title h2 {{
      font-size: 1.15rem;
      font-weight: 600;
    }}
    .top-links {{
      display: flex;
      gap: 12px;
    }}
    .btn {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 8px 16px;
      border-radius: 20px;
      font-size: 0.85rem;
      font-weight: 500;
      cursor: pointer;
      border: 1px solid transparent;
      text-decoration: none;
      transition: background 0.2s;
    }}
    .btn-outline {{
      border-color: var(--border);
      color: var(--text-main);
      background: white;
    }}
    .btn-outline:hover {{
      background: #F4F5F9;
    }}
    .btn-primary {{
      background: var(--primary);
      color: white;
    }}
    .btn-primary:hover {{
      background: #4F378B;
    }}

    /* Tabs & Content Area */
    .content-body {{
      flex: 1;
      display: flex;
      overflow: hidden;
    }}
    .preview-pane {{
      flex: 1.2;
      background: #EEF1F6;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: flex-start;
      padding: 20px;
      overflow-y: auto;
    }}
    .device-controls {{
      display: flex;
      gap: 8px;
      margin-bottom: 16px;
      background: white;
      padding: 4px;
      border-radius: 24px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.06);
    }}
    .device-btn {{
      padding: 6px 14px;
      border: none;
      background: transparent;
      border-radius: 20px;
      cursor: pointer;
      font-size: 0.85rem;
      font-weight: 500;
      color: var(--text-sub);
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .device-btn.active {{
      background: var(--primary);
      color: white;
    }}

    /* Device Mockup Frame */
    .device-frame {{
      background: white;
      border-radius: 36px;
      box-shadow: 0 16px 40px rgba(0,0,0,0.15);
      border: 10px solid #1E1E24;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      transition: all 0.3s ease;
      position: relative;
    }}
    .device-mobile {{
      width: 380px;
      height: 720px;
    }}
    .device-tablet {{
      width: 650px;
      height: 720px;
    }}
    .device-desktop {{
      width: 100%;
      max-width: 900px;
      height: 720px;
      border-radius: 16px;
      border: 2px solid #D0D4DC;
    }}
    .status-bar {{
      height: 28px;
      background: #000;
      color: white;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 18px;
      font-size: 0.75rem;
      font-weight: 500;
      user-select: none;
    }}
    .screen-content {{
      flex: 1;
      overflow-y: auto;
      background: #FAFAFA;
      position: relative;
      display: flex;
      flex-direction: column;
    }}

    /* Details / Code Pane */
    .info-pane {{
      flex: 1;
      border-left: 1px solid #E0E2EC;
      background: white;
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }}
    .info-tabs {{
      display: flex;
      border-bottom: 1px solid #E0E2EC;
      background: #FBFBFE;
    }}
    .info-tab {{
      padding: 14px 20px;
      font-size: 0.9rem;
      font-weight: 600;
      color: var(--text-sub);
      cursor: pointer;
      border-bottom: 2px solid transparent;
      transition: all 0.2s;
    }}
    .info-tab.active {{
      color: var(--primary);
      border-bottom-color: var(--primary);
      background: white;
    }}
    .tab-content {{
      flex: 1;
      overflow-y: auto;
      padding: 24px;
      display: none;
    }}
    .tab-content.active {{
      display: block;
    }}
    .doc-section {{
      margin-bottom: 24px;
    }}
    .doc-section h3 {{
      font-size: 1rem;
      font-weight: 700;
      color: var(--primary);
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .doc-section p {{
      font-size: 0.92rem;
      line-height: 1.6;
      color: #333;
    }}
    .code-container {{
      background: #1E1E2E;
      color: #CDD6F4;
      padding: 16px;
      border-radius: 12px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.85rem;
      line-height: 1.5;
      overflow-x: auto;
      white-space: pre-wrap;
    }}

    /* Flutter UI Components Emulation */
    .fl-appbar {{
      height: 56px;
      display: flex;
      align-items: center;
      padding: 0 16px;
      color: white;
      font-weight: 600;
      font-size: 1.1rem;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
      flex-shrink: 0;
    }}
    .fl-card {{
      background: white;
      border-radius: 12px;
      padding: 16px;
      margin: 10px 14px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }}
    .fl-list-tile {{
      display: flex;
      align-items: center;
      gap: 16px;
      padding: 12px 16px;
    }}
    .fl-avatar {{
      width: 44px;
      height: 44px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: bold;
      color: white;
    }}
    .fl-btn {{
      padding: 12px 24px;
      border: none;
      border-radius: 24px;
      cursor: pointer;
      font-weight: 600;
      font-size: 0.9rem;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: transform 0.1s, opacity 0.2s;
    }}
    .fl-btn:active {{
      transform: scale(0.98);
    }}
    .fl-input {{
      width: 100%;
      padding: 14px 16px;
      border-radius: 8px;
      border: 1px solid #CCC;
      font-size: 1rem;
      margin-bottom: 14px;
      outline: none;
    }}
    .fl-input:focus {{
      border-color: #6750A4;
      box-shadow: 0 0 0 2px rgba(103,80,164,0.2);
    }}
    .fl-snackbar {{
      position: absolute;
      bottom: 20px;
      left: 20px;
      right: 20px;
      background: #322F35;
      color: white;
      padding: 14px 18px;
      border-radius: 8px;
      font-size: 0.9rem;
      box-shadow: 0 4px 12px rgba(0,0,0,0.3);
      display: none;
      animation: slideUp 0.3s ease;
      z-index: 100;
    }}
    @keyframes slideUp {{
      from {{ transform: translateY(50px); opacity: 0; }}
      to {{ transform: translateY(0); opacity: 1; }}
    }}
    @media (max-width: 900px) {{
      body {{ flex-direction: column; overflow-y: auto; height: auto; }}
      .sidebar {{ width: 100%; height: auto; }}
      .content-body {{ flex-direction: column; }}
      .preview-pane, .info-pane {{ flex: none; width: 100%; }}
      .device-mobile, .device-tablet, .device-desktop {{ width: 100%; height: 600px; }}
    }}
  </style>
</head>
<body>

  <!-- Sidebar -->
  <aside class="sidebar">
    <div class="sidebar-header">
      <h1><span class="material-icons">flutter_dash</span> Flutter Lab</h1>
      <p>Building Applications Using Flutter</p>
    </div>
    <div class="exp-list" id="expList"></div>
  </aside>

  <!-- Main Content -->
  <main class="main-content">
    <header class="top-bar">
      <div class="top-title">
        <h2 id="currentTitle">Loading Experiment...</h2>
      </div>
      <div class="top-links">
        <a id="directLink" href="#" class="btn btn-outline" target="_blank">
          <span class="material-icons" style="font-size:18px;">open_in_new</span> Direct Link
        </a>
        <a href="https://github.com/Anmol-0705/FlutterLab" class="btn btn-primary" target="_blank">
          <span class="material-icons" style="font-size:18px;">code</span> GitHub Repo
        </a>
      </div>
    </header>

    <div class="content-body">
      <!-- Preview Simulator Pane -->
      <section class="preview-pane">
        <div class="device-controls">
          <button class="device-btn active" onclick="setDevice('mobile')">
            <span class="material-icons" style="font-size:16px;">phone_iphone</span> Mobile
          </button>
          <button class="device-btn" onclick="setDevice('tablet')">
            <span class="material-icons" style="font-size:16px;">tablet_mac</span> Tablet
          </button>
          <button class="device-btn" onclick="setDevice('desktop')">
            <span class="material-icons" style="font-size:16px;">desktop_windows</span> Desktop
          </button>
        </div>

        <div class="device-frame device-mobile" id="deviceFrame">
          <div class="status-bar" id="statusBar">
            <span>9:41</span>
            <div style="display:flex; gap:6px;">
              <span class="material-icons" style="font-size:14px;">signal_cellular_4_bar</span>
              <span class="material-icons" style="font-size:14px;">wifi</span>
              <span class="material-icons" style="font-size:14px;">battery_full</span>
            </div>
          </div>
          <div class="screen-content" id="screenContent"></div>
          <div class="fl-snackbar" id="snackBar"></div>
        </div>
      </section>

      <!-- Info & Code Pane -->
      <section class="info-pane">
        <div class="info-tabs">
          <div class="info-tab active" onclick="switchTab('tabCode')">Dart Code</div>
          <div class="info-tab" onclick="switchTab('tabDocs')">Aim & Procedure</div>
        </div>
        <div class="tab-content active" id="tabCode">
          <div id="codeFilesSelect" style="margin-bottom: 12px; display: none;"></div>
          <div class="code-container" id="codeDisplay"></div>
        </div>
        <div class="tab-content" id="tabDocs">
          <div class="doc-section">
            <h3><span class="material-icons">track_changes</span> Aim</h3>
            <p id="docAim"></p>
          </div>
          <div class="doc-section">
            <h3><span class="material-icons">info</span> Description</h3>
            <p id="docDescription"></p>
          </div>
          <div class="doc-section">
            <h3><span class="material-icons">folder</span> Project Directory</h3>
            <code id="docFolder" style="font-family:monospace; background:#EFEFEF; padding:4px 8px; border-radius:4px;"></code>
          </div>
        </div>
      </section>
    </div>
  </main>

  <script>
    const expData = {web_exp_json};
    let currentExp = {default_exp};
    let currentDevice = 'mobile';
    let currentScreen = 'home'; // for navigation app

    // App state holders
    let counterVal = 0;
    let animLarge = false;
    let studentList7 = ['Raj (1)'];
    let studentList8_sql = [{{ id: 1, name: 'Anmol Samual', course: 'Computer Science' }}];
    let studentList8_fb = [{{ id: 'doc_1', name: 'Anmol Samual', course: 'Computer Science' }}];
    let apiPosts = [];

    function showSnackBar(msg) {{
      const sb = document.getElementById('snackBar');
      sb.innerText = msg;
      sb.style.display = 'block';
      setTimeout(() => {{
        sb.style.display = 'none';
      }}, 3000);
    }}

    function setDevice(type) {{
      currentDevice = type;
      document.querySelectorAll('.device-btn').forEach(b => b.classList.remove('active'));
      event.currentTarget.classList.add('active');
      const frame = document.getElementById('deviceFrame');
      frame.className = 'device-frame device-' + type;
      renderAppScreen();
    }}

    function switchTab(tabId) {{
      document.querySelectorAll('.info-tab').forEach(t => t.classList.remove('active'));
      event.currentTarget.classList.add('active');
      document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
      document.getElementById(tabId).classList.add('active');
    }}

    function selectExp(num) {{
      currentExp = num;
      currentScreen = 'home';
      window.location.hash = '/exp' + num;
      document.querySelectorAll('.exp-item').forEach(el => {{
        el.classList.toggle('active', el.dataset.num == num);
      }});
      const data = expData[num];
      document.getElementById('currentTitle').innerText = 'Experiment ' + num + ': ' + data.title;
      document.getElementById('docAim').innerText = data.aim;
      document.getElementById('docDescription').innerText = data.description;
      document.getElementById('docFolder').innerText = data.folder;
      
      const repoBase = window.location.pathname.includes('/FlutterLab') ? '/FlutterLab' : '';
      document.getElementById('directLink').href = repoBase + '/exp' + num + '/';

      // Render Code Files
      const files = Object.keys(data.code);
      const codeSelect = document.getElementById('codeFilesSelect');
      if (files.length > 1) {{
        codeSelect.style.display = 'block';
        codeSelect.innerHTML = files.map(f => `<button class="btn btn-outline" style="margin-right:8px; padding:4px 10px; font-size:0.8rem;" onclick="displayCode('${{f}}')">${{f}}</button>`).join('');
      }} else {{
        codeSelect.style.display = 'none';
      }}
      displayCode(files[0]);

      renderAppScreen();
    }}

    function displayCode(fileName) {{
      const code = expData[currentExp].code[fileName];
      document.getElementById('codeDisplay').innerText = code;
    }}

    function renderAppScreen() {{
      const screen = document.getElementById('screenContent');
      const width = document.getElementById('deviceFrame').clientWidth;
      const isMobile = width < 550;

      switch(currentExp) {{
        case 1:
          screen.innerHTML = `
            <div class="fl-appbar" style="background:#3F51B5; justify-content:center;">
              Student Profile
            </div>
            <div style="padding:16px; flex:1; overflow-y:auto;">
              <div style="background:#3F51B5; color:white; border-radius:15px; padding:20px; margin-bottom:15px; text-align:center; box-shadow:0 3px 6px rgba(0,0,0,0.2);">
                <div style="width:80px; height:80px; background:white; border-radius:50%; margin:0 auto 12px; display:flex; align-items:center; justify-content:center;">
                  <span class="material-icons" style="font-size:50px; color:#3F51B5;">person</span>
                </div>
                <h3 style="font-size:22px; margin-bottom:5px;">ARSATH AHAMED URK23CS1203</h3>
                <p style="color:#E0E0E0; font-size:15px;">Computer Science and Engineering</p>
                <p style="color:#E0E0E0; font-size:14px; margin-top:3px;">Flutter Laboratory</p>
              </div>

              <div class="fl-card" style="display:flex; justify-content:space-around; padding:18px;">
                <span class="material-icons" style="font-size:32px; color:#2196F3;">home</span>
                <span class="material-icons" style="font-size:32px; color:#4CAF50;">person</span>
                <span class="material-icons" style="font-size:32px; color:#FF9800;">settings</span>
              </div>

              <h4 style="color:#3F51B5; margin:16px 4px 8px; font-size:18px;">Subjects</h4>

              <div class="fl-card" style="background:#E3F2FD; display:flex; align-items:center; gap:16px; margin:8px 0;">
                <div class="fl-avatar" style="background:#2196F3;"><span class="material-icons">menu_book</span></div>
                <div>
                  <strong>Flutter</strong>
                  <div style="font-size:13px; color:#666;">Mobile Application Development</div>
                </div>
              </div>

              <div class="fl-card" style="background:#E8F5E9; display:flex; align-items:center; gap:16px; margin:8px 0;">
                <div class="fl-avatar" style="background:#4CAF50;"><span class="material-icons">cloud</span></div>
                <div>
                  <strong>Cloud Computing</strong>
                  <div style="font-size:13px; color:#666;">Cloud Technologies and Services</div>
                </div>
              </div>

              <div class="fl-card" style="background:#FFF3E0; display:flex; align-items:center; gap:16px; margin:8px 0;">
                <div class="fl-avatar" style="background:#FF9800;"><span class="material-icons">code</span></div>
                <div>
                  <strong>Programming</strong>
                  <div style="font-size:13px; color:#666;">Programming Fundamentals</div>
                </div>
              </div>

              <div style="background:#673AB7; color:white; border-radius:12px; padding:14px; text-align:center; font-weight:bold; margin-top:14px;">
                Welcome to Flutter Laboratory!
              </div>
            </div>
          `;
          break;

        case 2:
          const isMobileLayout = currentDevice === 'mobile';
          screen.innerHTML = `
            <div class="fl-appbar" style="background:#D0BCFF; color:#381E72;">
              Adaptive and Responsive UI
            </div>
            <div style="padding:16px; flex:1;">
              <div style="margin-bottom:12px; font-size:13px; color:#666; text-align:center;">
                Current: <b>${{isMobileLayout ? 'Mobile Layout (< 600px)' : 'Desktop / Tablet Layout (≥ 600px)'}}</b>
              </div>
              <div style="display:${{isMobileLayout ? 'flex' : 'flex'}}; flex-direction:${{isMobileLayout ? 'column' : 'row'}}; gap:12px;">
                <div class="fl-card" style="flex:1; display:flex; align-items:center; gap:14px; margin:4px;">
                  <span class="material-icons" style="font-size:32px; color:#6750A4;">${{isMobileLayout ? 'person' : 'people'}}</span>
                  <div>
                    <strong>${{isMobileLayout ? 'Student' : 'Students'}}</strong>
                    <div style="font-size:12px; color:#666;">${{isMobileLayout ? 'Mobile Layout' : 'Desktop / Tablet Layout'}}</div>
                  </div>
                </div>
                <div class="fl-card" style="flex:1; display:flex; align-items:center; gap:14px; margin:4px;">
                  <span class="material-icons" style="font-size:32px; color:#6750A4;">${{isMobileLayout ? 'menu_book' : 'school'}}</span>
                  <div>
                    <strong>Courses</strong>
                    <div style="font-size:12px; color:#666;">${{isMobileLayout ? 'Mobile Layout' : 'Desktop / Tablet Layout'}}</div>
                  </div>
                </div>
              </div>
            </div>
          `;
          break;

        case 3:
          screen.innerHTML = `
            <div class="fl-appbar" style="background:#2196F3; justify-content:center;">
              Student Registration
            </div>
            <div style="padding:20px; flex:1; display:flex; align-items:center; justify-content:center;">
              <div class="fl-card" style="width:100%; text-align:center; padding:24px;">
                <span class="material-icons" style="font-size:60px; color:#2196F3; margin-bottom:10px;">school</span>
                <h3 style="margin-bottom:20px;">Create Student Account</h3>
                <input type="text" id="stuName" class="fl-input" placeholder="Student Name" />
                <input type="email" id="stuEmail" class="fl-input" placeholder="Email" />
                <input type="password" id="stuPass" class="fl-input" placeholder="Password" />
                <button class="fl-btn btn-primary" style="width:100%; justify-content:center; background:#2196F3;" onclick="submitExp3Form()">
                  Submit
                </button>
              </div>
            </div>
          `;
          break;

        case 4:
          screen.innerHTML = `
            <div class="fl-appbar" style="background:#02569B;">Flutter Assets and Media</div>
            <div style="padding:20px; text-align:center; flex:1; overflow-y:auto;">
              <h2 style="font-size:24px; font-weight:bold; margin-bottom:20px;">Hello World</h2>
              
              <h4 style="font-size:18px; margin-bottom:10px;">Image Asset</h4>
              <div style="width:200px; height:160px; background:#E1F5FE; border-radius:16px; margin:0 auto 20px; display:flex; flex-direction:column; align-items:center; justify-content:center; border:2px dashed #0288D1;">
                <span class="material-icons" style="font-size:64px; color:#0288D1;">flutter_dash</span>
                <span style="font-size:12px; font-weight:bold; color:#0288D1; margin-top:6px;">assets/images/flutter.png</span>
              </div>

              <h4 style="font-size:18px; margin-bottom:10px;">Video Asset</h4>
              <div style="width:100%; max-width:320px; height:180px; background:#212121; border-radius:12px; margin:0 auto 16px; display:flex; flex-direction:column; align-items:center; justify-content:center; color:white;">
                <span class="material-icons" style="font-size:56px; color:#03A9F4;">videocam</span>
                <div style="font-size:13px; color:#B0BEC5; margin-top:8px;">assets/video/sample.mp4</div>
              </div>
              <button class="fl-btn btn-primary" style="background:#0288D1;" onclick="showSnackBar('Playing sample video asset...')">
                <span class="material-icons">play_arrow</span> Play Video
              </button>
            </div>
          `;
          break;

        case 5:
          if (currentScreen === 'home') {{
            screen.innerHTML = `
              <div class="fl-appbar" style="background:#9C27B0; justify-content:center;">Home</div>
              <div style="flex:1; background:linear-gradient(135deg, #9C27B0, #E91E63, #03A9F4); display:flex; align-items:center; justify-content:center; padding:20px;">
                <div class="fl-card" style="text-align:center; padding:30px; border-radius:24px; width:100%;">
                  <span class="material-icons" style="font-size:70px; color:#9C27B0;">home</span>
                  <h3 style="color:#9C27B0; margin:16px 0 8px; font-size:24px;">Welcome Home!</h3>
                  <p style="color:#777; font-size:14px; margin-bottom:24px;">Explore the different screens</p>
                  <button class="fl-btn" style="background:#E91E63; color:white; width:100%; justify-content:center;" onclick="currentScreen='profile'; renderAppScreen();">
                    <span class="material-icons">person</span> Go to Profile
                  </button>
                </div>
              </div>
            `;
          }} else if (currentScreen === 'profile') {{
            screen.innerHTML = `
              <div class="fl-appbar" style="background:#E91E63; justify-content:center;">Profile</div>
              <div style="flex:1; background:linear-gradient(135deg, #E91E63, #9C27B0, #03A9F4); display:flex; align-items:center; justify-content:center; padding:20px;">
                <div class="fl-card" style="text-align:center; padding:30px; border-radius:24px; width:100%;">
                  <div class="fl-avatar" style="width:70px; height:70px; background:#E91E63; margin:0 auto 16px;">
                    <span class="material-icons" style="font-size:42px;">person</span>
                  </div>
                  <h3 style="color:#9C27B0; font-size:24px; margin-bottom:8px;">Student Profile</h3>
                  <p style="color:#777; font-size:14px; margin-bottom:24px;">Welcome to your profile page!</p>
                  <button class="fl-btn" style="background:#03A9F4; color:white; width:100%; justify-content:center;" onclick="currentScreen='details'; renderAppScreen();">
                    <span class="material-icons">info</span> View Details
                  </button>
                </div>
              </div>
            `;
          }} else if (currentScreen === 'details') {{
            screen.innerHTML = `
              <div class="fl-appbar" style="background:#03A9F4; justify-content:center;">Details</div>
              <div style="flex:1; background:linear-gradient(135deg, #03A9F4, #9C27B0, #E91E63); display:flex; align-items:center; justify-content:center; padding:20px;">
                <div class="fl-card" style="text-align:center; padding:30px; border-radius:24px; width:100%;">
                  <span class="material-icons" style="font-size:70px; color:#03A9F4;">school</span>
                  <h3 style="color:#9C27B0; font-size:24px; margin:16px 0;">Student Details</h3>
                  <p style="font-size:15px; line-height:1.7; color:#333; margin-bottom:24px;">
                    Name: Arsath Ahamed URK23CS1203<br>
                    Course: Computer Science<br>
                    Department: CSE
                  </p>
                  <button class="fl-btn" style="background:#9C27B0; color:white; width:100%; justify-content:center;" onclick="currentScreen='profile'; renderAppScreen();">
                    <span class="material-icons">arrow_back</span> Back to Profile
                  </button>
                </div>
              </div>
            `;
          }}
          break;

        case 6:
          screen.innerHTML = `
            <div class="fl-appbar" style="background:#673AB7; justify-content:center;">Flutter Animations</div>
            <div style="flex:1; background:#EDE7F6; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:20px;">
              <div id="animBox" style="
                width:${{animLarge ? '260px' : '140px'}};
                height:${{animLarge ? '260px' : '140px'}};
                border-radius:${{animLarge ? '45px' : '18px'}};
                background:#B39DDB;
                box-shadow:0 8px 24px rgba(0,0,0,0.18);
                display:flex;
                align-items:center;
                justify-content:center;
                color:white;
                font-size:${{animLarge ? '32px' : '22px'}};
                font-weight:bold;
                transition:all 1s cubic-bezier(0.4, 0, 0.2, 1);
              ">
                Flutter
              </div>
              <div style="margin-top:35px;">
                <button class="fl-btn" style="background:#673AB7; color:white; padding:14px 32px;" onclick="toggleAnimExp6()">
                  <span class="material-icons">animation</span> Animate
                </button>
              </div>
              <div style="margin-top:16px; color:#673AB7; font-weight:600;">
                ${{animLarge ? 'Widget is Large' : 'Widget is Small'}}
              </div>
            </div>
          `;
          break;

        case 7:
          screen.innerHTML = `
            <div class="fl-appbar" style="background:#4A148C;">Student State Management</div>
            <div style="padding:16px; flex:1; display:flex; flex-direction:column;">
              <button class="fl-btn" style="background:#4A148C; color:white; margin:0 auto 16px;" onclick="addExp7Student()">
                <span class="material-icons">add</span> Add Student
              </button>
              <div style="flex:1; overflow-y:auto;">
                ${{studentList7.map((name, i) => `
                  <div class="fl-card" style="display:flex; align-items:center; gap:14px; margin:6px 0;">
                    <div class="fl-avatar" style="background:#7B1FA2;">${{i+1}}</div>
                    <div>
                      <strong>${{name}}</strong>
                      <div style="font-size:12px; color:#666;">Course: CSE (JSON Serialized)</div>
                    </div>
                  </div>
                `).join('')}}
              </div>
            </div>
          `;
          break;

        case 8:
          screen.innerHTML = `
            <div class="fl-appbar" style="background:#303F9F; justify-content:center;">Student Data Persistence</div>
            <div style="padding:16px; flex:1; overflow-y:auto;">
              <h3 style="text-align:center; font-size:20px; font-weight:bold;">SQLite + Firebase</h3>
              <p style="text-align:center; font-size:12px; color:#666; margin-bottom:14px;">Web: SQLite WASM + Firebase</p>

              <div class="fl-card">
                <h4 style="margin-bottom:12px;">Add Student</h4>
                <input type="text" id="exp8Name" class="fl-input" placeholder="Student Name" style="padding:10px;" />
                <input type="text" id="exp8Course" class="fl-input" placeholder="Course" style="padding:10px;" />
                <button class="fl-btn btn-primary" style="background:#303F9F; width:100%; justify-content:center;" onclick="addExp8Student()">
                  Save to SQLite + Firebase
                </button>
              </div>

              <h4 style="margin:16px 4px 8px; color:#303F9F;">SQLite - Local Storage</h4>
              ${{studentList8_sql.map(s => `
                <div class="fl-card" style="display:flex; align-items:center; justify-content:space-between; padding:10px 14px; margin:6px 0;">
                  <div>
                    <strong>${{s.name}}</strong>
                    <div style="font-size:12px; color:#666;">${{s.course}}</div>
                  </div>
                  <span class="material-icons" style="color:#E53935; cursor:pointer;" onclick="deleteExp8Student(${{s.id}})">delete</span>
                </div>
              `).join('')}}

              <h4 style="margin:20px 4px 8px; color:#E65100;">Firebase - Cloud Storage</h4>
              ${{studentList8_fb.map(s => `
                <div class="fl-card" style="display:flex; align-items:center; justify-content:space-between; padding:10px 14px; margin:6px 0;">
                  <div style="display:flex; align-items:center; gap:10px;">
                    <span class="material-icons" style="color:#FFA000;">cloud</span>
                    <div>
                      <strong>${{s.name}}</strong>
                      <div style="font-size:12px; color:#666;">${{s.course}}</div>
                    </div>
                  </div>
                  <span class="material-icons" style="color:#E53935; cursor:pointer;" onclick="deleteExp8Student('${{s.id}}')">delete</span>
                </div>
              `).join('')}}
            </div>
          `;
          break;

        case 9:
          screen.innerHTML = `
            <div class="fl-appbar" style="background:#BFA2DB; color:white;">REST API Posts</div>
            <div id="postsContainer" style="padding:12px; flex:1; overflow-y:auto;">
              <div style="text-align:center; padding:40px;">
                <span class="material-icons" style="font-size:48px; color:#9C7AC7; animation:spin 1s infinite linear;">refresh</span>
                <p style="margin-top:10px; color:#666;">Fetching live data from JSONPlaceholder...</p>
              </div>
            </div>
          `;
          fetchExp9Posts();
          break;

        case 10:
          screen.innerHTML = `
            <div class="fl-appbar" style="background:#6750A4;">Experiment 10 - Android Target</div>
            <div style="flex:1; display:flex; flex-direction:column; align-items:center; justify-content:center; position:relative;">
              <span class="material-icons" style="font-size:70px; color:#4CAF50; margin-bottom:16px;">android</span>
              <p style="font-size:15px; color:#555;">You have pushed the button this many times:</p>
              <h1 style="font-size:42px; font-weight:bold; margin-top:8px;">${{counterVal}}</h1>
              <button style="position:absolute; bottom:24px; right:24px; width:56px; height:56px; border-radius:16px; background:#6750A4; color:white; border:none; box-shadow:0 4px 10px rgba(0,0,0,0.3); cursor:pointer; display:flex; align-items:center; justify-content:center;" onclick="counterVal++; renderAppScreen();">
                <span class="material-icons">add</span>
              </button>
            </div>
          `;
          break;

        case 11:
          screen.innerHTML = `
            <div class="fl-appbar" style="background:#673AB7; justify-content:center;">iOS Flutter Application</div>
            <div style="flex:1; background:#F3E5F5; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; padding:20px;">
              <span class="material-icons" style="font-size:80px; color:#673AB7; margin-bottom:12px;">phone_iphone</span>
              <h2 style="font-size:24px; color:#673AB7; font-weight:bold; margin-bottom:6px;">Flutter iOS App</h2>
              <p style="font-size:15px; color:#555; margin-bottom:20px;">Experiment 11<br>Add iOS as a Build Target</p>
              <button class="fl-btn" style="background:#673AB7; color:white;" onclick="showSnackBar('Button clicked successfully!')">
                Test Button
              </button>
              <div style="color:#2E7D32; font-weight:bold; margin-top:16px; display:flex; align-items:center; gap:4px;">
                <span class="material-icons" style="font-size:18px;">check_circle</span> Application Ready
              </div>
            </div>
          `;
          break;

        case 12:
          const isWebMobile = currentDevice === 'mobile';
          screen.innerHTML = `
            <div class="fl-appbar" style="background:#2196F3;">Flutter Web Application</div>
            <div style="flex:1; display:flex; align-items:center; justify-content:center; background:#FAFAFA;">
              <h2 style="font-size:${{isWebMobile ? '24px' : '32px'}}; color:#1976D2; font-weight:bold; text-align:center;">
                ${{isWebMobile ? 'Mobile Web Layout' : 'Desktop Web Layout'}}
              </h2>
            </div>
          `;
          break;
      }}
    }}

    function submitExp3Form() {{
      const name = document.getElementById('stuName').value.trim();
      if (!name) {{
        showSnackBar('Enter student name');
        return;
      }}
      showSnackBar('Form submitted successfully');
    }}

    function toggleAnimExp6() {{
      animLarge = !animLarge;
      renderAppScreen();
    }}

    function addExp7Student() {{
      studentList7.push('Raj (' + (studentList7.length + 1) + ')');
      renderAppScreen();
    }}

    function addExp8Student() {{
      const name = document.getElementById('exp8Name').value.trim();
      const course = document.getElementById('exp8Course').value.trim();
      if (!name || !course) {{
        showSnackBar('Please enter student name and course');
        return;
      }}
      const newId = studentList8_sql.length + 1;
      studentList8_sql.push({{ id: newId, name, course }});
      studentList8_fb.push({{ id: 'doc_' + newId, name, course }});
      showSnackBar('Student saved to SQLite and Firebase');
      renderAppScreen();
    }}

    function deleteExp8Student(id) {{
      studentList8_sql = studentList8_sql.filter(s => s.id !== id);
      studentList8_fb = studentList8_fb.filter(s => s.id !== id);
      renderAppScreen();
    }}

    async function fetchExp9Posts() {{
      try {{
        if (apiPosts.length === 0) {{
          const res = await fetch('https://jsonplaceholder.typicode.com/posts?_limit=10');
          apiPosts = await res.json();
        }}
        const container = document.getElementById('postsContainer');
        if (container) {{
          container.innerHTML = apiPosts.map(p => `
            <div class="fl-card" style="background:#F0E6F7; margin:8px 0; padding:12px;">
              <div style="display:flex; align-items:center; gap:10px; margin-bottom:6px;">
                <div class="fl-avatar" style="background:#9C7AC7; width:28px; height:28px; font-size:12px;">${{p.id}}</div>
                <strong style="font-size:14px; text-transform:capitalize;">${{p.title}}</strong>
              </div>
              <p style="font-size:13px; color:#555; line-height:1.4;">${{p.body}}</p>
            </div>
          `).join('');
        }}
      }} catch (e) {{
        const container = document.getElementById('postsContainer');
        if (container) {{
          container.innerHTML = '<div style="text-align:center; padding:20px; color:red;">Failed to load live data</div>';
        }}
      }}
    }}

    // Initialize sidebar
    const list = document.getElementById('expList');
    list.innerHTML = Object.keys(expData).map(num => `
      <div class="exp-item ${{num == currentExp ? 'active' : ''}}" data-num="${{num}}" onclick="selectExp(${{num}})">
        <span class="exp-badge">${{num}}</span>
        <span>${{expData[num].title}}</span>
      </div>
    `).join('');

    // Check hash for direct route
    const hashMatch = window.location.hash.match(/#\\/exp(\\d+)/);
    if (hashMatch) {{
      currentExp = parseInt(hashMatch[1]);
    }}

    selectExp(currentExp);
  </script>
</body>
</html>
"""

# 1. Write docs/index.html (hub)
with open("docs/index.html", "w", encoding="utf-8") as f:
    f.write(get_html_content(1))

# 2. Write root index.html (for repository root GitHub Pages)
with open("index.html", "w", encoding="utf-8") as f:
    f.write(get_html_content(1))

# 3. Write docs/404.html (for SPA GitHub Pages redirect handling)
with open("docs/404.html", "w", encoding="utf-8") as f:
    f.write(get_html_content(1))

# 4. Write docs/exp{i}/index.html and exp{i}/index.html for direct individual links
for i in range(1, 13):
    html = get_html_content(i, is_standalone=True)
    with open(f"docs/exp{i}/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    with open(f"exp{i}/index.html", "w", encoding="utf-8") as f:
        f.write(html)

print("Successfully generated all GitHub Pages web files and standalone experiment routes!")
