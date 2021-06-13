---
title: NumberFormat.setRoundingMode()
permalink: Java/NumberFormat/setRoundingMode
date: 2021-01-11
key: JavaJava.N.NumberFormat
category: Java
tags: ['java se', 'java.text', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NumberFormat.metodos valor="setRoundingMode" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setRoundingMode(RoundingMode roundingMode)
~~~

## Parámetros
* **RoundingMode roundingMode**,  {% include w3api/param_description.html metodo=_dato parametro="RoundingMode roundingMode" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[NumberFormat](/Java/NumberFormat/)

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
