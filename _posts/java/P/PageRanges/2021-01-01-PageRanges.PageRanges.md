---
title: PageRanges.PageRanges()
permalink: /Java/PageRanges/PageRanges/
date: 2021-01-11
key: Java.P.PageRanges
category: java
tags: ['java se', 'javax.print.attribute.standard', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PageRanges.constructores valor="PageRanges" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PageRanges(int member)
public PageRanges(int[][] members)
public PageRanges(int lowerBound, int upperBound)
public PageRanges(String members)
~~~

## Parámetros
* **int member**,  {% include w3api/param_description.html metodo=_dato parametro="int member" %}
* **int[][] members**,  {% include w3api/param_description.html metodo=_dato parametro="int[][] members" %}
* **int upperBound**,  {% include w3api/param_description.html metodo=_dato parametro="int upperBound" %}
* **int lowerBound**,  {% include w3api/param_description.html metodo=_dato parametro="int lowerBound" %}
* **String members**,  {% include w3api/param_description.html metodo=_dato parametro="String members" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[PageRanges](/Java/PageRanges/)

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
