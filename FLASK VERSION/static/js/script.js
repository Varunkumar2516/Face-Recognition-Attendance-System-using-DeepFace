
// --- Data ---
let students=[
  {id:'STU001',name:'Arjun Patel',courseType:'Bachelor\'s',department:'Computer Science',section:'A',batch:'2021-2025',year:'3rd Year',semester:'6th',classRoll:'1',universityRoll:'2021CS001',gender:'Male',dob:'2003-05-15',phone:'+91 9876543210',email:'arjun@college.edu',photoOption:'capture'},
  {id:'STU002',name:'Priya Sharma',courseType:'Bachelor\'s',department:'Information Tech',section:'B',batch:'2022-2026',year:'2nd Year',semester:'4th',classRoll:'2',universityRoll:'2022IT002',gender:'Female',dob:'2004-03-22',phone:'+91 9123456789',email:'priya@college.edu',photoOption:'capture'},
  {id:'STU003',name:'Rahul Kumar',courseType:'Bachelor\'s',department:'Electronics',section:'C',batch:'2021-2025',year:'3rd Year',semester:'6th',classRoll:'3',universityRoll:'2021EC003',gender:'Male',dob:'2002-11-08',phone:'+91 9988776655',email:'rahul@college.edu',photoOption:'skip'},
  {id:'STU004',name:'Sneha Gupta',courseType:'Bachelor\'s',department:'Computer Science',section:'A',batch:'2023-2027',year:'1st Year',semester:'2nd',classRoll:'4',universityRoll:'2023CS004',gender:'Female',dob:'2005-07-12',phone:'+91 9876543211',email:'sneha@college.edu',photoOption:'capture'},
];

let teachers=[
  {id:'TCH001',name:'Dr. Rajesh Kumar',department:'Computer Science',designation:'Professor',specialization:'Artificial Intelligence',experience:15,gender:'Male',dob:'1968-02-20',phone:'+91 9876543200',email:'rajesh@college.edu',officePhone:'+91 1234567890',qualification:'PhD in Computer Science',photoOption:'capture'},
  {id:'TCH002',name:'Prof. Anjali Singh',department:'Information Tech',designation:'Associate Professor',specialization:'Data Science',experience:10,gender:'Female',dob:'1975-06-15',phone:'+91 9876543201',email:'anjali@college.edu',officePhone:'+91 1234567891',qualification:'PhD in Information Technology',photoOption:'capture'},
  {id:'TCH003',name:'Dr. Vikram Patel',department:'Electronics',designation:'Assistant Professor',specialization:'Embedded Systems',experience:7,gender:'Male',dob:'1982-11-30',phone:'+91 9876543202',email:'vikram@college.edu',officePhone:'+91 1234567892',qualification:'PhD in Electronics',photoOption:'skip'},
];

const attendance=[
  {id:'STU001',name:'Arjun Patel',course:'Computer Science',date:'2025-01-15',time:'09:02 AM',status:'Present'},
  {id:'STU002',name:'Priya Sharma',course:'Information Tech',date:'2025-01-15',time:'09:05 AM',status:'Present'},
  {id:'STU003',name:'Rahul Kumar',course:'Electronics',date:'2025-01-15',time:'—',status:'Absent'},
  {id:'STU004',name:'Sneha Gupta',course:'Computer Science',date:'2025-01-15',time:'09:12 AM',status:'Present'},
  {id:'STU001',name:'Arjun Patel',course:'Computer Science',date:'2025-01-14',time:'08:58 AM',status:'Present'},
  {id:'STU003',name:'Rahul Kumar',course:'Electronics',date:'2025-01-14',time:'09:20 AM',status:'Present'},
];

let isDetecting=false,detectionInterval=null;

// --- Config + Element SDK ---
const defaultConfig={
  background_color:'#0b1120',
  surface_color:'#111827',
  text_color:'#f1f5f9',
  accent_color:'#3b82f6',
  secondary_color:'#22c55e',
  font_family:'Outfit',
  font_size:16,
  welcome_message:'Welcome, Admin',
  system_title:'Face Recognition System',
  developer_name:'Alex Chen',
  developer_role:'Full Stack Developer & AI Engineer'
};

