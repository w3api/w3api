---
title: ArrayDeque.removeIf()
permalink: /Java/ArrayDeque/removeIf/
date: 2021-01-11
key: Java.A.ArrayDeque
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.ArrayDeque.metodos valor="removeIf" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean removeIf(Predicate<? super E> filter)
~~~

## Parámetros
* **Predicate&lt;? super E&gt; filter**,  {% include w3api/param_description.html metodo=_dato parametro="Predicate<? super E> filter" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ArrayDeque](/Java/ArrayDeque/)

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
