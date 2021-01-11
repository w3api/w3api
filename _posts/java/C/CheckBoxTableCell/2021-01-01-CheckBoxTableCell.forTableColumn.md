---
title: CheckBoxTableCell.forTableColumn()
permalink: Java/CheckBoxTableCell/forTableColumn
date: 2021-01-11
key: JavaJava.C.CheckBoxTableCell
category: java
tags: ['java se', 'javafx.scene.control.cell', 'javafx.controls', 'metodo java', 'JavaFX 2.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CheckBoxTableCell.metodos valor="forTableColumn" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <S> Callback<TableColumn<S,Boolean>,TableCell<S,Boolean>> forTableColumn(TableColumn<S,Boolean> column)
static <S,T> Callback<TableColumn<S,T>,TableCell<S,T>> forTableColumn(Callback<Integer,ObservableValue<Boolean>> getSelectedProperty)
static <S,T> Callback<TableColumn<S,T>,TableCell<S,T>> forTableColumn(Callback<Integer,ObservableValue<Boolean>> getSelectedProperty, boolean showLabel)
static <S,T> Callback<TableColumn<S,T>,TableCell<S,T>> forTableColumn(Callback<Integer,ObservableValue<Boolean>> getSelectedProperty, StringConverter<T> converter)
~~~

## Parámetros
* **StringConverter&lt;T&gt; converter**,  {% include w3api/param_description.html metodo=_dato parametro="StringConverter<T> converter" %}
* **ObservableValue&lt;Boolean&gt;&gt; getSelectedProperty**,  {% include w3api/param_description.html metodo=_dato parametro="ObservableValue<Boolean>> getSelectedProperty" %}
* **TableColumn&lt;S**,  {% include w3api/param_description.html metodo=_dato parametro="TableColumn<S" %}
* **Boolean&gt; column**,  {% include w3api/param_description.html metodo=_dato parametro="Boolean> column" %}
* **boolean showLabel**,  {% include w3api/param_description.html metodo=_dato parametro="boolean showLabel" %}
* **Callback&lt;Integer**,  {% include w3api/param_description.html metodo=_dato parametro="Callback<Integer" %}

## Clase Padre
[CheckBoxTableCell](/Java/CheckBoxTableCell/)

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