function applyConfig(c){
  const el=k=>document.getElementById(k);
  if(el('welcomeMsg'))el('welcomeMsg').textContent=c.welcome_message||defaultConfig.welcome_message;
  if(el('navTitle'))el('navTitle').textContent=c.system_title||defaultConfig.system_title;
  if(el('devName'))el('devName').textContent=c.developer_name||defaultConfig.developer_name;
  if(el('devRole'))el('devRole').textContent=c.developer_role||defaultConfig.developer_role;
  const ff=c.font_family||defaultConfig.font_family;
  document.body.style.fontFamily=`${ff}, sans-serif`;
}

if(window.elementSdk){
  window.elementSdk.init({
    defaultConfig,
    onConfigChange:async(c)=>applyConfig(c),
    mapToCapabilities:(c)=>({
      recolorables:[
        {get:()=>c.background_color||defaultConfig.background_color,set:v=>{c.background_color=v;window.elementSdk.setConfig({background_color:v})}},
        {get:()=>c.surface_color||defaultConfig.surface_color,set:v=>{c.surface_color=v;window.elementSdk.setConfig({surface_color:v})}},
        {get:()=>c.text_color||defaultConfig.text_color,set:v=>{c.text_color=v;window.elementSdk.setConfig({text_color:v})}},
        {get:()=>c.accent_color||defaultConfig.accent_color,set:v=>{c.accent_color=v;window.elementSdk.setConfig({accent_color:v})}},
        {get:()=>c.secondary_color||defaultConfig.secondary_color,set:v=>{c.secondary_color=v;window.elementSdk.setConfig({secondary_color:v})}},
      ],
      borderables:[],
      fontEditable:{get:()=>c.font_family||defaultConfig.font_family,set:v=>{c.font_family=v;window.elementSdk.setConfig({font_family:v})}},
      fontSizeable:{get:()=>c.font_size||defaultConfig.font_size,set:v=>{c.font_size=v;window.elementSdk.setConfig({font_size:v})}}
    }),
    mapToEditPanelValues:(c)=>new Map([
      ['welcome_message',c.welcome_message||defaultConfig.welcome_message],
      ['system_title',c.system_title||defaultConfig.system_title],
      ['developer_name',c.developer_name||defaultConfig.developer_name],
      ['developer_role',c.developer_role||defaultConfig.developer_role],
    ])
  });
}

// --- Navigation ---
function navigateTo(page){
  document.querySelectorAll('.page').forEach(p=>{p.classList.remove('active');p.style.display='none'});
  const target=document.getElementById('page-'+page);
  if(target){target.style.display='block';setTimeout(()=>target.classList.add('active'),10)}
  document.querySelectorAll('.nav-item').forEach(n=>n.classList.toggle('active',n.dataset.page===page));
  if(window.innerWidth<768)document.getElementById('sidebar').classList.remove('mobile-open');
  lucide.createIcons();
}

function toggleSidebar(){
  const sb=document.getElementById('sidebar');
  if(window.innerWidth<768){sb.classList.toggle('mobile-open')}else{sb.classList.toggle('collapsed')}
}

// --- Theme ---
let isDark=true;
function toggleTheme(){
  isDark=!isDark;
  document.body.classList.toggle('light',!isDark);
  lucide.createIcons();
}

// --- Toast ---
function showToast(msg,type='success'){
  const t=document.getElementById('toast');
  t.className='toast toast-'+type;
  t.innerHTML=`<i data-lucide="${type==='success'?'check-circle':type==='error'?'x-circle':'info'}" style="width:18px;height:18px"></i>${msg}`;
  t.classList.add('show');
  lucide.createIcons();
  setTimeout(()=>t.classList.remove('show'),3000);
}

