---
title: MemoryImageSource.newPixels()
permalink: Java/MemoryImageSource/newPixels
date: 2021-01-11
key: JavaJava.M.MemoryImageSource
category: Java
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
* **byte[] newpix**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] newpix" %}
* **int h**,  {% include w3api/param_description.html metodo=_dato parametro="int h" %}
* **int scansize**,  {% include w3api/param_description.html metodo=_dato parametro="int scansize" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **ColorModel newmodel**,  {% include w3api/param_description.html metodo=_dato parametro="ColorModel newmodel" %}
* **int w**,  {% include w3api/param_description.html metodo=_dato parametro="int w" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **boolean framenotify**,  {% include w3api/param_description.html metodo=_dato parametro="boolean framenotify" %}
* **int[] newpix**,  {% include w3api/param_description.html metodo=_dato parametro="int[] newpix" %}

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
