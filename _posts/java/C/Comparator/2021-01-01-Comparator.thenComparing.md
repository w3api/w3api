---
title: Comparator.thenComparing()
permalink: /Java/Comparator/thenComparing/
date: 2021-01-11
key: Java.C.Comparator
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Comparator.metodos valor="thenComparing" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default Comparator<T> thenComparing(Comparator<? super T> other)
default <U extends Comparable<? super U>>Comparator<T> thenComparing(Function<? super T,? extends U> keyExtractor)
default <U> Comparator<T> thenComparing(Function<? super T,? extends U> keyExtractor, Comparator<? super U> keyComparator)
~~~

## Parámetros
* **Comparator&lt;? super U&gt; keyComparator**,  {% include w3api/param_description.html metodo=_dato parametro="Comparator<? super U> keyComparator" %}
* **? extends U&gt; keyExtractor**,  {% include w3api/param_description.html metodo=_dato parametro="? extends U> keyExtractor" %}
* **Function&lt;? super T**,  {% include w3api/param_description.html metodo=_dato parametro="Function<? super T" %}
* **Comparator&lt;? super T&gt; other**,  {% include w3api/param_description.html metodo=_dato parametro="Comparator<? super T> other" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Comparator](/Java/Comparator/)

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