// --- Students ---
function renderStudents(list){
  const b=document.getElementById('studentBody');
  b.innerHTML=list.map((s,i)=>`<tr>
    <td style="font-weight:600">${s.id}</td><td>${s.name}</td><td>${s.department}</td><td>${s.year}</td><td>${s.email}</td>
    <td><div style="display:flex;gap:6px">
      <button class="btn btn-outline" style="padding:6px 10px;font-size:12px" onclick="editStudent(${students.indexOf(s)})"><i data-lucide="edit" style="width:14px;height:14px"></i></button>
      <button class="btn btn-outline" style="padding:6px 10px;font-size:12px;border-color:rgba(239,68,68,.3);color:#ef4444" onclick="deleteStudent(${students.indexOf(s)})"><i data-lucide="trash-2" style="width:14px;height:14px"></i></button>
    </div></td></tr>`).join('');
  lucide.createIcons();
}

function filterStudents(){
  const q=document.getElementById('studentSearch').value.toLowerCase();
  const c=document.getElementById('courseFilter').value;
  renderStudents(students.filter(s=>(!q||s.name.toLowerCase().includes(q)||s.id.toLowerCase().includes(q))&&(!c||s.course===c)));
}

// --- Teachers ---
function renderTeachers(list){
  const b=document.getElementById('teacherBody');
  b.innerHTML=list.map((t,i)=>`<tr>
    <td style="font-weight:600">${t.id}</td><td>${t.name}</td><td>${t.department}</td><td>${t.designation}</td><td>${t.email}</td>
    <td><div style="display:flex;gap:6px">
      <button class="btn btn-outline" style="padding:6px 10px;font-size:12px" onclick="editTeacher(${teachers.indexOf(t)})"><i data-lucide="edit" style="width:14px;height:14px"></i></button>
      <button class="btn btn-outline" style="padding:6px 10px;font-size:12px;border-color:rgba(239,68,68,.3);color:#ef4444" onclick="deleteTeacher(${teachers.indexOf(t)})"><i data-lucide="trash-2" style="width:14px;height:14px"></i></button>
    </div></td></tr>`).join('');
  lucide.createIcons();
}

function filterTeachers(){
  const q=document.getElementById('teacherSearch').value.toLowerCase();
  const d=document.getElementById('departmentFilter').value;
  renderTeachers(teachers.filter(t=>(!q||t.name.toLowerCase().includes(q)||t.id.toLowerCase().includes(q))&&(!d||t.department===d)));
}

function handleTeacherSubmit(e){
  e.preventDefault();
  const idx=+document.getElementById('editTeacherIndex').value;
  const photoOption=document.querySelector('input[name="teacherPhotoOption"]:checked')?.value||'capture';
  const t={
    id:document.getElementById('tId').value||'TCH'+(String(Math.max(...teachers.map(tt=>parseInt(tt.id.slice(3))||0))+1).padStart(3,'0')),
    name:document.getElementById('tName').value,
    department:document.getElementById('tDepartment').value,
    designation:document.getElementById('tDesignation').value,
    specialization:document.getElementById('tSpecialization').value,
    experience:+document.getElementById('tExperience').value||0,
    gender:document.getElementById('tGender').value,
    dob:document.getElementById('tDOB').value,
    phone:document.getElementById('tPhone').value,
    email:document.getElementById('tEmail').value,
    officePhone:document.getElementById('tOfficePhone').value,
    qualification:document.getElementById('tQualification').value,
    photoOption:photoOption
  };
  if(idx>=0){teachers[idx]=t;showToast('Teacher updated successfully!','success')}else{teachers.push(t);showToast('Teacher added successfully!','success')}
  closeTeacherModal();renderTeachers(teachers);
}

function editTeacher(i){
  const t=teachers[i];
  document.getElementById('editTeacherIndex').value=i;
  document.getElementById('tId').value=t.id;
  document.getElementById('tName').value=t.name;
  document.getElementById('tDepartment').value=t.department||'';
  document.getElementById('tDesignation').value=t.designation||'';
  document.getElementById('tSpecialization').value=t.specialization||'';
  document.getElementById('tExperience').value=t.experience||'';
  document.getElementById('tGender').value=t.gender||'';
  document.getElementById('tDOB').value=t.dob||'';
  document.getElementById('tPhone').value=t.phone||'';
  document.getElementById('tEmail').value=t.email||'';
  document.getElementById('tOfficePhone').value=t.officePhone||'';
  document.getElementById('tQualification').value=t.qualification||'';
  if(t.photoOption==='skip')document.getElementById('teacherPhotoSkip').checked=true;
  else document.getElementById('teacherPhotoCapture').checked=true;
  document.getElementById('teacherModalTitle').textContent='Edit Teacher';
  document.getElementById('submitTeacherBtn').innerHTML='<i data-lucide="save" style="width:16px;height:16px"></i> Update Teacher';
  document.getElementById('deleteTeacherBtn').style.display='inline-flex';
  document.getElementById('teacherModal').classList.add('show');
  lucide.createIcons();
}

