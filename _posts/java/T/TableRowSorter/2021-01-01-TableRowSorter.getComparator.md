---
title: TableRowSorter.getComparator()
permalink: /Java/TableRowSorter/getComparator/
date: 2021-01-11
key: Java.T.TableRowSorter
category: Java
tags: ['java se', 'javax.swing.table', 'java.desktop', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TableRowSorter.metodos valor="getComparator" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Comparator<?> getComparator(int column)
~~~

## Parámetros
* **int column**,  {% include w3api/param_description.html metodo=_dato parametro="int column" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/)

## Clase Padre
[TableRowSorter](/Java/TableRowSorter/)

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
