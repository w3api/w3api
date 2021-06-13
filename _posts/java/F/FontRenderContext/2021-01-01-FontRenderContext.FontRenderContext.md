---
title: FontRenderContext.FontRenderContext()
permalink: /Java/FontRenderContext/FontRenderContext/
date: 2021-01-11
key: Java.F.FontRenderContext
category: Java
tags: ['java se', 'java.awt.font', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FontRenderContext.constructores valor="FontRenderContext" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected FontRenderContext()
public FontRenderContext(AffineTransform tx, boolean isAntiAliased, boolean usesFractionalMetrics)
public FontRenderContext(AffineTransform tx, Object aaHint, Object fmHint)
~~~

## Parámetros
* **Object fmHint**,  {% include w3api/param_description.html metodo=_dato parametro="Object fmHint" %}
* **boolean isAntiAliased**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isAntiAliased" %}
* **Object aaHint**,  {% include w3api/param_description.html metodo=_dato parametro="Object aaHint" %}
* **boolean usesFractionalMetrics**,  {% include w3api/param_description.html metodo=_dato parametro="boolean usesFractionalMetrics" %}
* **AffineTransform tx**,  {% include w3api/param_description.html metodo=_dato parametro="AffineTransform tx" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[FontRenderContext](/Java/FontRenderContext/)

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