function deleteTeacher(i){
  document.getElementById('deleteModal').classList.add('show');
  document.getElementById('confirmDeleteBtn').onclick=()=>{
    teachers.splice(i,1);renderTeachers(teachers);
    document.getElementById('deleteModal').classList.remove('show');
    showToast('Teacher deleted successfully','success');
  };
  lucide.createIcons();
}

function closeTeacherModal(){
  document.getElementById('teacherModal').classList.remove('show');
  document.getElementById('teacherForm').reset();
  document.getElementById('editTeacherIndex').value=-1;
  document.getElementById('teacherModalTitle').textContent='Teacher Registration Form';
  document.getElementById('submitTeacherBtn').innerHTML='<i data-lucide="save" style="width:16px;height:16px"></i> Save Teacher';
  document.getElementById('deleteTeacherBtn').style.display='none';
  document.getElementById('teacherPhotoCapture').checked=true;
}

function resetTeacherForm(){
  document.getElementById('teacherForm').reset();
  document.getElementById('teacherPhotoCapture').checked=true;
  document.getElementById('tId').value='';
  showToast('Form reset','info');
}

function deleteCurrentTeacher(){
  const idx=+document.getElementById('editTeacherIndex').value;
  if(idx>=0){
    document.getElementById('deleteModal').classList.add('show');
    document.getElementById('confirmDeleteBtn').onclick=()=>{
      teachers.splice(idx,1);
      renderTeachers(teachers);
      document.getElementById('deleteModal').classList.remove('show');
      closeTeacherModal();
      showToast('Teacher deleted successfully','success');
    };
    lucide.createIcons();
  }
}

function handleStudentSubmit(e){
  e.preventDefault();
  const idx=+document.getElementById('editIndex').value;
  const photoOption=document.querySelector('input[name="photoOption"]:checked')?.value||'capture';
  const s={
    id:document.getElementById('sId').value||'STU'+(String(Math.max(...students.map(st=>parseInt(st.id.slice(3))||0))+1).padStart(3,'0')),
    name:document.getElementById('sName').value,
    courseType:document.getElementById('sCourseType').value,
    department:document.getElementById('sDepartment').value,
    section:document.getElementById('sSection').value,
    batch:document.getElementById('sBatch').value,
    year:document.getElementById('sYear').value,
    semester:document.getElementById('sSemester').value,
    classRoll:document.getElementById('sClassRoll').value,
    universityRoll:document.getElementById('sUniversityRoll').value,
    gender:document.getElementById('sGender').value,
    dob:document.getElementById('sDOB').value,
    phone:document.getElementById('sPhone').value,
    email:document.getElementById('sEmail').value,
    photoOption:photoOption
  };
  if(idx>=0){students[idx]=s;showToast('Student updated successfully!','success')}else{students.push(s);showToast('Student added successfully!','success')}
  closeStudentModal();renderStudents(students);
}

