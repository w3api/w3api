---
title: NumericShaper.shape()
permalink: Java/NumericShaper/shape
date: 2021-01-04
key: JavaJava.N.NumericShaper
category: java
tags: ['java se', 'java.awt.font', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NumericShaper.metodos valor="shape" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void shape(char[] text, int start, int count)
public void shape(char[] text, int start, int count, int context)
public void shape(char[] text, int start, int count, NumericShaper.Range context)
~~~

## Parámetros
* **int context**,  {% include w3api/param_description.html metodo=_data parametro="int context" %}
* **NumericShaper.Range context**,  {% include w3api/param_description.html metodo=_data parametro="NumericShaper.Range context" %}
* **char[] text**,  {% include w3api/param_description.html metodo=_data parametro="char[] text" %}
* **int start**,  {% include w3api/param_description.html metodo=_data parametro="int start" %}
* **int count**,  {% include w3api/param_description.html metodo=_data parametro="int count" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[NumericShaper](/Java/NumericShaper/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.N.NumericShaper.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
