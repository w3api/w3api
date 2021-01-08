---
title: SetOfIntegerSyntax.SetOfIntegerSyntax()
permalink: Java/SetOfIntegerSyntax/SetOfIntegerSyntax
date: 2021-01-04
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
* **int lowerBound**,  {% include w3api/param_description.html metodo=_data parametro="int lowerBound" %}
* **int[][] members**,  {% include w3api/param_description.html metodo=_data parametro="int[][] members" %}
* **String members**,  {% include w3api/param_description.html metodo=_data parametro="String members" %}
* **int upperBound**,  {% include w3api/param_description.html metodo=_data parametro="int upperBound" %}
* **int member**,  {% include w3api/param_description.html metodo=_data parametro="int member" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[SetOfIntegerSyntax](/Java/SetOfIntegerSyntax/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SetOfIntegerSyntax.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
