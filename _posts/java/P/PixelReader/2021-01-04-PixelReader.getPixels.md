---
title: PixelReader.getPixels()
permalink: Java/PixelReader/getPixels
date: 2021-01-04
key: JavaJava.P.PixelReader
category: java
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
* **int x**,  {% include w3api/param_description.html metodo=_data parametro="int x" %}
* **int scanlineStride**,  {% include w3api/param_description.html metodo=_data parametro="int scanlineStride" %}
* **int y**,  {% include w3api/param_description.html metodo=_data parametro="int y" %}
* **WritablePixelFormat&lt;T&gt; pixelformat**,  {% include w3api/param_description.html metodo=_data parametro="WritablePixelFormat<T> pixelformat" %}
* **byte[] buffer**,  {% include w3api/param_description.html metodo=_data parametro="byte[] buffer" %}
* **WritablePixelFormat&lt;IntBuffer&gt; pixelformat**,  {% include w3api/param_description.html metodo=_data parametro="WritablePixelFormat<IntBuffer> pixelformat" %}
* **T buffer**,  {% include w3api/param_description.html metodo=_data parametro="T buffer" %}
* **int[] buffer**,  {% include w3api/param_description.html metodo=_data parametro="int[] buffer" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}
* **int w**,  {% include w3api/param_description.html metodo=_data parametro="int w" %}
* **int h**,  {% include w3api/param_description.html metodo=_data parametro="int h" %}
* **WritablePixelFormat&lt;ByteBuffer&gt; pixelformat**,  {% include w3api/param_description.html metodo=_data parametro="WritablePixelFormat<ByteBuffer> pixelformat" %}

## Clase Padre
[PixelReader](/Java/PixelReader/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PixelReader.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
