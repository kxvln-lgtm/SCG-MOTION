import React from 'react';
import {AbsoluteFill,interpolate,useCurrentFrame,spring,useVideoConfig} from 'remotion';
const chapters=[
{start:0,end:420,kicker:'STAGE CRAFT GROUP',headline:'ONE SYSTEM.',sub:'ARQASHAN ZHUREKPEN'},
{start:420,end:840,kicker:'PEOPLE',headline:'WE MOVE.',sub:'BIRLIKTE ALGA'},
{start:840,end:1260,kicker:'THE BACKSTAGE UNION',headline:'TOGETHER.',sub:'BIR MAQSAT'},
{start:1260,end:1680,kicker:'BACKSTAGE STAFF AGENT',headline:'PRECISION.',sub:'AR ISTIN ARTYNDA'},
{start:1680,end:2100,kicker:'CREATIVE BUREAU',headline:'IMAGINE.',sub:'IDEIADAN SHYNDYQQA'},
{start:2100,end:2520,kicker:'SCENIQUE',headline:'FEEL IT.',sub:'SAHNA TYNYSY'},
{start:2520,end:3060,kicker:'FIVE REGIONS',headline:'ONE PULSE.',sub:'BES ONIR. BIR ZHUREK.'},
{start:3060,end:3600,kicker:'STAGE CRAFT GROUP',headline:'SCG',sub:'ONE SYSTEM.'}];
const clamp=(v:number)=>Math.max(0,Math.min(1,v));
export const Film:React.FC=()=>{const f=useCurrentFrame();const {fps}=useVideoConfig();const c=chapters.find(x=>f>=x.start&&f<x.end)??chapters[7];const local=f-c.start;const intro=spring({frame:local,fps,config:{damping:18,stiffness:115}});const outro=clamp((c.end-f)/35);const opacity=clamp(local/22)*outro;const scale=interpolate(intro,[0,1],[1.32,1]);const sweep=(f%210)/210;return <AbsoluteFill style={{background:'#050505',color:'#f7f7f7',overflow:'hidden',fontFamily:'Arial,Helvetica,sans-serif'}}><AbsoluteFill style={{background:'radial-gradient(circle at '+(25+50*sweep)+'% 50%,#182033 0%,#080a0e 36%,#050505 70%)'}}/><div style={{position:'absolute',top:70,left:100,fontSize:24,letterSpacing:8,fontWeight:600,opacity:.55}}>SCG / 2026</div><div style={{position:'absolute',top:70,right:100,fontSize:24,letterSpacing:4,opacity:.55}}>ONE SYSTEM</div><AbsoluteFill style={{alignItems:'center',justifyContent:'center',opacity,transform:'scale('+scale+')'}}><div style={{fontSize:25,letterSpacing:12,fontWeight:700,marginBottom:34,color:'#aab6cc'}}>{c.kicker}</div><div style={{fontSize:c.headline==='SCG'?330:Math.min(180,1400/c.headline.length*1.5),fontWeight:900,letterSpacing:-9,lineHeight:1,textAlign:'center'}}>{c.headline}</div><div style={{fontSize:28,letterSpacing:9,marginTop:44,opacity:.7}}>{c.sub}</div></AbsoluteFill><div style={{position:'absolute',bottom:68,left:100,right:100,height:2,background:'#333'}}><div style={{width:(f/3600*100)+'%',height:'100%',background:'#eee'}}/></div></AbsoluteFill>};
