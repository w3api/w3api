---
title: PixelGrabber.setPixels()
permalink: Java/PixelGrabber/setPixels
date: 2021-01-04
key: JavaJava.P.PixelGrabber
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PixelGrabber.metodos valor="setPixels" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setPixels(int srcX, int srcY, int srcW, int srcH, ColorModel model, byte[] pixels, int srcOff, int srcScan)
public void setPixels(int srcX, int srcY, int srcW, int srcH, ColorModel model, int[] pixels, int srcOff, int srcScan)
~~~

## Parámetros
* **int srcY**,  {% include w3api/param_description.html metodo=_data parametro="int srcY" %}
* **int srcOff**,  {% include w3api/param_description.html metodo=_data parametro="int srcOff" %}
* **byte[] pixels**,  {% include w3api/param_description.html metodo=_data parametro="byte[] pixels" %}
* **int srcW**,  {% include w3api/param_description.html metodo=_data parametro="int srcW" %}
* **int srcH**,  {% include w3api/param_description.html metodo=_data parametro="int srcH" %}
* **int[] pixels**,  {% include w3api/param_description.html metodo=_data parametro="int[] pixels" %}
* **ColorModel model**,  {% include w3api/param_description.html metodo=_data parametro="ColorModel model" %}
* **int srcX**,  {% include w3api/param_description.html metodo=_data parametro="int srcX" %}
* **int srcScan**,  {% include w3api/param_description.html metodo=_data parametro="int srcScan" %}

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
