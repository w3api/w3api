---
title: TexturePaint.createContext()
permalink: /Java/TexturePaint/createContext/
date: 2021-01-11
key: Java.T.TexturePaint
category: Java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TexturePaint.metodos valor="createContext" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PaintContext createContext(ColorModel cm, Rectangle deviceBounds, Rectangle2D userBounds, AffineTransform xform, RenderingHints hints)
~~~

## Parámetros
* **ColorModel cm**,  {% include w3api/param_description.html metodo=_dato parametro="ColorModel cm" %}
* **Rectangle deviceBounds**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle deviceBounds" %}
* **Rectangle2D userBounds**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle2D userBounds" %}
* **RenderingHints hints**,  {% include w3api/param_description.html metodo=_dato parametro="RenderingHints hints" %}
* **AffineTransform xform**,  {% include w3api/param_description.html metodo=_dato parametro="AffineTransform xform" %}

## Clase Padre
[TexturePaint](/Java/TexturePaint/)

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
