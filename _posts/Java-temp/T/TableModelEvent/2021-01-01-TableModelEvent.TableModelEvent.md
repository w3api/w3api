---
title: TableModelEvent.TableModelEvent()
permalink: /Java/TableModelEvent/TableModelEvent/
date: 2021-01-11
key: Java.T.TableModelEvent
category: Java
tags: ['java se', 'javax.swing.event', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TableModelEvent.constructores valor="TableModelEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public TableModelEvent(TableModel source)
public TableModelEvent(TableModel source, int row)
public TableModelEvent(TableModel source, int firstRow, int lastRow)
public TableModelEvent(TableModel source, int firstRow, int lastRow, int column)
public TableModelEvent(TableModel source, int firstRow, int lastRow, int column, int type)
~~~

## Parámetros
* **int column**,  {% include w3api/param_description.html metodo=_dato parametro="int column" %}
* **int lastRow**,  {% include w3api/param_description.html metodo=_dato parametro="int lastRow" %}
* **int type**,  {% include w3api/param_description.html metodo=_dato parametro="int type" %}
* **TableModel source**,  {% include w3api/param_description.html metodo=_dato parametro="TableModel source" %}
* **int row**,  {% include w3api/param_description.html metodo=_dato parametro="int row" %}
* **int firstRow**,  {% include w3api/param_description.html metodo=_dato parametro="int firstRow" %}

## Clase Padre
[TableModelEvent](/Java/TableModelEvent/)

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
