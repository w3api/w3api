---
title: Utilities.getBreakLocation()
permalink: /Java/Utilities/getBreakLocation/
date: 2021-01-11
key: Java.U.Utilities
category: Java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.Utilities.metodos valor="getBreakLocation" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static int getBreakLocation(Segment s, FontMetrics metrics, float x0, float x, TabExpander e, int startOffset)
static int getBreakLocation(Segment s, FontMetrics metrics, int x0, int x, TabExpander e, int startOffset)
~~~

## Parámetros
* **Segment s**,  {% include w3api/param_description.html metodo=_dato parametro="Segment s" %}
* **float x0**,  {% include w3api/param_description.html metodo=_dato parametro="float x0" %}
* **int startOffset**,  {% include w3api/param_description.html metodo=_dato parametro="int startOffset" %}
* **float x**,  {% include w3api/param_description.html metodo=_dato parametro="float x" %}
* **int x0**,  {% include w3api/param_description.html metodo=_dato parametro="int x0" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **TabExpander e**,  {% include w3api/param_description.html metodo=_dato parametro="TabExpander e" %}
* **FontMetrics metrics**,  {% include w3api/param_description.html metodo=_dato parametro="FontMetrics metrics" %}

## Clase Padre
[Utilities](/Java/Utilities/)

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
