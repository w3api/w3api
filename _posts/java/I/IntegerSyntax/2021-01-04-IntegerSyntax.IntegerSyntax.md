---
title: IntegerSyntax.IntegerSyntax()
permalink: Java/IntegerSyntax/IntegerSyntax
date: 2021-01-04
key: JavaJava.I.IntegerSyntax
category: java
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
* **int upperBound**,  {% include w3api/param_description.html metodo=_data parametro="int upperBound" %}
* **int lowerBound**,  {% include w3api/param_description.html metodo=_data parametro="int lowerBound" %}
* **int value**,  {% include w3api/param_description.html metodo=_data parametro="int value" %}

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
{%- for _ldc in site.data.Java.I.IntegerSyntax.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
