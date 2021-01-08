---
title: MemoryImageSource.newPixels()
permalink: Java/MemoryImageSource/newPixels
date: 2021-01-04
key: JavaJava.M.MemoryImageSource
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MemoryImageSource.metodos valor="newPixels" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void newPixels()
public void newPixels(byte[] newpix, ColorModel newmodel, int offset, int scansize)
public void newPixels(int[] newpix, ColorModel newmodel, int offset, int scansize)
public void newPixels(int x, int y, int w, int h)
public void newPixels(int x, int y, int w, int h, boolean framenotify)
~~~

## Parámetros
* **ColorModel newmodel**,  {% include w3api/param_description.html metodo=_data parametro="ColorModel newmodel" %}
* **int scansize**,  {% include w3api/param_description.html metodo=_data parametro="int scansize" %}
* **int y**,  {% include w3api/param_description.html metodo=_data parametro="int y" %}
* **int[] newpix**,  {% include w3api/param_description.html metodo=_data parametro="int[] newpix" %}
* **byte[] newpix**,  {% include w3api/param_description.html metodo=_data parametro="byte[] newpix" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}
* **int h**,  {% include w3api/param_description.html metodo=_data parametro="int h" %}
* **int w**,  {% include w3api/param_description.html metodo=_data parametro="int w" %}
* **boolean framenotify**,  {% include w3api/param_description.html metodo=_data parametro="boolean framenotify" %}
* **int x**,  {% include w3api/param_description.html metodo=_data parametro="int x" %}

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
