---
title: RenderContext.RenderContext()
permalink: Java/RenderContext/RenderContext
date: 2021-01-11
key: JavaJava.R.RenderContext
category: java
tags: ['java se', 'java.awt.image.renderable', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RenderContext.constructores valor="RenderContext" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public RenderContext(AffineTransform usr2dev)
public RenderContext(AffineTransform usr2dev, RenderingHints hints)
public RenderContext(AffineTransform usr2dev, Shape aoi)
public RenderContext(AffineTransform usr2dev, Shape aoi, RenderingHints hints)
~~~

## Parámetros
* **AffineTransform usr2dev**,  {% include w3api/param_description.html metodo=_dato parametro="AffineTransform usr2dev" %}
* **Shape aoi**,  {% include w3api/param_description.html metodo=_dato parametro="Shape aoi" %}
* **RenderingHints hints**,  {% include w3api/param_description.html metodo=_dato parametro="RenderingHints hints" %}

## Clase Padre
[RenderContext](/Java/RenderContext/)

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
