---
title: MemoryImageSource.MemoryImageSource()
permalink: Java/MemoryImageSource/MemoryImageSource
date: 2021-01-04
key: JavaJava.M.MemoryImageSource
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MemoryImageSource.constructores valor="MemoryImageSource" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MemoryImageSource(int w, int h, int[] pix, int off, int scan)
public MemoryImageSource(int w, int h, int[] pix, int off, int scan, Hashtable<?,?> props)
public MemoryImageSource(int w, int h, ColorModel cm, byte[] pix, int off, int scan)
public MemoryImageSource(int w, int h, ColorModel cm, byte[] pix, int off, int scan, Hashtable<?,?> props)
public MemoryImageSource(int w, int h, ColorModel cm, int[] pix, int off, int scan)
public MemoryImageSource(int w, int h, ColorModel cm, int[] pix, int off, int scan, Hashtable<?,?> props)
~~~

## Parámetros
* **int off**,  {% include w3api/param_description.html metodo=_data parametro="int off" %}
* **int scan**,  {% include w3api/param_description.html metodo=_data parametro="int scan" %}
* **ColorModel cm**,  {% include w3api/param_description.html metodo=_data parametro="ColorModel cm" %}
* **byte[] pix**,  {% include w3api/param_description.html metodo=_data parametro="byte[] pix" %}
* **?&gt; props**,  {% include w3api/param_description.html metodo=_data parametro="?> props" %}
* **int w**,  {% include w3api/param_description.html metodo=_data parametro="int w" %}
* **int h**,  {% include w3api/param_description.html metodo=_data parametro="int h" %}
* **Hashtable&lt;?**,  {% include w3api/param_description.html metodo=_data parametro="Hashtable<?" %}
* **int[] pix**,  {% include w3api/param_description.html metodo=_data parametro="int[] pix" %}

## Clase Padre
[MemoryImageSource](/Java/MemoryImageSource/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MemoryImageSource.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
