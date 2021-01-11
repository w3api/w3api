---
title: FilteredList.FilteredList()
permalink: Java/FilteredList/FilteredList
date: 2021-01-11
key: JavaJava.F.FilteredList
category: java
tags: ['java se', 'javafx.collections.transformation', 'javafx.base', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FilteredList.constructores valor="FilteredList" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public FilteredList(ObservableList<E> source)
public FilteredList(ObservableList<E> source, Predicate<? super E> predicate)
~~~

## Parámetros
* **ObservableList&lt;E&gt; source**,  {% include w3api/param_description.html metodo=_dato parametro="ObservableList<E> source" %}
* **Predicate&lt;? super E&gt; predicate**,  {% include w3api/param_description.html metodo=_dato parametro="Predicate<? super E> predicate" %}

## Clase Padre
[FilteredList](/Java/FilteredList/)

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
