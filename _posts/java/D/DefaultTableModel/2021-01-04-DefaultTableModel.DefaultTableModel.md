---
title: DefaultTableModel.DefaultTableModel()
permalink: Java/DefaultTableModel/DefaultTableModel
date: 2021-01-04
key: JavaJava.D.DefaultTableModel
category: java
tags: ['java se', 'javax.swing.table', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DefaultTableModel.constructores valor="DefaultTableModel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DefaultTableModel()
public DefaultTableModel(int rowCount, int columnCount)
public DefaultTableModel(Object[][] data, Object[] columnNames)
public DefaultTableModel(Object[] columnNames, int rowCount)
public DefaultTableModel(Vector<?> columnNames, int rowCount)
public DefaultTableModel(Vector<? extends Vector> data, Vector<?> columnNames)
~~~

## Parámetros
* **Vector&lt;?&gt; columnNames**,  {% include w3api/param_description.html metodo=_data parametro="Vector<?> columnNames" %}
* **Object[][] data**,  {% include w3api/param_description.html metodo=_data parametro="Object[][] data" %}
* **int columnCount**,  {% include w3api/param_description.html metodo=_data parametro="int columnCount" %}
* **Object[] columnNames**,  {% include w3api/param_description.html metodo=_data parametro="Object[] columnNames" %}
* **Vector&lt;? extends Vector&gt; data**,  {% include w3api/param_description.html metodo=_data parametro="Vector<? extends Vector> data" %}
* **int rowCount**,  {% include w3api/param_description.html metodo=_data parametro="int rowCount" %}

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
