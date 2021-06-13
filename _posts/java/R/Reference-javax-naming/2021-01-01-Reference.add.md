---
title: Reference.add()
permalink: Java/Reference-javax-naming/add
date: 2021-01-11
key: Java.R.Reference-javax-naming
category: java
tags: ['java se', 'javax.naming', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.Reference-javax-naming.metodos valor="add" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void add(int posn, RefAddr addr)
public void add(RefAddr addr)
~~~

## Parámetros
* **int posn**,  {% include w3api/param_description.html metodo=_dato parametro="int posn" %}
* **RefAddr addr**,  {% include w3api/param_description.html metodo=_dato parametro="RefAddr addr" %}

## Excepciones
[ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/)

## Clase Padre
[Reference](/Java/Reference-javax-naming/)

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
