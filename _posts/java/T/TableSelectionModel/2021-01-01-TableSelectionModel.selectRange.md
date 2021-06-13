---
title: TableSelectionModel.selectRange()
permalink: /Java/TableSelectionModel/selectRange/
date: 2021-01-11
key: Java.T.TableSelectionModel
category: Java
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
* **?&gt; minColumn**,  {% include w3api/param_description.html metodo=_dato parametro="?> minColumn" %}
* **?&gt; maxColumn**,  {% include w3api/param_description.html metodo=_dato parametro="?> maxColumn" %}
* **int minRow**,  {% include w3api/param_description.html metodo=_dato parametro="int minRow" %}
* **TableColumnBase&lt;T**,  {% include w3api/param_description.html metodo=_dato parametro="TableColumnBase<T" %}
* **int maxRow**,  {% include w3api/param_description.html metodo=_dato parametro="int maxRow" %}

## Clase Padre
[TableSelectionModel](/Java/TableSelectionModel/)

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
