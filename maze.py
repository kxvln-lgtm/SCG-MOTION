import bpy, math, os, random, argparse
from mathutils import Vector

# Invoke: blender -b -t 4 --python blender/maze.py -- --mode preview
args=__import__('sys').argv
args=args[args.index('--')+1:] if '--' in args else []
mode=args[args.index('--mode')+1] if '--mode' in args else 'preview'
preview=mode=='preview'
random.seed(2608)
bpy.ops.object.select_all(action='SELECT'); bpy.ops.object.delete(use_global=False)
sc=bpy.context.scene
sc.render.engine='CYCLES'
sc.cycles.samples=8 if preview else 16
sc.render.resolution_x=360 if preview else 720
sc.render.resolution_y=640 if preview else 1280
sc.render.resolution_percentage=100
sc.render.fps=24
sc.frame_start=1;sc.frame_end=120 if preview else 720
sc.render.image_settings.file_format='PNG'
sc.render.image_settings.color_mode='RGB'
sc.render.filepath=os.path.abspath('out/frames/frame_')
sc.render.film_transparent=False
sc.world.color=(0.07,0.07,0.07)

# PBR architectural material setup
def mat(name,color,roughness=0.8,metal=0):
 m=bpy.data.materials.new(name);m.use_nodes=True
 n=m.node_tree.nodes.get('Principled BSDF')
 n.inputs['Base Color'].default_value=(*color,1)
 n.inputs['Roughness'].default_value=roughness
 n.inputs['Metallic'].default_value=metal
 return m
chalk=mat('SCG / porcelain concrete',(.78,.81,.85),.72)
obsidian=mat('SCG / obsidian',(.015,.019,.026),.31,.25)
metal=mat('SCG / brushed steel',(.15,.18,.21),.29,.8)

def block(name,loc,size,material):
 bpy.ops.mesh.primitive_cube_add(size=1,location=loc)
 o=bpy.context.object;o.name=name;o.dimensions=size
 bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
 o.data.materials.append(material)
 b=o.modifiers.new('Light-catching bevel','BEVEL');b.width=.055;b.segments=2
 o.modifiers.new('Weighted normals','WEIGHTED_NORMAL')
 return o

# Interlocking corridor runs; openings are preserved at every junction.
P=[(0,0),(0,10),(0,20),(10,20),(20,20),(20,30),(20,40),(10,40),(0,40),(0,50)]
block('Endless obsidian floor',(10,25,-.2),(48,70,.4),obsidian)
for i in range(len(P)-1):
 x,y=P[i];u,v=P[i+1]
 if x==u:
  for side in (-1,1):block('Wall %02d %d'%(i,side),(x+side*3.2,(y+v)/2,3.5),(.65,abs(v-y)-1.5,7),chalk)
 else:
  for side in (-1,1):block('Wall %02d %d'%(i,side),((x+u)/2,y+side*3.2,3.5),(abs(u-x)-1.5,.65,7),chalk)
# Art-directed repeated overhead fins, avoid flight path collision.
for i in range(24):
 y=-1+i*2.4
 block('Monolith rhythm %02d'%i,(-11,y,random.uniform(3,8)),(random.uniform(.5,1.8),.8,random.uniform(5,12)),metal)
# Light strips high above flight corridor
for j,(x,y) in enumerate(P):
 data=bpy.data.lights.new('Architectural softbox %02d'%j,'AREA')
 data.energy=1250;data.shape='DISK';data.size=9
 obj=bpy.data.objects.new(data.name,data);sc.collection.objects.link(obj)
 obj.location=(x,y,6.7)
 obj.rotation_euler=(0,0,0)
# Wide overhead fill
for x,y in [(10,10),(10,30),(0,47)]:
 data=bpy.data.lights.new('High fill','AREA');data.energy=1800;data.size=18
 o=bpy.data.objects.new('High fill',data);sc.collection.objects.link(o)
 o.location=(x,y,17)

camera_data=bpy.data.cameras.new('Cinematic FPV 18mm');camera=bpy.data.objects.new('Cinematic FPV 18mm',camera_data)
sc.collection.objects.link(camera);sc.camera=camera
camera_data.lens=18;camera_data.clip_end=200
# Smooth Catmull-Rom path with eased traversal. Uses tangent lookahead for yaw.
def sample(t):
 t=max(0,min(len(P)-1-1e-6,t));i=int(t);f=t-i
 p0=Vector(P[max(i-1,0)]);p1=Vector(P[i]);p2=Vector(P[i+1]);p3=Vector(P[min(i+2,len(P)-1)])
 xy=.5*((2*p1)+(-p0+p2)*f+(2*p0-5*p1+4*p2-p3)*f*f+(-p0+3*p1-3*p2+p3)*f*f*f)
 return Vector((xy.x,xy.y,1.9+0.12*math.sin(t*3)))
for frame in range(1,sc.frame_end+1):
 q=(frame-1)/max(1,sc.frame_end-1)
 t=q*(len(P)-1-0.001)
 pos=sample(t)
 look=sample(min(t+.18,len(P)-1-.0001))
 delta=look-pos
 if delta.length<.00001:delta=Vector((0,1,0))
 camera.location=pos
 camera.rotation_euler=delta.to_track_quat('-Z','Y').to_euler()
 camera.keyframe_insert(data_path='location',frame=frame)
 camera.keyframe_insert(data_path='rotation_euler',frame=frame)
# Linear movement between closely sampled frames avoids oscillations.
if camera.animation_data and camera.animation_data.action:
 for fc in camera.animation_data.action.fcurves:
  for key in fc.keyframe_points:key.interpolation='LINEAR'
sc.view_settings.view_transform='AgX'
os.makedirs('out/frames',exist_ok=True)
bpy.ops.wm.save_as_mainfile(filepath=os.path.abspath('out/SCG-The-Maze.blend'))
bpy.ops.render.render(animation=True)
