---
title: CopyOnWriteArraySet.removeIf()
permalink: Java/CopyOnWriteArraySet/removeIf
date: 2021-01-11
key: JavaJava.C.CopyOnWriteArraySet
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CopyOnWriteArraySet.metodos valor="removeIf" %}

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
[CopyOnWriteArraySet](/Java/CopyOnWriteArraySet/)

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
