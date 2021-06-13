---
title: PixelGrabber.setPixels()
permalink: /Java/PixelGrabber/setPixels/
date: 2021-01-11
key: Java.P.PixelGrabber
category: Java
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
* **int srcY**,  {% include w3api/param_description.html metodo=_dato parametro="int srcY" %}
* **int srcOff**,  {% include w3api/param_description.html metodo=_dato parametro="int srcOff" %}
* **int srcW**,  {% include w3api/param_description.html metodo=_dato parametro="int srcW" %}
* **int srcScan**,  {% include w3api/param_description.html metodo=_dato parametro="int srcScan" %}
* **byte[] pixels**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] pixels" %}
* **int[] pixels**,  {% include w3api/param_description.html metodo=_dato parametro="int[] pixels" %}
* **int srcH**,  {% include w3api/param_description.html metodo=_dato parametro="int srcH" %}
* **int srcX**,  {% include w3api/param_description.html metodo=_dato parametro="int srcX" %}
* **ColorModel model**,  {% include w3api/param_description.html metodo=_dato parametro="ColorModel model" %}

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
