---
title: IntegerSyntax.IntegerSyntax()
permalink: /Java/IntegerSyntax/IntegerSyntax/
date: 2021-01-11
key: Java.I.IntegerSyntax
category: Java
tags: ['java se', 'javax.print.attribute', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IntegerSyntax.constructores valor="IntegerSyntax" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected IntegerSyntax(int value)
protected IntegerSyntax(int value, int lowerBound, int upperBound)
~~~

## Parámetros
* **int value**,  {% include w3api/param_description.html metodo=_dato parametro="int value" %}
* **int upperBound**,  {% include w3api/param_description.html metodo=_dato parametro="int upperBound" %}
* **int lowerBound**,  {% include w3api/param_description.html metodo=_dato parametro="int lowerBound" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[IntegerSyntax](/Java/IntegerSyntax/)

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
