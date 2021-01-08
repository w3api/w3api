---
title: FontRenderContext.FontRenderContext()
permalink: Java/FontRenderContext/FontRenderContext
date: 2021-01-04
key: JavaJava.F.FontRenderContext
category: java
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
* **AffineTransform tx**,  {% include w3api/param_description.html metodo=_data parametro="AffineTransform tx" %}
* **Object aaHint**,  {% include w3api/param_description.html metodo=_data parametro="Object aaHint" %}
* **Object fmHint**,  {% include w3api/param_description.html metodo=_data parametro="Object fmHint" %}
* **boolean usesFractionalMetrics**,  {% include w3api/param_description.html metodo=_data parametro="boolean usesFractionalMetrics" %}
* **boolean isAntiAliased**,  {% include w3api/param_description.html metodo=_data parametro="boolean isAntiAliased" %}

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
{%- for _ldc in site.data.Java.F.FontRenderContext.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
