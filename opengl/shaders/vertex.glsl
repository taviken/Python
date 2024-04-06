#version 430 core

layout (location = 0) in vec3 vertexPos;


out vec2 fragmentTextureCoordinate;

void main()
{
    gl_Position = vec4(vertexPos.x, vertexPos.y, vertexPos.z, 1.0);
    //gl_Position = vec4(vertexPos, 1.0); // this is shorthand for just putting a 3 vec and appending the fourth 1.0
}