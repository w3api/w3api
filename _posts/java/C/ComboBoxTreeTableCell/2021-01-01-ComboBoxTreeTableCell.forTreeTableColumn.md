---
title: ComboBoxTreeTableCell.forTreeTableColumn()
permalink: Java/ComboBoxTreeTableCell/forTreeTableColumn
date: 2021-01-11
key: JavaJava.C.ComboBoxTreeTableCell
category: java
tags: ['java se', 'javafx.scene.control.cell', 'javafx.controls', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ComboBoxTreeTableCell.metodos valor="forTreeTableColumn" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <S,T> Callback<TreeTableColumn<S,T>,TreeTableCell<S,T>> forTreeTableColumn(ObservableList<T> items)
static <S,T> Callback<TreeTableColumn<S,T>,TreeTableCell<S,T>> forTreeTableColumn(StringConverter<T> converter, ObservableList<T> items)
static <S,T> Callback<TreeTableColumn<S,T>,TreeTableCell<S,T>> forTreeTableColumn(StringConverter<T> converter, T... items)
static <S,T> Callback<TreeTableColumn<S,T>,TreeTableCell<S,T>> forTreeTableColumn(T... items)
~~~

## Parámetros
* **StringConverter&lt;T&gt; converter**,  {% include w3api/param_description.html metodo=_dato parametro="StringConverter<T> converter" %}
* **ObservableList&lt;T&gt; items**,  {% include w3api/param_description.html metodo=_dato parametro="ObservableList<T> items" %}
* **T... items**,  {% include w3api/param_description.html metodo=_dato parametro="T... items" %}

## Clase Padre
[ComboBoxTreeTableCell](/Java/ComboBoxTreeTableCell/)

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