---
title: TextMeasurer.getLineBreakIndex()
permalink: Java/TextMeasurer/getLineBreakIndex
date: 2021-01-11
key: JavaJava.T.TextMeasurer
category: java
tags: ['java se', 'java.awt.font', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TextMeasurer.metodos valor="getLineBreakIndex" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int getLineBreakIndex(int start, float maxAdvance)
~~~

## Parámetros
* **int start**,  {% include w3api/param_description.html metodo=_dato parametro="int start" %}
* **float maxAdvance**,  {% include w3api/param_description.html metodo=_dato parametro="float maxAdvance" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[TextMeasurer](/Java/TextMeasurer/)

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
