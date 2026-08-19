import os

from flask import Flask, render_template_string

app = Flask(__name__)

INDEX_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<meta name="theme-color" content="#07070b">
<title>For Madam Ji — A Little Piece of the Night ♡</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Inter:wght@300;400;500;600&family=Parisienne&display=swap" rel="stylesheet">
<style>
:root{
 --bg:#170d13; --bg2:#1c1017; --ink:#f7f3f5; --soft:#d9d1d6;
 --muted:#a99aa2; --line:rgba(255,255,255,.12);
 --glass:rgba(255,255,255,.055); --glass2:rgba(255,255,255,.085);
 --accent:#f6d3e0; --accent2:#fff;
}
*{box-sizing:border-box;-webkit-tap-highlight-color:transparent}
html,body{margin:0;width:100%;height:100%;height:100dvh;background:var(--bg);color:var(--ink);font-family:Inter,sans-serif;overscroll-behavior:none}
body{overflow:hidden}
button{font:inherit;touch-action:manipulation}
.option,.btn,.music-toggle,.dot,.flip-card,#blowBtn{touch-action:manipulation}
input,textarea{font-size:16px}
#scene{
 position:fixed;inset:0;overflow:hidden;
 background:
 radial-gradient(circle at 50% 42%,rgba(255,255,255,.065),transparent 28%),
 radial-gradient(circle at 12% 10%,rgba(245,218,231,.05),transparent 25%),
 radial-gradient(circle at 90% 85%,rgba(255,255,255,.035),transparent 30%),
 linear-gradient(145deg,#06060a,#0b0a10 50%,#050508);
}
#scene:before{
 content:"";position:absolute;inset:-20%;
 background:conic-gradient(from 180deg at 50% 50%,transparent,#fff1f6 8%,transparent 20%,transparent 72%,#fff 80%,transparent 90%);
 opacity:.025;filter:blur(45px);animation:aurora 18s linear infinite;
}
@keyframes aurora{to{transform:rotate(360deg)}}


