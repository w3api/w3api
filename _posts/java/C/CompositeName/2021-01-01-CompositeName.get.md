---
title: CompositeName.get()
permalink: Java/CompositeName/get
date: 2021-01-11
key: JavaJava.C.CompositeName
category: java
tags: ['java se', 'javax.naming', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompositeName.metodos valor="get" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public String get(int posn)
~~~

## Parámetros
* **int posn**,  {% include w3api/param_description.html metodo=_dato parametro="int posn" %}

## Excepciones
[ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/)

## Clase Padre
[CompositeName](/Java/CompositeName/)

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