function editStudent(i){
  const s=students[i];
  document.getElementById('editIndex').value=i;
  document.getElementById('sId').value=s.id;
  document.getElementById('sName').value=s.name;
  document.getElementById('sCourseType').value=s.courseType||'';
  document.getElementById('sDepartment').value=s.department||'';
  document.getElementById('sSection').value=s.section||'';
  document.getElementById('sBatch').value=s.batch||'';
  document.getElementById('sYear').value=s.year||'';
  document.getElementById('sSemester').value=s.semester||'';
  document.getElementById('sClassRoll').value=s.classRoll||'';
  document.getElementById('sUniversityRoll').value=s.universityRoll||'';
  document.getElementById('sGender').value=s.gender||'';
  document.getElementById('sDOB').value=s.dob||'';
  document.getElementById('sPhone').value=s.phone||'';
  document.getElementById('sEmail').value=s.email||'';
  if(s.photoOption==='skip')document.getElementById('photoSkip').checked=true;
  else document.getElementById('photoCapture').checked=true;
  document.getElementById('modalTitle').textContent='Edit Student';
  document.getElementById('submitStudentBtn').innerHTML='<i data-lucide="save" style="width:16px;height:16px"></i> Update Student';
  document.getElementById('deleteStudentBtn').style.display='inline-flex';
  document.getElementById('studentModal').classList.add('show');
  lucide.createIcons();
}

function deleteStudent(i){
  document.getElementById('deleteModal').classList.add('show');
  document.getElementById('confirmDeleteBtn').onclick=()=>{
    students.splice(i,1);renderStudents(students);
    document.getElementById('deleteModal').classList.remove('show');
    showToast('Student deleted successfully','success');
  };
  lucide.createIcons();
}

function closeStudentModal(){
  document.getElementById('studentModal').classList.remove('show');
  document.getElementById('studentForm').reset();
  document.getElementById('editIndex').value=-1;
  document.getElementById('modalTitle').textContent='Student Registration Form';
  document.getElementById('submitStudentBtn').innerHTML='<i data-lucide="save" style="width:16px;height:16px"></i> Save Student';
  document.getElementById('deleteStudentBtn').style.display='none';
  document.getElementById('photoCapture').checked=true;
}

// --- Attendance ---
function renderAttendance(list){
  document.getElementById('attendanceBody').innerHTML=list.map(a=>`<tr>
    <td style="font-weight:600">${a.id}</td><td>${a.name}</td><td>${a.course}</td><td>${a.date}</td><td>${a.time}</td>
    <td><span class="badge badge-${a.status.toLowerCase()}">${a.status}</span></td></tr>`).join('');
}

function filterAttendance(){
  const d=document.getElementById('dateFilter').value;
  const c=document.getElementById('attCourseFilter').value;
  const s=document.getElementById('statusFilter').value;
  renderAttendance(attendance.filter(a=>(!d||a.date===d)&&(!c||a.course===c)&&(!s||a.status===s)));
}

function exportCSV(){
  const hdr='ID,Name,Course,Date,Time,Status\n';
  const rows=attendance.map(a=>`${a.id},${a.name},${a.course},${a.date},${a.time},${a.status}`).join('\n');
  const blob=new Blob([hdr+rows],{type:'text/csv'});
  const url=URL.createObjectURL(blob);
  const link=document.createElement('a');link.href=url;link.download='attendance.csv';link.click();
  URL.revokeObjectURL(url);showToast('CSV exported!');
}

// --- Detection ---
const faceNames=['Arjun Patel','Priya Sharma','Sneha Gupta','Unknown'];
function startDetection(){
  isDetecting=true;
  document.getElementById('cameraPlaceholder').style.display='none';
  document.getElementById('cameraActive').style.display='block';
  document.getElementById('scanLine').style.display='block';
  document.getElementById('startDetBtn').disabled=true;
  document.getElementById('stopDetBtn').disabled=false;
  document.getElementById('detectionLog').innerHTML='';
  detectionInterval=setInterval(()=>{
    const n=faceNames[Math.floor(Math.random()*faceNames.length)];
    const isKnown=n!=='Unknown';
    const conf=(Math.random()*15+85).toFixed(1);
    const now=new Date().toLocaleTimeString();
    document.getElementById('detectionStatus').textContent=isKnown?`Recognized: ${n}`:'Scanning...';
    const log=document.getElementById('detectionLog');
    const entry=document.createElement('div');
    entry.style.cssText=`padding:10px;border-radius:8px;font-size:13px;background:${isKnown?'rgba(34,197,94,.1)':'rgba(239,68,68,.1)'};border:1px solid ${isKnown?'rgba(34,197,94,.2)':'rgba(239,68,68,.2)'}`;
    entry.innerHTML=`<div style="font-weight:600;color:${isKnown?'var(--accent2)':'#ef4444'}">${isKnown?'✓ '+n:'✗ Unknown Face'}</div><div style="color:var(--text2);font-size:11px;margin-top:2px">${now} • ${isKnown?conf+'% confidence':'Low confidence'}</div>`;
    log.prepend(entry);
    if(log.children.length>20)log.lastChild.remove();
  },2500);
}

