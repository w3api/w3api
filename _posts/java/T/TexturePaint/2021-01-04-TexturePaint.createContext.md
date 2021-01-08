---
title: TexturePaint.createContext()
permalink: Java/TexturePaint/createContext
date: 2021-01-04
key: JavaJava.T.TexturePaint
category: java
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
* **RenderingHints hints**,  {% include w3api/param_description.html metodo=_data parametro="RenderingHints hints" %}
* **ColorModel cm**,  {% include w3api/param_description.html metodo=_data parametro="ColorModel cm" %}
* **Rectangle deviceBounds**,  {% include w3api/param_description.html metodo=_data parametro="Rectangle deviceBounds" %}
* **Rectangle2D userBounds**,  {% include w3api/param_description.html metodo=_data parametro="Rectangle2D userBounds" %}
* **AffineTransform xform**,  {% include w3api/param_description.html metodo=_data parametro="AffineTransform xform" %}

## Clase Padre
[TexturePaint](/Java/TexturePaint/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TexturePaint.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
