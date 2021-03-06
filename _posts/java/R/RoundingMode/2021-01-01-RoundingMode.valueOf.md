---
title: RoundingMode.valueOf()
permalink: /Java/RoundingMode/valueOf/
date: 2021-01-11
key: Java.R.RoundingMode
category: Java
tags: ['java se', 'java.math', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RoundingMode.metodos valor="valueOf" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static RoundingMode valueOf(int rm)
public static RoundingMode valueOf(String name)
~~~

## Parámetros
* **int rm**,  {% include w3api/param_description.html metodo=_dato parametro="int rm" %}
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[RoundingMode](/Java/RoundingMode/)

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
