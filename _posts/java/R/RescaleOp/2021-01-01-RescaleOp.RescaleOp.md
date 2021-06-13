---
title: RescaleOp.RescaleOp()
permalink: /Java/RescaleOp/RescaleOp/
date: 2021-01-11
key: Java.R.RescaleOp
category: Java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RescaleOp.constructores valor="RescaleOp" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public RescaleOp(float[] scaleFactors, float[] offsets, RenderingHints hints)
public RescaleOp(float scaleFactor, float offset, RenderingHints hints)
~~~

## Parámetros
* **float scaleFactor**,  {% include w3api/param_description.html metodo=_dato parametro="float scaleFactor" %}
* **float[] offsets**,  {% include w3api/param_description.html metodo=_dato parametro="float[] offsets" %}
* **float[] scaleFactors**,  {% include w3api/param_description.html metodo=_dato parametro="float[] scaleFactors" %}
* **float offset**,  {% include w3api/param_description.html metodo=_dato parametro="float offset" %}
* **RenderingHints hints**,  {% include w3api/param_description.html metodo=_dato parametro="RenderingHints hints" %}

## Clase Padre
[RescaleOp](/Java/RescaleOp/)

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
