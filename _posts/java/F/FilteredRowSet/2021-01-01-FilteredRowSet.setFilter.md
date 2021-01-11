---
title: FilteredRowSet.setFilter()
permalink: Java/FilteredRowSet/setFilter
date: 2021-01-11
key: JavaJava.F.FilteredRowSet
category: java
tags: ['java se', 'javax.sql.rowset', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FilteredRowSet.metodos valor="setFilter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setFilter(Predicate p) throws SQLException
~~~

## Parámetros
* **Predicate p**,  {% include w3api/param_description.html metodo=_dato parametro="Predicate p" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[FilteredRowSet](/Java/FilteredRowSet/)

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
