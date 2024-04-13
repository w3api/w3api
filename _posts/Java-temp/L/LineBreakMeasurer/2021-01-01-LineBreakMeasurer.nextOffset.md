---
title: LineBreakMeasurer.nextOffset()
permalink: /Java/LineBreakMeasurer/nextOffset/
date: 2021-01-11
key: Java.L.LineBreakMeasurer
category: Java
tags: ['java se', 'java.awt.font', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LineBreakMeasurer.metodos valor="nextOffset" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int nextOffset(float wrappingWidth)
public int nextOffset(float wrappingWidth, int offsetLimit, boolean requireNextWord)
~~~

## Parámetros
* **float wrappingWidth**,  {% include w3api/param_description.html metodo=_dato parametro="float wrappingWidth" %}
* **boolean requireNextWord**,  {% include w3api/param_description.html metodo=_dato parametro="boolean requireNextWord" %}
* **int offsetLimit**,  {% include w3api/param_description.html metodo=_dato parametro="int offsetLimit" %}

## Clase Padre
[LineBreakMeasurer](/Java/LineBreakMeasurer/)

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
