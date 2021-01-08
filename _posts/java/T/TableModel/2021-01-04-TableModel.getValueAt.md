---
title: TableModel.getValueAt()
permalink: Java/TableModel/getValueAt
date: 2021-01-04
key: JavaJava.T.TableModel
category: java
tags: ['java se', 'javax.swing.table', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TableModel.metodos valor="getValueAt" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object getValueAt(int rowIndex, int columnIndex)
~~~

## Parámetros
* **int columnIndex**,  {% include w3api/param_description.html metodo=_data parametro="int columnIndex" %}
* **int rowIndex**,  {% include w3api/param_description.html metodo=_data parametro="int rowIndex" %}

## Clase Padre
[TableModel](/Java/TableModel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TableModel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
