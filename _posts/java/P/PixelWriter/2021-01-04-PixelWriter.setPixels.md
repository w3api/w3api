---
title: PixelWriter.setPixels()
permalink: Java/PixelWriter/setPixels
date: 2021-01-04
key: JavaJava.P.PixelWriter
category: java
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
* **int dstx**,  {% include w3api/param_description.html metodo=_data parametro="int dstx" %}
* **int scanlineStride**,  {% include w3api/param_description.html metodo=_data parametro="int scanlineStride" %}
* **PixelFormat&lt;T&gt; pixelformat**,  {% include w3api/param_description.html metodo=_data parametro="PixelFormat<T> pixelformat" %}
* **int y**,  {% include w3api/param_description.html metodo=_data parametro="int y" %}
* **int srcx**,  {% include w3api/param_description.html metodo=_data parametro="int srcx" %}
* **byte[] buffer**,  {% include w3api/param_description.html metodo=_data parametro="byte[] buffer" %}
* **T buffer**,  {% include w3api/param_description.html metodo=_data parametro="T buffer" %}
* **int[] buffer**,  {% include w3api/param_description.html metodo=_data parametro="int[] buffer" %}
* **int dsty**,  {% include w3api/param_description.html metodo=_data parametro="int dsty" %}
* **int srcy**,  {% include w3api/param_description.html metodo=_data parametro="int srcy" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}
* **PixelFormat&lt;IntBuffer&gt; pixelformat**,  {% include w3api/param_description.html metodo=_data parametro="PixelFormat<IntBuffer> pixelformat" %}
* **PixelReader reader**,  {% include w3api/param_description.html metodo=_data parametro="PixelReader reader" %}
* **int w**,  {% include w3api/param_description.html metodo=_data parametro="int w" %}
* **int h**,  {% include w3api/param_description.html metodo=_data parametro="int h" %}
* **PixelFormat&lt;ByteBuffer&gt; pixelformat**,  {% include w3api/param_description.html metodo=_data parametro="PixelFormat<ByteBuffer> pixelformat" %}
* **int x**,  {% include w3api/param_description.html metodo=_data parametro="int x" %}

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
{%- for _ldc in site.data.Java.P.PixelWriter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
