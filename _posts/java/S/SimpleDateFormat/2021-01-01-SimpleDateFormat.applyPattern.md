---
title: SimpleDateFormat.applyPattern()
permalink: Java/SimpleDateFormat/applyPattern
date: 2021-01-11
key: JavaJava.S.SimpleDateFormat
category: java
tags: ['java se', 'java.text', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SimpleDateFormat.metodos valor="applyPattern" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void applyPattern(String pattern)
~~~

## Parámetros
* **String pattern**,  {% include w3api/param_description.html metodo=_dato parametro="String pattern" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[SimpleDateFormat](/Java/SimpleDateFormat/)

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