---
title: LinearGradientPaint.createContext()
permalink: Java/LinearGradientPaint/createContext
date: 2021-01-04
key: JavaJava.L.LinearGradientPaint
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LinearGradientPaint.metodos valor="createContext" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PaintContext createContext(ColorModel cm, Rectangle deviceBounds, Rectangle2D userBounds, AffineTransform transform, RenderingHints hints)
~~~

## Parámetros
* **RenderingHints hints**,  {% include w3api/param_description.html metodo=_data parametro="RenderingHints hints" %}
* **ColorModel cm**,  {% include w3api/param_description.html metodo=_data parametro="ColorModel cm" %}
* **Rectangle deviceBounds**,  {% include w3api/param_description.html metodo=_data parametro="Rectangle deviceBounds" %}
* **Rectangle2D userBounds**,  {% include w3api/param_description.html metodo=_data parametro="Rectangle2D userBounds" %}
* **AffineTransform transform**,  {% include w3api/param_description.html metodo=_data parametro="AffineTransform transform" %}

## Clase Padre
[LinearGradientPaint](/Java/LinearGradientPaint/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LinearGradientPaint.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
