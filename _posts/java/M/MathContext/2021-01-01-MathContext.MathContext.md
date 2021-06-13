---
title: MathContext.MathContext()
permalink: Java/MathContext/MathContext
date: 2021-01-11
key: JavaJava.M.MathContext
category: Java
tags: ['java se', 'java.math', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MathContext.constructores valor="MathContext" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MathContext(int setPrecision)
public MathContext(int setPrecision, RoundingMode setRoundingMode)
public MathContext(String val)
~~~

## Parámetros
* **String val**,  {% include w3api/param_description.html metodo=_dato parametro="String val" %}
* **int setPrecision**,  {% include w3api/param_description.html metodo=_dato parametro="int setPrecision" %}
* **RoundingMode setRoundingMode**,  {% include w3api/param_description.html metodo=_dato parametro="RoundingMode setRoundingMode" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[MathContext](/Java/MathContext/)

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
