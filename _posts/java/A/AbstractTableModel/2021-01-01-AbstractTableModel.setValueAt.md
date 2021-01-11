---
title: AbstractTableModel.setValueAt()
permalink: Java/AbstractTableModel/setValueAt
date: 2021-01-11
key: JavaJava.A.AbstractTableModel
category: java
tags: ['java se', 'javax.swing.table', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractTableModel.metodos valor="setValueAt" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setValueAt(Object aValue, int rowIndex, int columnIndex)
~~~

## Parámetros
* **int columnIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int columnIndex" %}
* **int rowIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int rowIndex" %}
* **Object aValue**,  {% include w3api/param_description.html metodo=_dato parametro="Object aValue" %}

## Clase Padre
[AbstractTableModel](/Java/AbstractTableModel/)

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
