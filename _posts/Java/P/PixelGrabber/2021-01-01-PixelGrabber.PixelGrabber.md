---
title: PixelGrabber.PixelGrabber()
permalink: /Java/PixelGrabber/PixelGrabber/
date: 2021-01-11
key: Java.P.PixelGrabber
category: Java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PixelGrabber.constructores valor="PixelGrabber" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PixelGrabber(ImageProducer ip, int x, int y, int w, int h, int[] pix, int off, int scansize)
public PixelGrabber(Image img, int x, int y, int w, int h, boolean forceRGB)
public PixelGrabber(Image img, int x, int y, int w, int h, int[] pix, int off, int scansize)
~~~

## Parámetros
* **boolean forceRGB**,  {% include w3api/param_description.html metodo=_dato parametro="boolean forceRGB" %}
* **int[] pix**,  {% include w3api/param_description.html metodo=_dato parametro="int[] pix" %}
* **int h**,  {% include w3api/param_description.html metodo=_dato parametro="int h" %}
* **int scansize**,  {% include w3api/param_description.html metodo=_dato parametro="int scansize" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **int w**,  {% include w3api/param_description.html metodo=_dato parametro="int w" %}
* **Image img**,  {% include w3api/param_description.html metodo=_dato parametro="Image img" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **ImageProducer ip**,  {% include w3api/param_description.html metodo=_dato parametro="ImageProducer ip" %}
* **int off**,  {% include w3api/param_description.html metodo=_dato parametro="int off" %}

## Clase Padre
[PixelGrabber](/Java/PixelGrabber/)

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
