---
title: PixelReader.getPixels()
permalink: /Java/PixelReader/getPixels/
date: 2021-01-11
key: Java.P.PixelReader
category: Java
tags: ['java se', 'javafx.scene.image', 'javafx.graphics', 'metodo java', 'JavaFX 2.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PixelReader.metodos valor="getPixels" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void getPixels(int x, int y, int w, int h, WritablePixelFormat<ByteBuffer> pixelformat, byte[] buffer, int offset, int scanlineStride)
void getPixels(int x, int y, int w, int h, WritablePixelFormat<IntBuffer> pixelformat, int[] buffer, int offset, int scanlineStride)
<T extends Buffer>void getPixels(int x, int y, int w, int h, WritablePixelFormat<T> pixelformat, T buffer, int scanlineStride)
~~~

## Parámetros
* **WritablePixelFormat&lt;ByteBuffer&gt; pixelformat**,  {% include w3api/param_description.html metodo=_dato parametro="WritablePixelFormat<ByteBuffer> pixelformat" %}
* **byte[] buffer**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] buffer" %}
* **int h**,  {% include w3api/param_description.html metodo=_dato parametro="int h" %}
* **WritablePixelFormat&lt;IntBuffer&gt; pixelformat**,  {% include w3api/param_description.html metodo=_dato parametro="WritablePixelFormat<IntBuffer> pixelformat" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **int[] buffer**,  {% include w3api/param_description.html metodo=_dato parametro="int[] buffer" %}
* **WritablePixelFormat&lt;T&gt; pixelformat**,  {% include w3api/param_description.html metodo=_dato parametro="WritablePixelFormat<T> pixelformat" %}
* **int w**,  {% include w3api/param_description.html metodo=_dato parametro="int w" %}
* **T buffer**,  {% include w3api/param_description.html metodo=_dato parametro="T buffer" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **int scanlineStride**,  {% include w3api/param_description.html metodo=_dato parametro="int scanlineStride" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}

## Clase Padre
[PixelReader](/Java/PixelReader/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
