---
title: SortedList.SortedList()
permalink: /Java/SortedList/SortedList/
date: 2021-01-11
key: Java.S.SortedList
category: Java
tags: ['java se', 'javafx.collections.transformation', 'javafx.base', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SortedList.constructores valor="SortedList" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SortedList(ObservableList<? extends E> source)
public SortedList(ObservableList<? extends E> source, Comparator<? super E> comparator)
~~~

## Parámetros
* **Comparator&lt;? super E&gt; comparator**,  {% include w3api/param_description.html metodo=_dato parametro="Comparator<? super E> comparator" %}
* **ObservableList&lt;? extends E&gt; source**,  {% include w3api/param_description.html metodo=_dato parametro="ObservableList<? extends E> source" %}

## Clase Padre
[SortedList](/Java/SortedList/)

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
