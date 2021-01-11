---
title: DefaultTableModel.addColumn()
permalink: Java/DefaultTableModel/addColumn
date: 2021-01-11
key: JavaJava.D.DefaultTableModel
category: java
tags: ['java se', 'javax.swing.table', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DefaultTableModel.metodos valor="addColumn" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void addColumn(Object columnName)
public void addColumn(Object columnName, Object[] columnData)
public void addColumn(Object columnName, Vector<?> columnData)
~~~

## Parámetros
* **Object columnName**,  {% include w3api/param_description.html metodo=_dato parametro="Object columnName" %}
* **Object[] columnData**,  {% include w3api/param_description.html metodo=_dato parametro="Object[] columnData" %}
* **Vector&lt;?&gt; columnData**,  {% include w3api/param_description.html metodo=_dato parametro="Vector<?> columnData" %}

## Clase Padre
[DefaultTableModel](/Java/DefaultTableModel/)

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
