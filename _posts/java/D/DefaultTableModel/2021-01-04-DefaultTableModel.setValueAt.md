---
title: DefaultTableModel.setValueAt()
permalink: Java/DefaultTableModel/setValueAt
date: 2021-01-04
key: JavaJava.D.DefaultTableModel
category: java
tags: ['java se', 'javax.swing.table', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DefaultTableModel.metodos valor="setValueAt" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setValueAt(Object aValue, int row, int column)
~~~

## Parámetros
* **int column**,  {% include w3api/param_description.html metodo=_data parametro="int column" %}
* **int row**,  {% include w3api/param_description.html metodo=_data parametro="int row" %}
* **Object aValue**,  {% include w3api/param_description.html metodo=_data parametro="Object aValue" %}

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
