---
title: StringBuilder.deleteCharAt()
permalink: /Java/StringBuilder/deleteCharAt/
date: 2021-01-11
key: Java.S.StringBuilder
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StringBuilder.metodos valor="deleteCharAt" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public StringBuilder deleteCharAt(int index)
~~~

## Parámetros
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}

## Excepciones
[StringIndexOutOfBoundsException](/Java/StringIndexOutOfBoundsException/)

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
