---
title: RowSorter.rowsInserted()
permalink: /Java/RowSorter/rowsInserted/
date: 2021-01-11
key: Java.R.RowSorter
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RowSorter.metodos valor="rowsInserted" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void rowsInserted(int firstRow, int endRow)
~~~

## Parámetros
* **int endRow**,  {% include w3api/param_description.html metodo=_dato parametro="int endRow" %}
* **int firstRow**,  {% include w3api/param_description.html metodo=_dato parametro="int firstRow" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/)

## Clase Padre
[RowSorter](/Java/RowSorter/)

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
