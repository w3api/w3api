---
title: Utilities.getBreakLocation()
permalink: Java/Utilities/getBreakLocation
date: 2021-01-04
key: JavaJava.U.Utilities
category: java
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
* **float x**,  {% include w3api/param_description.html metodo=_data parametro="float x" %}
* **TabExpander e**,  {% include w3api/param_description.html metodo=_data parametro="TabExpander e" %}
* **int startOffset**,  {% include w3api/param_description.html metodo=_data parametro="int startOffset" %}
* **int x0**,  {% include w3api/param_description.html metodo=_data parametro="int x0" %}
* **float x0**,  {% include w3api/param_description.html metodo=_data parametro="float x0" %}
* **Segment s**,  {% include w3api/param_description.html metodo=_data parametro="Segment s" %}
* **FontMetrics metrics**,  {% include w3api/param_description.html metodo=_data parametro="FontMetrics metrics" %}
* **int x**,  {% include w3api/param_description.html metodo=_data parametro="int x" %}

## Clase Padre
[Utilities](/Java/Utilities/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.U.Utilities.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
