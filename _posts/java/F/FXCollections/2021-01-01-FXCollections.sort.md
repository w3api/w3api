---
title: FXCollections.sort()
permalink: Java/FXCollections/sort
date: 2021-01-11
key: JavaJava.F.FXCollections
category: java
tags: ['java se', 'javafx.collections', 'javafx.base', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FXCollections.metodos valor="sort" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T extends Comparable<? super T>>void sort(ObservableList<T> list)
static <T> void sort(ObservableList<T> list, Comparator<? super T> c)
~~~

## Parámetros
* **ObservableList&lt;T&gt; list**,  {% include w3api/param_description.html metodo=_dato parametro="ObservableList<T> list" %}
* **Comparator&lt;? super T&gt; c**,  {% include w3api/param_description.html metodo=_dato parametro="Comparator<? super T> c" %}

## Clase Padre
[FXCollections](/Java/FXCollections/)

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
