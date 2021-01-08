---
title: PixelGrabber.grabPixels()
permalink: Java/PixelGrabber/grabPixels
date: 2021-01-04
key: JavaJava.P.PixelGrabber
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PixelGrabber.metodos valor="grabPixels" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean grabPixels() throws InterruptedException
public boolean grabPixels(long ms) throws InterruptedException
~~~

## Parámetros
* **long ms**,  {% include w3api/param_description.html metodo=_data parametro="long ms" %}

## Excepciones
[InterruptedException](/Java/InterruptedException/)

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
