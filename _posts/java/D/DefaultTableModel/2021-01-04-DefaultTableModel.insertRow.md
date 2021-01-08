---
title: DefaultTableModel.insertRow()
permalink: Java/DefaultTableModel/insertRow
date: 2021-01-04
key: JavaJava.D.DefaultTableModel
category: java
tags: ['java se', 'javax.swing.table', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DefaultTableModel.metodos valor="insertRow" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void insertRow(int row, Object[] rowData)
public void insertRow(int row, Vector<?> rowData)
~~~

## Parámetros
* **Vector&lt;?&gt; rowData**,  {% include w3api/param_description.html metodo=_data parametro="Vector<?> rowData" %}
* **int row**,  {% include w3api/param_description.html metodo=_data parametro="int row" %}
* **Object[] rowData**,  {% include w3api/param_description.html metodo=_data parametro="Object[] rowData" %}

## Excepciones
[ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/)

## Clase Padre
[DefaultTableModel](/Java/DefaultTableModel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DefaultTableModel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
