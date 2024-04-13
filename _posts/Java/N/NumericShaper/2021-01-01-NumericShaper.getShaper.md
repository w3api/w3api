---
title: NumericShaper.getShaper()
permalink: /Java/NumericShaper/getShaper/
date: 2021-01-11
key: Java.N.NumericShaper
category: Java
tags: ['java se', 'java.awt.font', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NumericShaper.metodos valor="getShaper" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static NumericShaper getShaper(int singleRange)
public static NumericShaper getShaper(NumericShaper.Range singleRange)
~~~

## Parámetros
* **NumericShaper.Range singleRange**,  {% include w3api/param_description.html metodo=_dato parametro="NumericShaper.Range singleRange" %}
* **int singleRange**,  {% include w3api/param_description.html metodo=_dato parametro="int singleRange" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

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
