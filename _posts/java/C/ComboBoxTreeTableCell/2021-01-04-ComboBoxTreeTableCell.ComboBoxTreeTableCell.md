---
title: ComboBoxTreeTableCell.ComboBoxTreeTableCell()
permalink: Java/ComboBoxTreeTableCell/ComboBoxTreeTableCell
date: 2021-01-04
key: JavaJava.C.ComboBoxTreeTableCell
category: java
tags: ['java se', 'javafx.scene.control.cell', 'javafx.controls', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ComboBoxTreeTableCell.constructores valor="ComboBoxTreeTableCell" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ComboBoxTreeTableCell()
public ComboBoxTreeTableCell(ObservableList<T> items)
public ComboBoxTreeTableCell(StringConverter<T> converter, ObservableList<T> items)
@SafeVarargs public ComboBoxTreeTableCell(StringConverter<T> converter, T... items)
@SafeVarargs public ComboBoxTreeTableCell(T... items)
~~~

## Parámetros
* **StringConverter&lt;T&gt; converter**,  {% include w3api/param_description.html metodo=_data parametro="StringConverter<T> converter" %}
* **ObservableList&lt;T&gt; items**,  {% include w3api/param_description.html metodo=_data parametro="ObservableList<T> items" %}
* **T... items**,  {% include w3api/param_description.html metodo=_data parametro="T... items" %}

## Clase Padre
[ComboBoxTreeTableCell](/Java/ComboBoxTreeTableCell/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ComboBoxTreeTableCell.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
