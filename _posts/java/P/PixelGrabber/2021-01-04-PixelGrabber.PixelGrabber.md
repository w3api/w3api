---
title: PixelGrabber.PixelGrabber()
permalink: Java/PixelGrabber/PixelGrabber
date: 2021-01-04
key: JavaJava.P.PixelGrabber
category: java
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
* **int off**,  {% include w3api/param_description.html metodo=_data parametro="int off" %}
* **int scansize**,  {% include w3api/param_description.html metodo=_data parametro="int scansize" %}
* **int y**,  {% include w3api/param_description.html metodo=_data parametro="int y" %}
* **ImageProducer ip**,  {% include w3api/param_description.html metodo=_data parametro="ImageProducer ip" %}
* **boolean forceRGB**,  {% include w3api/param_description.html metodo=_data parametro="boolean forceRGB" %}
* **Image img**,  {% include w3api/param_description.html metodo=_data parametro="Image img" %}
* **int w**,  {% include w3api/param_description.html metodo=_data parametro="int w" %}
* **int h**,  {% include w3api/param_description.html metodo=_data parametro="int h" %}
* **int[] pix**,  {% include w3api/param_description.html metodo=_data parametro="int[] pix" %}
* **int x**,  {% include w3api/param_description.html metodo=_data parametro="int x" %}

## Clase Padre
[PixelGrabber](/Java/PixelGrabber/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PixelGrabber.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
