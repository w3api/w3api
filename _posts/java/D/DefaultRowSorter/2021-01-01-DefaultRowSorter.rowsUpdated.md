---
title: DefaultRowSorter.rowsUpdated()
permalink: /Java/DefaultRowSorter/rowsUpdated/
date: 2021-01-11
key: Java.D.DefaultRowSorter
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DefaultRowSorter.metodos valor="rowsUpdated" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void rowsUpdated(int firstRow, int endRow)
public void rowsUpdated(int firstRow, int endRow, int column)
~~~

## Parámetros
* **int column**,  {% include w3api/param_description.html metodo=_dato parametro="int column" %}
* **int endRow**,  {% include w3api/param_description.html metodo=_dato parametro="int endRow" %}
* **int firstRow**,  {% include w3api/param_description.html metodo=_dato parametro="int firstRow" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/)

## Clase Padre
[DefaultRowSorter](/Java/DefaultRowSorter/)

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
