---
title: ObservableList.filtered()
permalink: /Java/ObservableList/filtered/
date: 2021-01-11
key: JavaJava.O.ObservableList
category: java
tags: ['java se', 'javafx.collections', 'javafx.base', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObservableList.metodos valor="filtered" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default FilteredList<E> filtered(Predicate<E> predicate)
~~~

## Parámetros
* **Predicate&lt;E&gt; predicate**,  {% include w3api/param_description.html metodo=_dato parametro="Predicate<E> predicate" %}

## Clase Padre
[ObservableList](/Java/ObservableList/)

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
