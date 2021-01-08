---
title: TableModelEvent.TableModelEvent()
permalink: Java/TableModelEvent/TableModelEvent
date: 2021-01-04
key: JavaJava.T.TableModelEvent
category: java
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
* **int type**,  {% include w3api/param_description.html metodo=_data parametro="int type" %}
* **int row**,  {% include w3api/param_description.html metodo=_data parametro="int row" %}
* **int column**,  {% include w3api/param_description.html metodo=_data parametro="int column" %}
* **int lastRow**,  {% include w3api/param_description.html metodo=_data parametro="int lastRow" %}
* **TableModel source**,  {% include w3api/param_description.html metodo=_data parametro="TableModel source" %}
* **int firstRow**,  {% include w3api/param_description.html metodo=_data parametro="int firstRow" %}

## Clase Padre
[TableModelEvent](/Java/TableModelEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TableModelEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
