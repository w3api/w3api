---
title: SetOfIntegerSyntax.SetOfIntegerSyntax()
permalink: Java/SetOfIntegerSyntax/SetOfIntegerSyntax
date: 2021-01-11
key: JavaJava.S.SetOfIntegerSyntax
category: java
tags: ['java se', 'javax.print.attribute', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SetOfIntegerSyntax.constructores valor="SetOfIntegerSyntax" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected SetOfIntegerSyntax(int member)
protected SetOfIntegerSyntax(int[][] members)
protected SetOfIntegerSyntax(int lowerBound, int upperBound)
protected SetOfIntegerSyntax(String members)
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
[SetOfIntegerSyntax](/Java/SetOfIntegerSyntax/)

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
