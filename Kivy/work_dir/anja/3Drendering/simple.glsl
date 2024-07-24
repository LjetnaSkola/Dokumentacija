/*
    Ovaj GLSL kod sastoji se od jednostavnog vertex i fragment shadera 
    koji se koriste za osvjetljavanje objekta u 3D prostoru koristeći
    Lambertov kosinusni zakon.

    Ovaj set shadera jednostavno osvjetljava objekte u 3D prostoru koristeći 
    Lambertov zakon kosinusa. Vertex shader transformira vrhove objekta u prostor 
    za prikaz, dok fragment shader računa difuzno osvjetljenje na temelju normala 
    vrhova i pozicije svjetla (pretpostavljene na poziciji oka). Ova tehnika je 
    osnovna ali može poslužiti kao temelj za kompleksnije renderiranje osvjetljenja
    u OpenGL-u.
*/

/* simple.glsl

simple diffuse lighting based on laberts cosine law; see e.g.:
    http://en.wikipedia.org/wiki/Lambertian_reflectance
    http://en.wikipedia.org/wiki/Lambert%27s_cosine_law
*/
---VERTEX SHADER-------------------------------------------------------
#ifdef GL_ES
    precision highp float;
#endif

attribute vec3  v_pos;
attribute vec3  v_normal;

uniform mat4 modelview_mat;
uniform mat4 projection_mat;

varying vec4 normal_vec;
varying vec4 vertex_pos;

void main (void) {
    //compute vertex position in eye_space and normalize normal vector
    vec4 pos = modelview_mat * vec4(v_pos,1.0);
    vertex_pos = pos;
    normal_vec = vec4(v_normal,0.0);
    gl_Position = projection_mat * pos;
}


---FRAGMENT SHADER-----------------------------------------------------
#ifdef GL_ES
    precision highp float;
#endif

varying vec4 normal_vec;
varying vec4 vertex_pos;

uniform mat4 normal_mat;

void main (void){
    //correct normal, and compute light vector (assume light at the eye)
    vec4 v_normal = normalize( normal_mat * normal_vec ) ;
    vec4 v_light = normalize( vec4(0,0,0,1) - vertex_pos );
    //reflectance based on lamberts law of cosine
    float theta = clamp(dot(v_normal, v_light), 0.0, 1.0);
    gl_FragColor = vec4(theta, theta, theta, 1.0);
}