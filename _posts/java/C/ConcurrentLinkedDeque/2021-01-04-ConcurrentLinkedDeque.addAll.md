---
title: ConcurrentLinkedDeque.addAll()
permalink: Java/ConcurrentLinkedDeque/addAll
date: 2021-01-04
key: JavaJava.C.ConcurrentLinkedDeque
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentLinkedDeque.metodos valor="addAll" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean addAll(Collection<? extends E> c)
~~~

## Parámetros
* **Collection&lt;? extends E&gt; c**,  {% include w3api/param_description.html metodo=_data parametro="Collection<? extends E> c" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ConcurrentLinkedDeque](/Java/ConcurrentLinkedDeque/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ConcurrentLinkedDeque.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
