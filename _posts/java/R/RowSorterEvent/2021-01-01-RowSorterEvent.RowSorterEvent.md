---
title: RowSorterEvent.RowSorterEvent()
permalink: /Java/RowSorterEvent/RowSorterEvent/
date: 2021-01-11
key: Java.R.RowSorterEvent
category: Java
tags: ['java se', 'javax.swing.event', 'java.desktop', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RowSorterEvent.constructores valor="RowSorterEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public RowSorterEvent(RowSorter<?> source)
public RowSorterEvent(RowSorter<?> source, RowSorterEvent.Type type, int[] previousRowIndexToModel)
~~~

## Parámetros
* **int[] previousRowIndexToModel**,  {% include w3api/param_description.html metodo=_dato parametro="int[] previousRowIndexToModel" %}
* **RowSorter&lt;?&gt; source**,  {% include w3api/param_description.html metodo=_dato parametro="RowSorter<?> source" %}
* **RowSorterEvent.Type type**,  {% include w3api/param_description.html metodo=_dato parametro="RowSorterEvent.Type type" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[RowSorterEvent](/Java/RowSorterEvent/)

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
