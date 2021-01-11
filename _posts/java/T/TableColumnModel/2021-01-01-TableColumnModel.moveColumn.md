---
title: TableColumnModel.moveColumn()
permalink: Java/TableColumnModel/moveColumn
date: 2021-01-11
key: JavaJava.T.TableColumnModel
category: java
tags: ['java se', 'javax.swing.table', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TableColumnModel.metodos valor="moveColumn" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void moveColumn(int columnIndex, int newIndex)
~~~

## Parámetros
* **int columnIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int columnIndex" %}
* **int newIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int newIndex" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[TableColumnModel](/Java/TableColumnModel/)

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
