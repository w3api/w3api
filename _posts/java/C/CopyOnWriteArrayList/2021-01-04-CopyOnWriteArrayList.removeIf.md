---
title: CopyOnWriteArrayList.removeIf()
permalink: Java/CopyOnWriteArrayList/removeIf
date: 2021-01-04
key: JavaJava.C.CopyOnWriteArrayList
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CopyOnWriteArrayList.metodos valor="removeIf" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean removeIf(Predicate<? super E> filter)
~~~

## Parámetros
* **Predicate&lt;? super E&gt; filter**,  {% include w3api/param_description.html metodo=_data parametro="Predicate<? super E> filter" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[CopyOnWriteArrayList](/Java/CopyOnWriteArrayList/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CopyOnWriteArrayList.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
