---
title: DefaultTableModel.getValueAt()
permalink: /Java/DefaultTableModel/getValueAt/
date: 2021-01-11
key: Java.D.DefaultTableModel
category: Java
tags: ['java se', 'javax.swing.table', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DefaultTableModel.metodos valor="getValueAt" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object getValueAt(int row, int column)
~~~

## Parámetros
* **int column**,  {% include w3api/param_description.html metodo=_dato parametro="int column" %}
* **int row**,  {% include w3api/param_description.html metodo=_dato parametro="int row" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
