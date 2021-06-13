---
title: TableModel.isCellEditable()
permalink: Java/TableModel/isCellEditable
date: 2021-01-11
key: JavaJava.T.TableModel
category: java
tags: ['java se', 'javax.swing.table', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TableModel.metodos valor="isCellEditable" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean isCellEditable(int rowIndex, int columnIndex)
~~~

## Parámetros
* **int columnIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int columnIndex" %}
* **int rowIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int rowIndex" %}

## Clase Padre
[TableModel](/Java/TableModel/)

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