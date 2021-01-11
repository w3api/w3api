---
title: ComboBoxTableCell.ComboBoxTableCell()
permalink: Java/ComboBoxTableCell/ComboBoxTableCell
date: 2021-01-11
key: JavaJava.C.ComboBoxTableCell
category: java
tags: ['java se', 'javafx.scene.control.cell', 'javafx.controls', 'metodo java', 'JavaFX 2.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ComboBoxTableCell.constructores valor="ComboBoxTableCell" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ComboBoxTableCell()
public ComboBoxTableCell(ObservableList<T> items)
public ComboBoxTableCell(StringConverter<T> converter, ObservableList<T> items)
@SafeVarargs public ComboBoxTableCell(StringConverter<T> converter, T... items)
@SafeVarargs public ComboBoxTableCell(T... items)
~~~

## Parámetros
* **StringConverter&lt;T&gt; converter**,  {% include w3api/param_description.html metodo=_dato parametro="StringConverter<T> converter" %}
* **ObservableList&lt;T&gt; items**,  {% include w3api/param_description.html metodo=_dato parametro="ObservableList<T> items" %}
* **T... items**,  {% include w3api/param_description.html metodo=_dato parametro="T... items" %}

## Clase Padre
[ComboBoxTableCell](/Java/ComboBoxTableCell/)

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
