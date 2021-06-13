---
title: MemoryImageSource.MemoryImageSource()
permalink: Java/MemoryImageSource/MemoryImageSource
date: 2021-01-11
key: JavaJava.M.MemoryImageSource
category: Java
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
* **ColorModel cm**,  {% include w3api/param_description.html metodo=_dato parametro="ColorModel cm" %}
* **byte[] pix**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] pix" %}
* **int[] pix**,  {% include w3api/param_description.html metodo=_dato parametro="int[] pix" %}
* **int h**,  {% include w3api/param_description.html metodo=_dato parametro="int h" %}
* **Hashtable&lt;?**,  {% include w3api/param_description.html metodo=_dato parametro="Hashtable<?" %}
* **?&gt; props**,  {% include w3api/param_description.html metodo=_dato parametro="?> props" %}
* **int w**,  {% include w3api/param_description.html metodo=_dato parametro="int w" %}
* **int scan**,  {% include w3api/param_description.html metodo=_dato parametro="int scan" %}
* **int off**,  {% include w3api/param_description.html metodo=_dato parametro="int off" %}

## Clase Padre
[MemoryImageSource](/Java/MemoryImageSource/)

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