function stopDetection(){
  isDetecting=false;clearInterval(detectionInterval);
  document.getElementById('cameraPlaceholder').style.display='block';
  document.getElementById('cameraActive').style.display='none';
  document.getElementById('scanLine').style.display='none';
  document.getElementById('startDetBtn').disabled=false;
  document.getElementById('stopDetBtn').disabled=true;
  showToast('Detection stopped','info');
}

// --- Train Model ---
function trainModel(){
  const btn=document.getElementById('trainBtn');
  btn.disabled=true;btn.innerHTML='<div class="spinner" style="width:16px;height:16px;border-width:2px"></div> Training...';
  const logs=document.getElementById('trainLogs');
  logs.innerHTML='<div style="color:var(--accent)">$ Starting training...</div>';
  const msgs=['Loading dataset...','Preprocessing 1,420 images...','Extracting face features...','Training LBPH model...','Validating accuracy...','Saving model to disk...','Training complete!'];
  let step=0,pct=0;
  const iv=setInterval(()=>{
    if(step<msgs.length){
      pct=Math.min(100,Math.round((step+1)/msgs.length*100));
      document.getElementById('trainProgress').style.width=pct+'%';
      document.getElementById('trainPercent').textContent=pct+'%';
      const d=document.createElement('div');
      d.style.color=step===msgs.length-1?'var(--accent2)':'var(--text2)';
      d.textContent='$ '+msgs[step];logs.appendChild(d);logs.scrollTop=logs.scrollHeight;
      step++;
    }else{
      clearInterval(iv);btn.disabled=false;
      btn.innerHTML='<i data-lucide="zap" style="width:16px;height:16px"></i> Start Training';
      lucide.createIcons();showToast('Model trained successfully! Accuracy: 98.2%','success');
    }
  },800);
}

// --- Dataset ---
function renderDataset(){
  const g=document.getElementById('photoGrid');
  const names=['Arjun','Priya','Rahul','Sneha','Amit','Neha','Vikram','Riya'];
  const colors=['#3b82f6','#22c55e','#a855f7','#ec4899','#f59e0b','#06b6d4','#6366f1','#ef4444'];
  g.innerHTML=names.flatMap((n,i)=>Array.from({length:3},(_,j)=>`
    <div class="photo-card">
      <div style="display:flex;flex-direction:column;align-items:center;gap:6px">
        <div style="width:50px;height:50px;border-radius:50%;background:${colors[i]};display:flex;align-items:center;justify-content:center;font-weight:700;color:#fff;font-size:18px">${n[0]}</div>
        <div style="font-size:11px;color:var(--text2)">${n}_${j+1}.jpg</div>
      </div>
    </div>`)).join('');
}

// --- Responsive detection grid ---
const style=document.createElement('style');
style.textContent=`@media(max-width:900px){.detection-grid,.train-grid{grid-template-columns:1fr!important}}`;
document.head.appendChild(style);

// --- Init ---
renderStudents(students);
renderTeachers(teachers);
renderAttendance(attendance);
renderDataset();
lucide.createIcons();

// Helper functions for form management
function resetStudentForm(){
  document.getElementById('studentForm').reset();
  document.getElementById('photoCapture').checked=true;
  document.getElementById('sId').value='';
  showToast('Form reset','info');
}

function deleteCurrentStudent(){
  const idx=+document.getElementById('editIndex').value;
  if(idx>=0){
    document.getElementById('deleteModal').classList.add('show');
    document.getElementById('confirmDeleteBtn').onclick=()=>{
      students.splice(idx,1);
      renderStudents(students);
      document.getElementById('deleteModal').classList.remove('show');
      closeStudentModal();
      showToast('Student deleted successfully','success');
    };
    lucide.createIcons();
  }
}
