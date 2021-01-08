---
title: TableSelectionModel.selectRange()
permalink: Java/TableSelectionModel/selectRange
date: 2021-01-04
key: JavaJava.T.TableSelectionModel
category: java
tags: ['java se', 'javafx.scene.control', 'javafx.controls', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TableSelectionModel.metodos valor="selectRange" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void selectRange(int minRow, TableColumnBase<T,?> minColumn, int maxRow, TableColumnBase<T,?> maxColumn)
~~~

## Parámetros
* **?&gt; minColumn**,  {% include w3api/param_description.html metodo=_data parametro="?> minColumn" %}
* **?&gt; maxColumn**,  {% include w3api/param_description.html metodo=_data parametro="?> maxColumn" %}
* **int maxRow**,  {% include w3api/param_description.html metodo=_data parametro="int maxRow" %}
* **int minRow**,  {% include w3api/param_description.html metodo=_data parametro="int minRow" %}
* **TableColumnBase&lt;T**,  {% include w3api/param_description.html metodo=_data parametro="TableColumnBase<T" %}

## Clase Padre
[TableSelectionModel](/Java/TableSelectionModel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TableSelectionModel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
