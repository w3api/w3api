---
title: NumberFormat.setCurrency()
permalink: Java/NumberFormat/setCurrency
date: 2021-01-04
key: JavaJava.N.NumberFormat
category: java
tags: ['java se', 'java.text', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NumberFormat.metodos valor="setCurrency" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setCurrency(Currency currency)
~~~

## Parámetros
* **Currency currency**,  {% include w3api/param_description.html metodo=_data parametro="Currency currency" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[NumberFormat](/Java/NumberFormat/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.N.NumberFormat.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
