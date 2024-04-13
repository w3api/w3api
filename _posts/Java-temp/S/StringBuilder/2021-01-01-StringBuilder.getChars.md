---
title: StringBuilder.getChars()
permalink: /Java/StringBuilder/getChars/
date: 2021-01-11
key: Java.S.StringBuilder
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StringBuilder.metodos valor="getChars" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void getChars(int srcBegin, int srcEnd, char[] dst, int dstBegin)
~~~

## Parámetros
* **int dstBegin**,  {% include w3api/param_description.html metodo=_dato parametro="int dstBegin" %}
* **char[] dst**,  {% include w3api/param_description.html metodo=_dato parametro="char[] dst" %}
* **int srcEnd**,  {% include w3api/param_description.html metodo=_dato parametro="int srcEnd" %}
* **int srcBegin**,  {% include w3api/param_description.html metodo=_dato parametro="int srcBegin" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/)

## Clase Padre
[StringBuilder](/Java/StringBuilder/)

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
