---
title: NumericShaper.shape()
permalink: /Java/NumericShaper/shape/
date: 2021-01-11
key: Java.N.NumericShaper
category: Java
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
* **char[] text**,  {% include w3api/param_description.html metodo=_dato parametro="char[] text" %}
* **NumericShaper.Range context**,  {% include w3api/param_description.html metodo=_dato parametro="NumericShaper.Range context" %}
* **int context**,  {% include w3api/param_description.html metodo=_dato parametro="int context" %}
* **int count**,  {% include w3api/param_description.html metodo=_dato parametro="int count" %}
* **int start**,  {% include w3api/param_description.html metodo=_dato parametro="int start" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[NumericShaper](/Java/NumericShaper/)

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
