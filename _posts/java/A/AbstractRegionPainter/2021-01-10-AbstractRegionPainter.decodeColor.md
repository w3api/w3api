---
title: AbstractRegionPainter.decodeColor()
permalink: Java/AbstractRegionPainter/decodeColor
date: 2021-01-10
key: JavaJava.A.AbstractRegionPainter
category: java
tags: ['java se', 'javax.swing.plaf.nimbus', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractRegionPainter.metodos valor="decodeColor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected Color decodeColor(Color color1, Color color2, float midPoint)
protected Color decodeColor(String key, float hOffset, float sOffset, float bOffset, int aOffset)
~~~

## Parámetros
* **float sOffset**,  {% include w3api/param_description.html metodo=_dato parametro="float sOffset" %}
* **float bOffset**,  {% include w3api/param_description.html metodo=_dato parametro="float bOffset" %}
* **String key**,  {% include w3api/param_description.html metodo=_dato parametro="String key" %}
* **float midPoint**,  {% include w3api/param_description.html metodo=_dato parametro="float midPoint" %}
* **Color color2**,  {% include w3api/param_description.html metodo=_dato parametro="Color color2" %}
* **int aOffset**,  {% include w3api/param_description.html metodo=_dato parametro="int aOffset" %}
* **float hOffset**,  {% include w3api/param_description.html metodo=_dato parametro="float hOffset" %}
* **Color color1**,  {% include w3api/param_description.html metodo=_dato parametro="Color color1" %}

## Clase Padre
[AbstractRegionPainter](/Java/AbstractRegionPainter/)

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