.deep-space{
 position:absolute;inset:0;
 background:
 radial-gradient(ellipse at 55% 38%,rgba(255,190,215,.11),transparent 34%),
 radial-gradient(ellipse at 20% 82%,rgba(130,55,90,.20),transparent 38%),
 linear-gradient(180deg,#1c1017 0%,#221319 44%,#170d14 78%,#0e070c 100%);
}
.galaxy-cloud{
 position:absolute;width:155%;height:72%;left:-29%;top:2%;
 transform:rotate(-17deg);
 background:
 radial-gradient(ellipse at 47% 50%,rgba(255,192,216,.30) 0%,rgba(255,170,202,.17) 17%,rgba(150,80,115,.12) 33%,transparent 65%),
 radial-gradient(ellipse at 57% 55%,rgba(255,228,238,.18),transparent 35%),
 radial-gradient(ellipse at 35% 40%,rgba(255,165,190,.11),transparent 48%);
 filter:blur(16px);
 opacity:.95;
 animation:galaxyFloat 28s ease-in-out infinite alternate;
}
.galaxy-core{
 position:absolute;width:155%;height:48%;left:-30%;top:15%;
 transform:rotate(-17deg);
 background:
 radial-gradient(ellipse at 50% 50%,rgba(255,255,255,.68) 0%,rgba(255,232,241,.46) 6%,rgba(255,190,212,.24) 18%,rgba(200,110,140,.11) 34%,transparent 67%);
 filter:blur(7px);
 opacity:.85;
}
.galaxy-core:after{
 content:"";position:absolute;inset:10% 0;
 opacity:0;
}
.galaxy-dust{
 position:absolute;width:155%;height:50%;left:-30%;top:17%;
 transform:rotate(-17deg);
 background:
 radial-gradient(ellipse at 44% 50%,transparent 0 20%,rgba(45,16,26,.34) 21% 25%,transparent 26% 37%,rgba(38,13,22,.26) 38% 42%,transparent 43%);
 filter:blur(6px);
 opacity:.7;
}
@keyframes galaxyFloat{
 from{transform:rotate(-17deg) translate3d(-1%,0,0) scale(1)}
 to{transform:rotate(-17deg) translate3d(2%,1%,0) scale(1.04)}
}
.horizon-glow{
 position:absolute;left:-10%;right:-10%;bottom:5%;height:28%;
 background:
 radial-gradient(ellipse at 55% 100%,rgba(255,130,190,.28),transparent 35%),
 radial-gradient(ellipse at 48% 100%,rgba(225,120,165,.20),transparent 48%),
 linear-gradient(180deg,transparent 0%,rgba(40,18,28,.12) 55%,rgba(8,3,6,.50) 100%);
 filter:blur(13px);
 opacity:.8;
}
.horizon-silhouette{
 position:absolute;left:-5%;right:-5%;bottom:-5px;height:14%;
 background:#0c0509;
 clip-path:polygon(
  0 82%, 4% 76%, 7% 80%, 11% 69%, 15% 74%, 19% 63%,
  23% 70%, 27% 66%, 31% 73%, 36% 60%, 40% 68%, 44% 64%,
  48% 72%, 53% 58%, 57% 70%, 61% 65%, 66% 73%, 70% 62%,
  74% 69%, 78% 61%, 82% 70%, 87% 65%, 92% 76%, 96% 70%, 100% 77%,
  100% 100%,0 100%);
 box-shadow:0 -15px 35px rgba(0,0,0,.8);
}
.stars{
 position:absolute;inset:-10%;pointer-events:none;
 background-image:
 radial-gradient(circle,rgba(255,255,255,.96) 0 1px,transparent 1.5px),
 radial-gradient(circle,rgba(207,222,255,.72) 0 .7px,transparent 1.2px),
 radial-gradient(circle,rgba(255,255,255,.50) 0 .55px,transparent 1px);
 background-size:173px 173px,83px 83px,47px 47px;
 background-position:13px 22px,41px 7px,17px 29px;
}
.stars-a{opacity:.36;animation:starsMove 80s linear infinite}
.stars-b{opacity:.22;background-size:239px 239px,127px 127px,71px 71px;background-position:87px 43px,11px 72px,40px 16px;animation:starsMove 120s linear reverse infinite}
.stars-c{opacity:.16;background-size:61px 61px,151px 151px,97px 97px;background-position:23px 8px,70px 37px,12px 61px}
@keyframes starsMove{to{transform:translate3d(1.5%,1%,0)}}
.twinkles{position:absolute;inset:0;pointer-events:none}
.twinkles:before,.twinkles:after{
 content:"✦";position:absolute;color:rgba(255,255,255,.92);font-size:11px;
 text-shadow:0 0 12px white,0 0 22px rgba(150,190,255,.9);
 animation:twinkle 3.8s ease-in-out infinite;
}
.twinkles:before{left:22%;top:25%;animation-delay:-1.2s}
.twinkles:after{right:20%;top:61%;font-size:8px;animation-delay:-2.4s}
@keyframes twinkle{0%,100%{opacity:.15;transform:scale(.7)}50%{opacity:.98;transform:scale(1.35)}}
.moon{
 position:absolute;width:190px;height:190px;border-radius:50%;right:-62px;top:-60px;
 background:radial-gradient(circle at 34% 30%,#fff 0 7%,#eeeef2 22%,#aaaab4 64%,#676775 100%);
 box-shadow:0 0 80px rgba(235,235,255,.16),inset -18px -12px 35px rgba(0,0,0,.22);
 opacity:.20;
}
.moon:after{content:"";position:absolute;width:154px;height:154px;border-radius:50%;background:#0c0710;left:44px;top:-7px}

/* cherry blossom branches framing the corners */
.sakura-branch{position:absolute;top:-14px;width:260px;height:260px;pointer-events:none;z-index:1;filter:drop-shadow(0 12px 22px rgba(0,0,0,.4))}
.sakura-branch-left{left:-24px}
.sakura-branch-right{right:-24px;transform:scaleX(-1)}
@media(max-width:720px){.sakura-branch{width:190px;height:190px}}
@media(max-width:400px){.sakura-branch{width:150px;height:150px}}

#petals{position:fixed;inset:0;pointer-events:none;z-index:80;overflow:hidden}
.petal{
 position:absolute;top:-50px;left:0;font-size:var(--size);
 filter:drop-shadow(0 0 5px rgba(255,214,229,.4));
 opacity:0;animation:petalfall var(--duration) cubic-bezier(.35,.05,.55,1) var(--delay) infinite;
}
.petal.small{font-size:var(--size)}
@keyframes petalfall{
 0%{transform:translate3d(0,-50px,0) rotate(0deg);opacity:0}
 8%{opacity:var(--opacity)}
 45%{transform:translate3d(var(--x1),52vh,0) rotate(210deg)}
 100%{transform:translate3d(var(--x2),110vh,0) rotate(480deg);opacity:0}
}

#app{position:fixed;inset:0;z-index:10}
.page{
 position:absolute;inset:0;display:flex;align-items:center;justify-content:center;
 padding:calc(55px + env(safe-area-inset-top)) calc(24px + env(safe-area-inset-right)) calc(75px + env(safe-area-inset-bottom)) calc(24px + env(safe-area-inset-left));
 overflow-y:auto;overflow-x:hidden;-webkit-overflow-scrolling:touch;
 opacity:0;visibility:hidden;transform:translate3d(0,35px,0) scale(.985);
 transition:opacity 900ms cubic-bezier(.22,.8,.25,1),transform 1100ms cubic-bezier(.22,.8,.25,1),visibility 0s linear 1s;
 pointer-events:none;
}
.page.active{
 opacity:1;visibility:visible;transform:translate3d(0,0,0) scale(1);
 transition:opacity 900ms cubic-bezier(.22,.8,.25,1),transform 1100ms cubic-bezier(.22,.8,.25,1),visibility 0s;
 pointer-events:auto;
}
.page.active .content > *{
 animation:contentReveal .8s cubic-bezier(.22,.8,.25,1) backwards;
}
.page.active .eyebrow{animation-delay:.1s}
.page.active .display,.page.active .script{animation-delay:.2s}
.page.active .line{animation-delay:.3s}
.page.active .body,.page.active .quote{animation-delay:.4s}
.page.active .options,.page.active .flip-grid,.page.active .frame,.page.active .btn{animation-delay:.5s}
@keyframes contentReveal{
 from{opacity:0;transform:translate3d(0,12px,0)}
 to{opacity:1;transform:translate3d(0,0,0)}
}
.page.leaving{opacity:0;transform:translate3d(0,-35px,0) scale(1.01)}
.content{width:min(980px,94vw);position:relative;z-index:2}
.center{text-align:center}
.eyebrow{font-size:10px;letter-spacing:5px;text-transform:uppercase;color:#cfc5cb;margin-bottom:20px}
.kicker{font-size:12px;color:#a9a0a6;letter-spacing:2px}
.script{font-family:Parisienne,cursive;font-size:clamp(45px,7vw,78px);font-weight:400}
.display{font-family:"Cormorant Garamond",serif;font-size:clamp(52px,8vw,102px);font-weight:500;line-height:.9;letter-spacing:-2px}
.display em{font-style:italic;color:#fff}
.body{font-size:15px;line-height:1.9;color:var(--muted);font-weight:300}
.line{width:55px;height:1px;background:rgba(255,255,255,.5);margin:24px auto}
.btn{
 border:1px solid rgba(255,255,255,.25);background:linear-gradient(135deg,rgba(255,255,255,.12) 0%,rgba(255,255,255,.05) 100%);color:#fff;
 border-radius:999px;padding:14px 24px;cursor:pointer;transition:all .35s cubic-bezier(.22,.8,.25,1);
 backdrop-filter:blur(16px);letter-spacing:.3px;position:relative;overflow:hidden;
 box-shadow:0 8px 32px rgba(0,0,0,.1),inset 0 1px rgba(255,255,255,.2);
}
.btn:before{
 content:"";position:absolute;inset:0;background:linear-gradient(90deg,transparent,rgba(255,255,255,.3),transparent);
 transform:translateX(-100%);opacity:0;
}
.btn:hover{
 background:linear-gradient(135deg,rgba(255,255,255,.18) 0%,rgba(255,255,255,.08) 100%);
 border-color:rgba(255,255,255,.45);transform:translateY(-3px);box-shadow:0 16px 48px rgba(255,200,220,.15),inset 0 1px rgba(255,255,255,.3);
}
.btn:hover:before{
 animation:buttonShimmer .6s ease-in-out forwards;
}
@keyframes buttonShimmer{
 0%{transform:translateX(-100%);opacity:0}
 50%{opacity:1}
 100%{transform:translateX(100%);opacity:0}
}
.btn.primary{background:linear-gradient(135deg,#f8f2f5 0%,#fae8f0 100%);color:#171319;border-color:#fff;
 box-shadow:0 10px 40px rgba(248,242,245,.2),inset 0 1px rgba(255,255,255,.4);
}
.btn.primary:hover{
 background:linear-gradient(135deg,#fff 0%,#faf3f7 100%);
 box-shadow:0 16px 56px rgba(255,255,255,.25),inset 0 1px rgba(255,255,255,.5);
 transform:translateY(-4px);
}
.arrow{margin-left:9px}

/* opening */
.hero{min-height:550px;display:flex;align-items:center;justify-content:center;position:relative}
.hero-ring{
 position:absolute;width:min(560px,78vw);height:min(560px,78vw);border-radius:50%;
 border:2px solid rgba(255,255,255,.15);
 box-shadow:0 0 90px rgba(255,255,255,.08) inset,0 0 60px rgba(255,200,220,.1);
 animation:ringBreathe 6s ease-in-out infinite;
 background:radial-gradient(circle,rgba(255,255,255,.02),transparent 70%);
}
@keyframes ringBreathe{
 0%,100%{opacity:.7;transform:scale(1);box-shadow:0 0 90px rgba(255,255,255,.08) inset,0 0 60px rgba(255,200,220,.1)}
 50%{opacity:1;transform:scale(1.018);box-shadow:0 0 120px rgba(255,255,255,.12) inset,0 0 80px rgba(255,200,220,.15)}
}
.hero-ring:before,.hero-ring:after{
 content:"";position:absolute;border-radius:50%;border:1.5px solid rgba(255,255,255,.08);
 box-shadow:0 0 40px rgba(255,200,220,.08) inset;
}
.hero-ring:before{inset:34px;animation:ringFloat 8s ease-in-out infinite}
.hero-ring:after{inset:72px;animation:ringFloat 10s ease-in-out infinite reverse}
@keyframes ringFloat{
 0%,100%{opacity:.5;transform:scale(1)}
 50%{opacity:.8;transform:scale(1.08)}
}
.hero-copy{position:relative;z-index:2}
.hero-name{font-size:clamp(92px,15vw,175px);margin:0;text-shadow:0 0 40px rgba(255,200,220,.15)}
.hero-sub{max-width:570px;margin:25px auto;color:#bcb4ba;font-size:15px;line-height:1.9}
.typewrap{display:inline-block;position:relative}
.typewrap:after{content:"";display:inline-block;width:2px;height:.85em;background:currentColor;margin-left:4px;vertical-align:-.1em;animation:caret .85s step-end infinite}
.typewrap.done:after{display:none}
@keyframes caret{0%,49%{opacity:1}50%,100%{opacity:0}}

/* question */
.question-shell{
 background:linear-gradient(135deg,rgba(255,255,255,.095) 0%,rgba(255,255,255,.045) 100%);
 border:1px solid rgba(255,255,255,.2);border-radius:34px;padding:42px;
 box-shadow:0 35px 100px rgba(0,0,0,.35),inset 0 2px rgba(255,255,255,.12),inset 0 -1px rgba(0,0,0,.2);
 backdrop-filter:blur(28px);position:relative;overflow:hidden;
}
.question-shell:before{
 content:"";position:absolute;inset:0;border:1px solid rgba(255,255,255,.1);border-radius:34px;pointer-events:none;
 background:linear-gradient(135deg,rgba(255,200,220,.05),transparent 50%,rgba(200,150,180,.02));
}
.question-shell:after{
 content:"";position:absolute;top:-50%;right:-50%;width:300px;height:300px;border-radius:50%;
 background:radial-gradient(circle,rgba(255,255,255,.1),transparent 70%);opacity:0;pointer-events:none;
 transition:opacity .6s ease,transform .6s ease;transform:scale(0);
}
.question-shell:hover:after{
 opacity:.5;transform:scale(1);
}
.question{font-family:"Cormorant Garamond",serif;font-size:clamp(38px,6vw,66px);line-height:1.02;margin:0 auto 35px;max-width:850px;font-weight:500;position:relative;z-index:1}
.options{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.option{
 text-align:left;border:1px solid rgba(255,255,255,.1);background:rgba(255,255,255,.035);
 color:#e9e2e6;border-radius:19px;padding:17px 18px;cursor:pointer;transition:.35s;
}
.option:hover{background:rgba(255,255,255,.09);border-color:rgba(255,255,255,.25);transform:translateY(-2px)}
.option.selected{background:rgba(255,255,255,.12);border-color:rgba(255,255,255,.6);box-shadow:0 0 0 1px rgba(255,255,255,.06)}
.feedback{min-height:35px;color:#d8cbd1;font-family:"Cormorant Garamond",serif;font-size:25px;margin:22px 0 5px}
.next{display:none}.next.show{display:inline-flex}

/* story */
.story-grid{display:grid;grid-template-columns:1fr 1fr;gap:55px;align-items:center}
.story-number{font-family:"Cormorant Garamond";font-size:140px;line-height:.7;color:rgba(255,255,255,.055)}
.quote{
 font-family:"Cormorant Garamond",serif;font-size:clamp(28px,4vw,46px);line-height:1.18;
 font-style:italic;color:#eee6ea;margin:20px 0;
}
.quote-small{font-family:"Cormorant Garamond",serif;font-size:23px;line-height:1.55;color:#bdb2b9}

/* photo placeholder / portrait */
.frame{
 aspect-ratio:4/5;border-radius:220px 220px 35px 35px;
 border:1px solid rgba(255,255,255,.2);
 background:
 radial-gradient(circle at 50% 35%,rgba(255,255,255,.18),transparent 22%),
 linear-gradient(150deg,rgba(255,255,255,.12),rgba(255,255,255,.035)),
 rgba(0,0,0,.4);
 display:flex;align-items:flex-end;justify-content:center;overflow:hidden;
 box-shadow:0 30px 100px rgba(0,0,0,.35),inset 0 1px rgba(255,255,255,.15),0 0 60px rgba(255,200,220,.1);
 position:relative;transition:transform .4s cubic-bezier(.22,.8,.25,1),box-shadow .4s cubic-bezier(.22,.8,.25,1);
}
.frame:hover{
 transform:translateY(-8px) scale(1.02);
 box-shadow:0 40px 120px rgba(0,0,0,.4),inset 0 1px rgba(255,255,255,.2),0 0 80px rgba(255,200,220,.15);
}
.frame img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center top;transition:filter .4s ease}
.frame:hover img{filter:saturate(1.15) brightness(1.08)}
.frame-inner{display:none}
.frame-symbol{font-size:75px;opacity:.7;margin-bottom:10px}

/* spiritual */
.om{font-family:"Cormorant Garamond";font-size:100px;color:#f1e5eb;line-height:1;text-shadow:0 0 50px rgba(255,255,255,.1)}
.orbit{width:210px;height:210px;border:1px solid rgba(255,255,255,.12);border-radius:50%;margin:0 auto 25px;display:grid;place-items:center;position:relative}
.orbit:before,.orbit:after{content:"";position:absolute;border:1px solid rgba(255,255,255,.07);border-radius:50%}
.orbit:before{inset:20px}.orbit:after{inset:-13px}

/* architecture */
.architecture{
 border:1.5px solid rgba(255,255,255,.2);padding:45px;border-radius:32px;
 background:linear-gradient(135deg,rgba(255,255,255,.08) 0%,rgba(255,255,255,.03) 100%);
 box-shadow:0 30px 100px rgba(0,0,0,.25),inset 0 2px rgba(255,255,255,.12);
 backdrop-filter:blur(24px);position:relative;overflow:hidden;
}
.architecture:before{
 content:"";position:absolute;inset:0;border-radius:32px;
 background:radial-gradient(circle at 50% 0%,rgba(255,200,220,.08),transparent 60%);pointer-events:none;
}
.architecture > *{position:relative;z-index:1}
.blueprint{
 height:280px;border:1px solid rgba(255,255,255,.12);position:relative;overflow:hidden;
 background-image:linear-gradient(rgba(255,255,255,.08) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.08) 1px,transparent 1px);
 background-size:28px 28px;margin-top:25px;border-radius:16px;
 box-shadow:inset 0 2px 8px rgba(0,0,0,.2);
}
.blueprint:before{content:"";position:absolute;left:14%;top:18%;width:52%;height:58%;border:1px solid rgba(255,255,255,.48);transform:rotate(-3deg);box-shadow:0 0 20px rgba(255,200,220,.1) inset}
.blueprint:after{content:"⌂";position:absolute;left:52%;top:45%;transform:translate(-50%,-50%);font-family:"Cormorant Garamond";font-size:140px;color:rgba(255,255,255,.15)}

/* flip cards - reasons */
.flip-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:10px}
.flip-card{aspect-ratio:1/1;perspective:1200px;cursor:pointer;position:relative}
.flip-card:after{
 content:"";position:absolute;inset:0;border-radius:20px;opacity:0;
 background:radial-gradient(circle at var(--cx,50%) var(--cy,50%),rgba(255,255,255,.2),transparent 60%);
 transition:opacity .6s ease;pointer-events:none;
}
.flip-card:hover:after{opacity:.8}
.flip-inner{position:relative;width:100%;height:100%;transform-style:preserve-3d;transition:transform .7s cubic-bezier(.22,.8,.25,1)}
.flip-card.flipped .flip-inner{transform:rotateY(180deg)}
.flip-face{
 position:absolute;inset:0;backface-visibility:hidden;border-radius:20px;
 border:1.5px solid rgba(255,255,255,.2);display:flex;flex-direction:column;
 align-items:center;justify-content:center;padding:14px;text-align:center;
 box-shadow:0 15px 50px rgba(0,0,0,.25),inset 0 1px rgba(255,255,255,.1);
 transition:all .3s ease;
}
.flip-front{
 background:linear-gradient(135deg,rgba(255,255,255,.08) 0%,rgba(255,255,255,.03) 100%);
 backdrop-filter:blur(20px);
}
.flip-front:hover{background:linear-gradient(135deg,rgba(255,255,255,.12) 0%,rgba(255,255,255,.05) 100%)}
.flip-front .num{font-family:"Cormorant Garamond";font-size:40px;color:rgba(255,255,255,.65);text-shadow:0 0 20px rgba(255,200,220,.2)}
.flip-front .hint{font-size:9px;letter-spacing:2px;color:#8f858c;margin-top:8px;text-transform:uppercase}
.flip-back{
 background:linear-gradient(135deg,rgba(255,255,255,.12) 0%,rgba(255,255,255,.06) 100%);
 backdrop-filter:blur(24px);
 transform:rotateY(180deg);
}
.flip-back p{font-family:"Cormorant Garamond",serif;font-size:16px;line-height:1.35;color:#f1e9ed;margin:0}

/* candle */
.candle-wrap{display:flex;flex-direction:column;align-items:center;margin:20px auto 10px}
.candle{position:relative;width:26px;height:120px;border-radius:6px;
 background:linear-gradient(90deg,#efe6d8,#fff9ee 45%,#ddd0ba);
 box-shadow:0 20px 60px rgba(0,0,0,.4);
}
.wick{position:absolute;top:-14px;left:50%;transform:translateX(-50%);width:2px;height:14px;background:#3a332f}
.flame{
 position:absolute;top:-46px;left:50%;transform:translateX(-50%);
 width:20px;height:34px;border-radius:50% 50% 50% 50%/60% 60% 40% 40%;
 background:radial-gradient(circle at 50% 70%,#fff6d0 0%,#ffcf6b 35%,#ff9a3d 65%,#ff6a3d 100%);
 filter:blur(.3px);box-shadow:0 0 25px rgba(255,170,80,.65),0 0 55px rgba(255,140,60,.35);
 animation:flicker 1.6s ease-in-out infinite;transform-origin:bottom center;
 transition:opacity .6s ease,transform .6s ease;
}
@keyframes flicker{
 0%,100%{transform:translateX(-50%) scale(1) rotate(-1deg)}
 30%{transform:translateX(-50%) scale(1.06,.95) rotate(2deg)}
 60%{transform:translateX(-50%) scale(.94,1.05) rotate(-2deg)}
}
.flame.out{opacity:0;transform:translateX(-50%) scale(.2,.05);}
.smoke{position:absolute;top:-50px;left:50%;width:3px;height:0;background:rgba(255,255,255,.35);border-radius:3px;opacity:0}
.smoke.show{animation:smokeRise 1.8s ease-out forwards}
@keyframes smokeRise{0%{height:0;opacity:.5;transform:translateX(-50%)}100%{height:70px;opacity:0;transform:translateX(-70%) translateY(-40px)}}
.wish-reveal{max-height:0;overflow:hidden;opacity:0;transition:max-height .8s ease,opacity .8s ease}
.wish-reveal.show{max-height:200px;opacity:1;margin-top:22px}

/* night */
.night-card{max-width:800px;margin:auto;text-align:center}
.night-glow{width:230px;height:230px;border-radius:50%;margin:0 auto 30px;background:radial-gradient(circle,#fff 0,rgba(255,255,255,.18) 4%,transparent 65%);opacity:.18}
.stars-note{font-size:12px;letter-spacing:3px;color:#aaa1a8}

/* final */
.final-card{text-align:center;position:relative}
.final-card:before{
 content:"";position:absolute;inset:-40%;background:radial-gradient(circle,rgba(255,200,220,.15),transparent 60%);
 filter:blur(40px);pointer-events:none;animation:finalGlow 6s ease-in-out infinite;
}
@keyframes finalGlow{
 0%,100%{opacity:.4;transform:scale(1)}
 50%{opacity:.7;transform:scale(1.1)}
}
.final-name{
 font-family:"Cormorant Garamond";font-size:clamp(72px,13vw,155px);line-height:.78;margin:12px 0 25px;font-weight:500;
 position:relative;z-index:1;text-shadow:0 0 50px rgba(255,200,220,.2);
}
.final-name:after{
 content:"";position:absolute;bottom:-12px;left:50%;transform:translateX(-50%);width:80%;height:2px;
 background:linear-gradient(90deg,transparent,rgba(255,255,255,.5),transparent);
 box-shadow:0 0 20px rgba(255,200,220,.3);
}
.final-message{max-width:720px;margin:auto;font-family:"Cormorant Garamond";font-size:28px;line-height:1.45;color:#d7cdd2;position:relative;z-index:1}
.signature{font-family:Parisienne;font-size:48px;margin-top:35px;color:#eee5e9;position:relative;z-index:1}

/* progress */
.progress{position:fixed;bottom:calc(22px + env(safe-area-inset-bottom));left:50%;transform:translateX(-50%);z-index:100;display:flex;gap:7px;padding:9px 13px;border:1px solid rgba(255,255,255,.1);border-radius:999px;background:rgba(10,9,13,.55);backdrop-filter:blur(14px);max-width:92vw;overflow-x:auto;-webkit-overflow-scrolling:touch}
.dot{flex:none}
.dot{width:6px;height:6px;border-radius:50%;background:#6d666c;cursor:pointer;transition:.3s}.dot.active{width:20px;border-radius:8px;background:#f5edf1}
.hint{font-size:10px;color:#817980;letter-spacing:2px;margin-top:20px}

/* music toggle */
.music-toggle{
 position:fixed;top:calc(20px + env(safe-area-inset-top));right:calc(20px + env(safe-area-inset-right));z-index:100;width:44px;height:44px;border-radius:50%;
 border:1px solid rgba(255,255,255,.15);background:rgba(10,9,13,.55);backdrop-filter:blur(14px);
 color:#f2ecef;display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:16px;
 transition:.3s;
}
.music-toggle:hover{background:rgba(255,255,255,.12);transform:scale(1.06)}
.music-toggle.hidden{display:none}
.music-toggle .bars{display:flex;gap:2px;align-items:flex-end;height:14px}
.music-toggle .bars span{width:2.5px;background:#f2ecef;border-radius:2px;animation:bar 1s ease-in-out infinite}
.music-toggle .bars span:nth-child(1){height:6px;animation-delay:0s}
.music-toggle .bars span:nth-child(2){height:13px;animation-delay:.2s}
.music-toggle .bars span:nth-child(3){height:9px;animation-delay:.4s}
.music-toggle.paused .bars span{animation-play-state:paused;height:4px}
@keyframes bar{0%,100%{height:4px}50%{height:14px}}

/* film grain */
#grain{
 position:fixed;inset:-100%;z-index:90;pointer-events:none;opacity:.035;mix-blend-mode:overlay;
 background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2' stitchTiles='stitch'/></filter><rect width='100%25' height='100%25' filter='url(%23n)'/></svg>");
 animation:grainShift 1.4s steps(2) infinite;
}
@keyframes grainShift{0%{transform:translate(0,0)}50%{transform:translate(-1.5%,1%)}100%{transform:translate(1%,-1.5%)}}

/* cursor glow (desktop only) */
#cursorGlow{
 position:fixed;top:0;left:0;width:340px;height:340px;border-radius:50%;z-index:5;pointer-events:none;
 background:radial-gradient(circle,rgba(255,255,255,.05),rgba(200,190,255,.025) 40%,transparent 70%);
 transform:translate3d(-50%,-50%,0);will-change:transform;opacity:0;transition:opacity .5s ease;
}
#cursorGlow.on{opacity:1}

/* sparkle trail dot */
.spark-trail{position:fixed;z-index:6;pointer-events:none;border-radius:50%;background:#fff;
 box-shadow:0 0 8px 2px rgba(255,255,255,.7);opacity:.8;animation:sparkFade .9s ease-out forwards}
@keyframes sparkFade{to{opacity:0;transform:translate(var(--sx),var(--sy)) scale(.2)}}

/* bokeh orbs */
.bokeh{position:absolute;border-radius:50%;pointer-events:none;filter:blur(2px);
 background:radial-gradient(circle,rgba(255,226,236,.55),rgba(255,255,255,0) 70%);
 animation:bokehDrift linear infinite;opacity:0}
@keyframes bokehDrift{
 0%{opacity:0;transform:translate3d(0,0,0)}
 8%{opacity:var(--bo,.35)}
 92%{opacity:var(--bo,.35)}
 100%{opacity:0;transform:translate3d(var(--bx,40px),var(--by,-220px),0)}
}

/* shimmer text */
.shimmer{
 background:linear-gradient(100deg,#fff 0%,#fff 38%,#8f8792 46%,#fff 54%,#fff 100%);
 background-size:260% 100%;background-position:130% 0;
 -webkit-background-clip:text;background-clip:text;color:transparent;
 animation:shimmerSweep 5.5s ease-in-out infinite;
}
@keyframes shimmerSweep{0%{background-position:150% 0}45%,100%{background-position:-40% 0}}

/* blur-to-focus content reveal */
.content{filter:blur(9px);transition:filter 1000ms cubic-bezier(.22,.8,.25,1)}
.page.active .content{filter:blur(0)}

/* PREMIUM ACCESSIBILITY: respect prefers-reduced-motion */
@media(prefers-reduced-motion:reduce){
 *{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important}
 .hero-ring,.hero-ring:before,.hero-ring:after{animation:none!important}
 .bokeh{animation:none!important}
 .petal{animation:none!important;display:none}
 .stars-a,.stars-b{animation:none!important}
 .twinkles:before,.twinkles:after{animation:none!important}
 .flip-inner{transition:none}
 .btn{transition:none}
 .page{transition:none}
 #cursorGlow{display:none}
}

/* fireworks */
.fw-particle{position:fixed;z-index:85;left:0;top:0;width:5px;height:5px;border-radius:50%;pointer-events:none;
 will-change:transform,opacity;animation:fwFly var(--fwd,1.3s) cubic-bezier(.15,.6,.35,1) forwards}
@keyframes fwFly{
 0%{transform:translate3d(0,0,0) scale(1);opacity:1}
 70%{opacity:1}
 100%{transform:translate3d(var(--fx),var(--fy),0) scale(.3);opacity:0}
}

@media(max-width:720px){
 .page{padding:calc(65px + env(safe-area-inset-top)) calc(16px + env(safe-area-inset-right)) calc(75px + env(safe-area-inset-bottom)) calc(16px + env(safe-area-inset-left))}
 .options,.story-grid{grid-template-columns:1fr}
 .question-shell{padding:25px 18px;border-radius:25px}.story-grid{gap:25px}
 .story-number{display:none}.architecture{padding:25px}
 .flip-grid{grid-template-columns:repeat(2,1fr)}
 .music-toggle{top:calc(14px + env(safe-area-inset-top));right:calc(14px + env(safe-area-inset-right))}
 .blueprint{height:210px}
}

/* extra-small phones (iPhone SE, small Android) */
@media(max-width:400px){
 .hero-name{font-size:clamp(58px,17vw,92px)}
 .display{font-size:clamp(38px,9vw,52px)}
 .final-name{font-size:clamp(48px,14vw,72px)}
 .question{font-size:clamp(28px,7vw,38px)}
 .om{font-size:64px}
 .orbit{width:170px;height:170px}
 .flip-grid{grid-template-columns:repeat(2,1fr);gap:10px}
 .flip-front .num{font-size:30px}
 .flip-back p{font-size:14px}
 .btn{padding:13px 20px;font-size:14px}
 .candle{width:22px;height:100px}
 .hero-ring{display:none}
 .quote{font-size:clamp(22px,6.5vw,30px)}
}

/* short viewports (landscape phones) */
@media(max-height:480px) and (orientation:landscape){
 .page{padding-top:24px;padding-bottom:56px}
 .hero{min-height:0}
 .hero-name{font-size:clamp(48px,10vw,90px)}
 .progress{bottom:8px}
 .music-toggle{top:8px;right:8px;width:38px;height:38px}
}
</style>
</head>
<body>
<div id="scene">
      <div class="deep-space"></div>
      <div class="galaxy-cloud"></div>
      <div class="galaxy-core"></div>
      <div class="galaxy-dust"></div>
      <div class="horizon-glow"></div>
      <div class="horizon-silhouette"></div>
      <div class="stars stars-a"></div>
      <div class="stars stars-b"></div>
      <div class="stars stars-c"></div>
      <div class="twinkles"></div>
      <div class="moon"></div>
      <svg class="sakura-branch sakura-branch-left" viewBox="0 0 320 320" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
       <defs>
        <radialGradient id="blossomPink" cx="35%" cy="30%" r="75%">
         <stop offset="0%" stop-color="#fff6f9"/>
         <stop offset="55%" stop-color="#f6c6d8"/>
         <stop offset="100%" stop-color="#e295b8"/>
        </radialGradient>
        <radialGradient id="blossomWhite" cx="35%" cy="30%" r="75%">
         <stop offset="0%" stop-color="#ffffff"/>
         <stop offset="60%" stop-color="#fbeaf1"/>
         <stop offset="100%" stop-color="#eccfdd"/>
        </radialGradient>
       </defs>
       <g stroke="#2b1a20" stroke-linecap="round" fill="none" opacity=".9">
        <path d="M-10,-10 C40,10 70,55 95,100 C115,135 130,150 165,158" stroke-width="7"/>
        <path d="M95,100 C120,95 150,80 185,70" stroke-width="4"/>
        <path d="M120,128 C150,140 175,132 205,118" stroke-width="3.5"/>
        <path d="M165,158 C185,175 205,178 232,168" stroke-width="3"/>
       </g>
       <g fill="url(#blossomPink)">
        <circle cx="185" cy="70" r="11"/><circle cx="200" cy="62" r="8"/>
        <circle cx="205" cy="118" r="10"/><circle cx="222" cy="112" r="7"/>
        <circle cx="232" cy="168" r="10"/><circle cx="248" cy="160" r="7"/>
        <circle cx="60" cy="35" r="9"/><circle cx="30" cy="15" r="7"/>
       </g>
       <g fill="url(#blossomWhite)">
        <circle cx="193" cy="80" r="7"/><circle cx="212" cy="108" r="6"/>
        <circle cx="240" cy="150" r="6"/><circle cx="45" cy="25" r="6"/>
        <circle cx="130" cy="95" r="5"/>
       </g>
      </svg>
      <svg class="sakura-branch sakura-branch-right" viewBox="0 0 320 320" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
       <g stroke="#2b1a20" stroke-linecap="round" fill="none" opacity=".9">
        <path d="M-10,-10 C40,10 70,55 95,100 C115,135 130,150 165,158" stroke-width="7"/>
        <path d="M95,100 C120,95 150,80 185,70" stroke-width="4"/>
        <path d="M120,128 C150,140 175,132 205,118" stroke-width="3.5"/>
        <path d="M165,158 C185,175 205,178 232,168" stroke-width="3"/>
       </g>
       <g fill="url(#blossomPink)">
        <circle cx="185" cy="70" r="11"/><circle cx="200" cy="62" r="8"/>
        <circle cx="205" cy="118" r="10"/><circle cx="222" cy="112" r="7"/>
        <circle cx="232" cy="168" r="10"/><circle cx="248" cy="160" r="7"/>
        <circle cx="60" cy="35" r="9"/><circle cx="30" cy="15" r="7"/>
       </g>
       <g fill="url(#blossomWhite)">
        <circle cx="193" cy="80" r="7"/><circle cx="212" cy="108" r="6"/>
        <circle cx="240" cy="150" r="6"/><circle cx="45" cy="25" r="6"/>
        <circle cx="130" cy="95" r="5"/>
       </g>
      </svg>
      <div id="bokehLayer"></div>
    </div>
<div id="grain"></div>
<div id="cursorGlow"></div>
<div id="petals"></div>

<button class="music-toggle hidden" id="musicToggle" onclick="toggleMusic()" title="Play background music">
  <div class="bars"><span></span><span></span><span></span></div>
</button>
<audio id="bgMusic" loop preload="none">
  <source src="{{ url_for('static', filename='music/bg-music.mp3') }}" type="audio/mpeg">
</audio>

<main id="app">

<section class="page active" id="p0">
<div class="content hero center">
 <div class="hero-ring"></div>
 <div class="hero-copy">
  <div class="eyebrow">WELCOME, TO A LITTLE PIECE OF THE NIGHT</div>
  <div class="script"><span class="typewrap" id="typeHey"></span></div>
  <h1 class="display hero-name shimmer">Madam Ji</h1>
  <div class="line"></div>
  <p class="hero-sub">I made this little corner of the sky just for you.<br>Take your time, wander through it, and see where it takes you.</p>
  <button class="btn primary" onclick="go(1)">Begin <span class="arrow">→</span></button>
  <div class="hint">TAKE YOUR TIME • THERE'S NO RUSH</div>
 </div>
</div>
</section>

<section class="page" id="p1">
<div class="content">
 <div class="eyebrow center">QUESTION 01</div>
 <div class="question-shell center">
  <div class="question">Who can turn a five-minute conversation into a two-hour conversation?</div>
  <div class="options">
   <button class="option" onclick="answer(this,'Correct. We both know the answer. 😄')">🗣️ &nbsp; Madam Ji, obviously</button>
   <button class="option" onclick="answer(this,'Nice try... but she wins this one. 😂')">🤫 &nbsp; The quiet one</button>
   <button class="option" onclick="answer(this,'Technically possible. Emotionally impossible. 😌')">⏰ &nbsp; Time itself</button>
   <button class="option" onclick="answer(this,'There is only one correct answer here. 🌸')">✦ &nbsp; The girl who has stories for everything</button>
  </div>
  <div class="feedback" id="f1"></div>
  <button class="btn primary next" onclick="go(2)">Next question →</button>
 </div>
</div>
</section>

<section class="page" id="p2">
<div class="content">
 <div class="eyebrow center">QUESTION 02</div>
 <div class="question-shell center">
  <div class="question">What makes Madam Ji impossible not to like?</div>
  <div class="options">
   <button class="option" onclick="answer(this,'Yes. Definitely. ♡')">♡ &nbsp; Her lovable nature</button>
   <button class="option" onclick="answer(this,'Absolutely. Especially when she starts talking. 😄')">✦ &nbsp; Her energy</button>
   <button class="option" onclick="answer(this,'Correct — and probably more than she realizes. ✨')">☾ &nbsp; Her heart</button>
   <button class="option" onclick="answer(this,'Trick question. It is all of the above. 😊')">∞ &nbsp; All of the above</button>
  </div>
  <div class="feedback" id="f2"></div>
  <button class="btn primary next" onclick="go(3)">Continue →</button>
 </div>
</div>
</section>

<section class="page" id="p3">
<div class="content">
 <div class="eyebrow center">QUESTION 03</div>
 <div class="question-shell center">
  <div class="question">What's the fastest way to make Madam Ji laugh?</div>
  <div class="options">
   <button class="option" onclick="answer(this,'Works every single time. 😂')">🎭 &nbsp; Say something ridiculous</button>
   <button class="option" onclick="answer(this,'Instant nostalgia, instant laughter. 🥹')">📖 &nbsp; Bring up an old memory</button>
   <button class="option" onclick="answer(this,'Honestly, this might be the real answer. 😄')">🌟 &nbsp; Just exist near her</button>
   <button class="option" onclick="answer(this,'A close second. She pretends to hate them. 😏')">🥁 &nbsp; Tell a terrible pun</button>
  </div>
  <div class="feedback" id="f3"></div>
  <button class="btn primary next" onclick="go(4)">One more →</button>
 </div>
</div>
</section>

<section class="page" id="p4">
<div class="content">
 <div class="eyebrow center">QUESTION 04</div>
 <div class="question-shell center">
  <div class="question">If Madam Ji's life had a soundtrack, what would play during the good chapters?</div>
  <div class="options">
   <button class="option" onclick="answer(this,'Loud, joyful, and a little chaotic. Very her. 🎉')">🔊 &nbsp; Something loud and joyful</button>
   <button class="option" onclick="answer(this,'Soft and warm, like the version of her few people see. ☾')">🎧 &nbsp; Something soft and warm</button>
   <button class="option" onclick="answer(this,'Unpredictable in the best way. 😄')">🔀 &nbsp; Whatever is stuck in her head that day</button>
   <button class="option" onclick="answer(this,'Obviously. On shuffle, always. ∞')">🎶 &nbsp; All of the above, on shuffle</button>
  </div>
  <div class="feedback" id="f4"></div>
  <button class="btn primary next" onclick="go(5)">Continue →</button>
 </div>
</div>
</section>

<section class="page" id="p5">
<div class="content story-grid">
 <div><div class="story-number">05</div><div class="eyebrow">THE GIRL BEHIND THE SMILE</div>
  <div class="quote">"There is more to Madam Ji than meets the eye."</div>
  <p class="body">She talks enough to make silence disappear, has a laugh and energy that fill a conversation, wears her specs like they belong there, and creates spaces for a living.</p>
 </div>
 <div class="frame">
  <img src="{{ url_for('static', filename='photos/memory1.jpg') }}" alt="Madam Ji" onerror="this.style.display='none'">
 </div>
 </div>
 <div class="center" style="margin-top:35px"><button class="btn primary" onclick="go(6)">There is something deeper →</button></div>
</div>
</section>

<section class="page" id="p6">
<div class="content center">
 <div class="eyebrow">06 • HER FAITH</div>
 <div class="orbit"><div class="om">ॐ</div></div>
 <div class="display" style="font-size:clamp(45px,7vw,82px)">The girl who keeps<br><em>Mahadev</em> close.</div>
 <div class="line"></div>
 <p class="quote-small">"May Mahadev always guide your steps, protect your peace, and give you the strength to walk toward everything that is meant for you."</p>
 <p class="body" style="max-width:700px;margin:20px auto">May your faith remain your quiet strength. May you find peace when the world gets loud, courage when things feel uncertain, and grace in every new beginning.</p>
 <button class="btn primary" onclick="go(7)">Keep going →</button>
</div>
</section>

<section class="page" id="p7">
<div class="content">
 <div class="architecture">
  <div class="eyebrow">07 • THE ARCHITECT</div>
  <div class="display">You design spaces.<br><em>But...</em></div>
  <p class="quote-small" style="max-width:700px">I think the nicest thing you build isn't made of concrete, glass or drawings.</p>
  <div class="blueprint"></div>
  <div style="max-width:700px;margin:25px auto 0">
   <p class="body">You build feelings too — the comfort in a late-night conversation, the laughter in a random story, and that strange little feeling that people can simply be themselves around you.</p>
   <p class="quote-small">Maybe architecture is about creating places people want to stay. In your own way, you do that with people too.</p>
  </div>
  <div class="center"><button class="btn primary" onclick="go(8)">A few reasons why →</button></div>
 </div>
</div>
</section>

<section class="page" id="p8">
<div class="content">
 <div class="eyebrow center">08 • A FEW REASONS</div>
 <div class="display center" style="font-size:clamp(36px,6vw,62px);margin-bottom:8px">Tap each one.</div>
 <p class="body center" style="max-width:600px;margin:0 auto 25px">Small, true things about Madam Ji.</p>
 <div class="flip-grid" id="flipGrid">
  <div class="flip-card" onclick="this.classList.toggle('flipped')">
   <div class="flip-inner">
    <div class="flip-face flip-front"><div class="num">01</div><div class="hint">tap to reveal</div></div>
    <div class="flip-face flip-back"><p>You make people feel like they've known you for years, even on day one.</p></div>
   </div>
  </div>
  <div class="flip-card" onclick="this.classList.toggle('flipped')">
   <div class="flip-inner">
    <div class="flip-face flip-front"><div class="num">02</div><div class="hint">tap to reveal</div></div>
    <div class="flip-face flip-back"><p>Your laugh is loud enough to make a whole room smile without meaning to.</p></div>
   </div>
  </div>
  <div class="flip-card" onclick="this.classList.toggle('flipped')">
   <div class="flip-inner">
    <div class="flip-face flip-front"><div class="num">03</div><div class="hint">tap to reveal</div></div>
    <div class="flip-face flip-back"><p>You notice the small things about people that most others walk right past.</p></div>
   </div>
  </div>
  <div class="flip-card" onclick="this.classList.toggle('flipped')">
   <div class="flip-inner">
    <div class="flip-face flip-front"><div class="num">04</div><div class="hint">tap to reveal</div></div>
    <div class="flip-face flip-back"><p>You hold onto your faith quietly, without ever making it loud or performative.</p></div>
   </div>
  </div>
  <div class="flip-card" onclick="this.classList.toggle('flipped')">
   <div class="flip-inner">
    <div class="flip-face flip-front"><div class="num">05</div><div class="hint">tap to reveal</div></div>
    <div class="flip-face flip-back"><p>You build things — spaces, conversations, comfort — and somehow make it look easy.</p></div>
   </div>
  </div>
  <div class="flip-card" onclick="this.classList.toggle('flipped')">
   <div class="flip-inner">
    <div class="flip-face flip-front"><div class="num">06</div><div class="hint">tap to reveal</div></div>
    <div class="flip-face flip-back"><p>Underneath all the talking, there's a version of you that's quiet, thoughtful, and just as worth knowing.</p></div>
   </div>
  </div>
 </div>
 <div class="center" style="margin-top:30px"><button class="btn primary" onclick="go(9)">After midnight →</button></div>
</div>
</section>

<section class="page" id="p9">
<div class="content night-card">
 <div class="night-glow"></div>
 <div class="stars-note">09 • AFTER MIDNIGHT</div>
 <div class="quote" style="font-size:clamp(35px,5vw,62px)">"Some conversations happen late at night because that's when people stop performing and simply become themselves."</div>
 <p class="body">Somewhere between the random stories, the long talks and the little things you shared, I got the feeling that there is a quieter, deeper Madam Ji underneath the very talkative one.</p>
 <p class="quote-small" style="color:#e3d9de">And honestly?<br>I think that version of you is beautiful too. ♡</p>
 <button class="btn primary" onclick="go(10)">Make a wish →</button>
</div>
</section>

<section class="page" id="p10">
<div class="content center">
 <div class="eyebrow">10 • MAKE A WISH</div>
 <div class="display" style="font-size:clamp(38px,6vw,64px)">One candle.<br>One wish.</div>
 <div class="candle-wrap">
  <div class="smoke" id="smoke"></div>
  <div class="flame" id="flame"></div>
  <div class="candle"><div class="wick"></div></div>
 </div>
 <button class="btn primary" id="blowBtn" onclick="blowCandle()">Blow out the candle 🕯️</button>
 <div class="wish-reveal" id="wishReveal">
  <p class="quote-small" style="max-width:600px;margin:0 auto">Whatever you wished for — I hope it finds its way to you this year. And if it doesn't come on its own, I hope you go and build it yourself. You're good at building things.</p>
 </div>
 <div class="center" style="margin-top:35px"><button class="btn" onclick="go(11)">Last page →</button></div>
</div>
</section>

<section class="page" id="p11">
<div class="content center final-card">
 <div class="eyebrow">11 • THE FINAL CHAPTER</div>
 <div class="script">Happy Birthday,</div>
 <div class="final-name shimmer">Madam Ji</div>
 <div class="line"></div>
 <p class="final-message">May this year bring you more peace, more laughter, more people who understand your heart, more reasons to smile — and a life that feels as beautiful as the one you keep imagining.</p>
 <div class="signature">Keep being you. ♡</div>

 <button class="btn primary" style="margin-top:25px" onclick="celebrate()">A little birthday surprise ✦</button>
 <div style="margin-top:18px"><button class="btn" onclick="go(12)">Continue →</button></div>
</div>
</section>

<section class="page" id="p12">
<div class="content center">
 <div class="eyebrow">12 • BEFORE YOU GO</div>
 <div class="orbit" style="width:150px;height:150px;margin-bottom:20px"><span style="font-size:34px">♡</span></div>
 <div class="display" style="font-size:clamp(40px,6.5vw,72px)">Thank you for<br><em>reading till the end.</em></div>
 <div class="line"></div>
 <p class="body" style="max-width:600px;margin:0 auto">This took a little time to put together, but every part of it meant something — because it was for you. I hope some part of it made you smile.</p>
 <p class="quote-small" style="margin-top:20px">See you soon, Madam Ji. ♡</p>
 <button class="btn" style="margin-top:25px" onclick="go(0)">Watch it again ↺</button>
</div>
</section>

</main>

<div class="progress" id="progress"></div>

<script>
const pages=[...document.querySelectorAll('.page')];
const progress=document.getElementById('progress');
let current=0,locked=false;
const FINAL_PAGE=pages.length-1;

pages.forEach((_,i)=>{
 const d=document.createElement('span');
 d.className='dot'+(i===0?' active':'');
 d.onclick=()=>{if(i<=current+1)go(i)};
 progress.appendChild(d);
});
const dots=[...document.querySelectorAll('.dot')];

function go(n){
 if(n===current || locked) return;
 locked=true;
 const old=pages[current], next=pages[n];
 old.classList.add('leaving');
 next.classList.add('active');
 dots.forEach((d,i)=>d.classList.toggle('active',i===n));
 current=n;
 next.scrollTop=0;
 setTimeout(()=>{old.classList.remove('active','leaving');locked=false},1050);
 if(n===FINAL_PAGE)burst(80);
}

function answer(btn,msg){
 const page=btn.closest('.page');
 page.querySelectorAll('.option').forEach(x=>x.classList.remove('selected'));
 btn.classList.add('selected');
 const feedback=page.querySelector('.feedback');
 feedback.textContent=msg;
 const next=page.querySelector('.next');
 next.classList.add('show');
 chime(660);
 setTimeout(()=>next.scrollIntoView({behavior:'smooth',block:'center'}),120);
}

/* lighten decorative animation load on phones (smaller screens / no fine pointer) */
const isMobile=window.matchMedia('(max-width:720px), (hover:none)').matches;

const PETAL_COLORS=['#ffffff','#ffe4ee','#ffd3e3','#f9c2d7'];
function makePetal(initial=false){
 const p=document.createElement('div');
 p.className='petal';
 p.textContent=Math.random()>.38?'✿':'❀';
 p.style.color=PETAL_COLORS[Math.floor(Math.random()*PETAL_COLORS.length)];
 p.style.setProperty('--size',(10+Math.random()*16)+'px');
 p.style.setProperty('--x1',(-130+Math.random()*260)+'px');
 p.style.setProperty('--x2',(-220+Math.random()*440)+'px');
 p.style.setProperty('--duration',(5.5+Math.random()*7)+'s');
 p.style.setProperty('--delay',(Math.random()*6)+'s');
 p.style.setProperty('--opacity',(0.45+Math.random()*.45).toFixed(2));
 p.style.left=(Math.random()*100)+'vw';
 if(initial)p.style.animationDelay=(-Math.random()*8)+'s';
 document.getElementById('petals').appendChild(p);
 setTimeout(()=>p.remove(),15000);
}
for(let i=0;i<(isMobile?24:45);i++)makePetal(true);
function shootingStar(){
 const s=document.createElement('div');
 s.style.cssText=`position:fixed;z-index:2;pointer-events:none;width:${70+Math.random()*90}px;height:1px;
 left:${10+Math.random()*70}vw;top:${5+Math.random()*45}vh;
 background:linear-gradient(90deg,transparent,rgba(255,255,255,.85));
 transform:rotate(${18+Math.random()*18}deg);filter:blur(.3px);
 opacity:0;transition:transform 1.1s linear,opacity .25s ease`;
 document.body.appendChild(s);
 requestAnimationFrame(()=>{s.style.opacity='.75';s.style.transform+=' translate(170px,90px)'});
 setTimeout(()=>{s.style.opacity='0'},850);
 setTimeout(()=>s.remove(),1300);
}
setInterval(()=>{if(Math.random()<.72)shootingStar()},isMobile?7800:5200);

setInterval(()=>makePetal(false),isMobile?600:360);

/* ---- bokeh floating light orbs ---- */
const bokehLayer=document.getElementById('bokehLayer');
function makeBokeh(){
 const b=document.createElement('div');
 const size=18+Math.random()*70;
 b.className='bokeh';
 b.style.width=size+'px';b.style.height=size+'px';
 b.style.left=(Math.random()*100)+'%';
 b.style.top=(40+Math.random()*60)+'%';
 b.style.setProperty('--bx',(Math.random()*160-80)+'px');
 b.style.setProperty('--by',(-(280+Math.random()*260))+'px');
 b.style.setProperty('--bo',(0.12+Math.random()*.28).toFixed(2));
 b.style.animationDuration=(14+Math.random()*16)+'s';
 bokehLayer.appendChild(b);
 setTimeout(()=>b.remove(),32000);
}
for(let i=0;i<(isMobile?5:10);i++)setTimeout(makeBokeh,i*900);
setInterval(makeBokeh,isMobile?4200:2600);

/* ---- PREMIUM UI UPGRADE: 3D Tilt Effect + Card Spotlight ---- */
const canHover=window.matchMedia('(hover:hover) and (pointer:fine)').matches;
const prefersReducedMotion=window.matchMedia('(prefers-reduced-motion:reduce)').matches;

if(canHover && !prefersReducedMotion){
 /* 3D tilt effect for premium cards */
 const cardElements=[...document.querySelectorAll('.question-shell, .flip-card, .frame, .architecture')];
 cardElements.forEach(card=>{
  card.addEventListener('mousemove',e=>{
   if(card.classList.contains('flip-card')){
    /* update spotlight for flip cards */
    const rect=card.getBoundingClientRect();
    const x=(e.clientX-rect.left)/rect.width*100;
    const y=(e.clientY-rect.top)/rect.height*100;
    card.style.setProperty('--cx',x+'%');
    card.style.setProperty('--cy',y+'%');
    return; /* skip tilt for flip cards */
   }
   
   const rect=card.getBoundingClientRect();
   const centerX=rect.left+rect.width/2;
   const centerY=rect.top+rect.height/2;
   const rotateX=(e.clientY-centerY)/rect.height*4;
   const rotateY=-(e.clientX-centerX)/rect.width*4;
   card.style.transform=`perspective(1200px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.01)`;
   card.style.boxShadow=`0 ${Math.abs(rotateX)*3}px ${40+Math.abs(rotateX)*10}px rgba(0,0,0,.3)`;
  });
  card.addEventListener('mouseleave',()=>{
   card.style.transform='perspective(1200px) rotateX(0) rotateY(0) scale(1)';
   card.style.boxShadow=null;
  });
 });
}

/* ---- parallax + cursor glow + sparkle trail (fine-pointer devices only) ---- */
if(canHover){
 const cursorGlow=document.getElementById('cursorGlow');
 const galaxyEls=[document.querySelector('.galaxy-cloud'),document.querySelector('.galaxy-core'),document.querySelector('.galaxy-dust')];
 const moonEl=document.querySelector('.moon');
 const starsA=document.querySelector('.stars-a');
 let mx=innerWidth/2,my=innerHeight/2,tx=mx,ty=my,lastSpark=0;
 cursorGlow.classList.add('on');
 window.addEventListener('mousemove',e=>{
  mx=e.clientX;my=e.clientY;
  const now=performance.now();
  if(now-lastSpark>90){
   lastSpark=now;
   if(Math.random()<.5){
    const s=document.createElement('div');
    s.className='spark-trail';
    const sz=2+Math.random()*2.5;
    s.style.width=sz+'px';s.style.height=sz+'px';
    s.style.left=(e.clientX+(Math.random()*16-8))+'px';
    s.style.top=(e.clientY+(Math.random()*16-8))+'px';
    s.style.setProperty('--sx',(Math.random()*24-12)+'px');
    s.style.setProperty('--sy',(10+Math.random()*22)+'px');
    document.body.appendChild(s);
    setTimeout(()=>s.remove(),950);
   }
  }
 });
 function raf(){
  tx+=(mx-tx)*.06;ty+=(my-ty)*.06;
  cursorGlow.style.transform=`translate3d(${tx}px,${ty}px,0)`;
  const nx=(tx/innerWidth-.5), ny=(ty/innerHeight-.5);
  galaxyEls.forEach((el,i)=>{if(el)el.style.transform=`rotate(-17deg) translate3d(${nx*(8+i*4)}px,${ny*(6+i*3)}px,0)`});
  if(moonEl)moonEl.style.transform=`translate3d(${nx*-14}px,${ny*-10}px,0)`;
  if(starsA)starsA.style.transform=`translate3d(${nx*-6}px,${ny*-6}px,0)`;
  requestAnimationFrame(raf);
 }
 raf();
}

function burst(n){
 for(let i=0;i<n;i++)setTimeout(()=>makePetal(true),i*22);
}
function celebrate(){
 burst(160);
 fireworks(3);
 chime(880);
 setTimeout(()=>alert('Happy Birthday, Pooja Daksh. ♡\\n\\nMay Mahadev keep you happy, peaceful and protected.\\nAnd may this year be exceptionally kind to you.'),700);
}

/* ---- fireworks burst (DOM particles, no canvas needed) ---- */
const FW_COLORS=['#ffe6ef','#ffffff','#f2d6e6','#ffd9a8','#dcd1ff'];
function fireworkAt(x,y){
 const count=26;
 for(let i=0;i<count;i++){
  const p=document.createElement('div');
  p.className='fw-particle';
  const angle=(Math.PI*2*i)/count + Math.random()*.3;
  const dist=60+Math.random()*110;
  p.style.setProperty('--fx',(Math.cos(angle)*dist)+'px');
  p.style.setProperty('--fy',(Math.sin(angle)*dist)+'px');
  p.style.setProperty('--fwd',(1+Math.random()*.6)+'s');
  p.style.left=x+'px';p.style.top=y+'px';
  p.style.background=FW_COLORS[Math.floor(Math.random()*FW_COLORS.length)];
  p.style.boxShadow=`0 0 8px 1px ${p.style.background}`;
  document.body.appendChild(p);
  setTimeout(()=>p.remove(),1700);
 }
}
function fireworks(bursts=3){
 for(let i=0;i<bursts;i++){
  setTimeout(()=>{
   const x=innerWidth*(.25+Math.random()*.5);
   const y=innerHeight*(.2+Math.random()*.35);
   fireworkAt(x,y);
   chime(700+Math.random()*300);
  },i*450);
 }
}

/* ---- typewriter on hero ---- */
(function typewriter(){
 const el=document.getElementById('typeHey');
 const text='Hey,';
 let i=0;
 el.textContent='';
 const iv=setInterval(()=>{
  el.textContent=text.slice(0,i+1);
  i++;
  if(i>=text.length){clearInterval(iv);el.classList.add('done')}
 },140);
})();

/* ---- soft chime via WebAudio (no external file needed) ---- */
let audioCtx=null;
function chime(freq){
 try{
  audioCtx=audioCtx||new (window.AudioContext||window.webkitAudioContext)();
  const o=audioCtx.createOscillator();
  const g=audioCtx.createGain();
  o.type='sine';o.frequency.value=freq;
  g.gain.setValueAtTime(0.0001,audioCtx.currentTime);
  g.gain.exponentialRampToValueAtTime(0.05,audioCtx.currentTime+0.02);
  g.gain.exponentialRampToValueAtTime(0.0001,audioCtx.currentTime+0.9);
  o.connect(g);g.connect(audioCtx.destination);
  o.start();o.stop(audioCtx.currentTime+0.9);
 }catch(e){/* audio not available, ignore */}
}

/* ---- candle blow ---- */
let candleBlown=false;
function blowCandle(){
 if(candleBlown)return;
 candleBlown=true;
 document.getElementById('flame').classList.add('out');
 document.getElementById('smoke').classList.add('show');
 document.getElementById('wishReveal').classList.add('show');
 document.getElementById('blowBtn').textContent='Wish made ♡';
 chime(523);
 burst(40);
 fireworks(1);
}

/* ---- background music toggle (only shows up if a music file is present) ---- */
const bgMusic=document.getElementById('bgMusic');
const musicToggle=document.getElementById('musicToggle');
let musicChecked=false;
bgMusic.addEventListener('loadedmetadata',()=>{
 if(!musicChecked){musicChecked=true;musicToggle.classList.remove('hidden');musicToggle.classList.add('paused');}
});
bgMusic.addEventListener('error',()=>{ /* no music file added yet — keep the button hidden */ });
function toggleMusic(){
 if(bgMusic.paused){bgMusic.play().catch(()=>{});musicToggle.classList.remove('paused');}
 else{bgMusic.pause();musicToggle.classList.add('paused');}
}
</script>
</body>
</html>

"""


@app.route("/")
def birthday():
    return render_template_string(INDEX_HTML)


if __name__ == "__main__":
    print("\U0001F319 Madam Ji Birthday website is running!")
    print("Open: http://127.0.0.1:5000")
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
