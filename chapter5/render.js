const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+process.cwd()+'/chapter5.html');await p.waitForTimeout(500);
await p.pdf({path:'Chapter5_Week1_Pages32-35.pdf',width:'8.5in',height:'11in',printBackground:true,preferCSSPageSize:true});
await b.close()})();
