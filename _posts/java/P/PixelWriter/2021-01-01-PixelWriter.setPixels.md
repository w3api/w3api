---
title: PixelWriter.setPixels()
permalink: /Java/PixelWriter/setPixels/
date: 2021-01-11
key: Java.P.PixelWriter
category: Java
tags: ['java se', 'javafx.scene.image', 'javafx.graphics', 'metodo java', 'JavaFX 2.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PixelWriter.metodos valor="setPixels" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setPixels(int x, int y, int w, int h, PixelFormat<ByteBuffer> pixelformat, byte[] buffer, int offset, int scanlineStride)
void setPixels(int x, int y, int w, int h, PixelFormat<IntBuffer> pixelformat, int[] buffer, int offset, int scanlineStride)
<T extends Buffer>void setPixels(int x, int y, int w, int h, PixelFormat<T> pixelformat, T buffer, int scanlineStride)
void setPixels(int dstx, int dsty, int w, int h, PixelReader reader, int srcx, int srcy)
~~~

## Parámetros
* **PixelFormat&lt;IntBuffer&gt; pixelformat**,  {% include w3api/param_description.html metodo=_dato parametro="PixelFormat<IntBuffer> pixelformat" %}
* **PixelFormat&lt;T&gt; pixelformat**,  {% include w3api/param_description.html metodo=_dato parametro="PixelFormat<T> pixelformat" %}
* **int srcx**,  {% include w3api/param_description.html metodo=_dato parametro="int srcx" %}
* **byte[] buffer**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] buffer" %}
* **int h**,  {% include w3api/param_description.html metodo=_dato parametro="int h" %}
* **int[] buffer**,  {% include w3api/param_description.html metodo=_dato parametro="int[] buffer" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **int dsty**,  {% include w3api/param_description.html metodo=_dato parametro="int dsty" %}
* **int srcy**,  {% include w3api/param_description.html metodo=_dato parametro="int srcy" %}
* **PixelFormat&lt;ByteBuffer&gt; pixelformat**,  {% include w3api/param_description.html metodo=_dato parametro="PixelFormat<ByteBuffer> pixelformat" %}
* **int w**,  {% include w3api/param_description.html metodo=_dato parametro="int w" %}
* **T buffer**,  {% include w3api/param_description.html metodo=_dato parametro="T buffer" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **int scanlineStride**,  {% include w3api/param_description.html metodo=_dato parametro="int scanlineStride" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **int dstx**,  {% include w3api/param_description.html metodo=_dato parametro="int dstx" %}
* **PixelReader reader**,  {% include w3api/param_description.html metodo=_dato parametro="PixelReader reader" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[PixelWriter](/Java/PixelWriter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
