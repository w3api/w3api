---
title: ComboBoxListCell.ComboBoxListCell()
permalink: /Java/ComboBoxListCell/ComboBoxListCell/
date: 2021-01-11
key: Java.C.ComboBoxListCell
category: Java
tags: ['java se', 'javafx.scene.control.cell', 'javafx.controls', 'metodo java', 'JavaFX 2.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ComboBoxListCell.constructores valor="ComboBoxListCell" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ComboBoxListCell()
public ComboBoxListCell(ObservableList<T> items)
public ComboBoxListCell(StringConverter<T> converter, ObservableList<T> items)
@SafeVarargs public ComboBoxListCell(StringConverter<T> converter, T... items)
@SafeVarargs public ComboBoxListCell(T... items)
~~~

## Parámetros
* **StringConverter&lt;T&gt; converter**,  {% include w3api/param_description.html metodo=_dato parametro="StringConverter<T> converter" %}
* **ObservableList&lt;T&gt; items**,  {% include w3api/param_description.html metodo=_dato parametro="ObservableList<T> items" %}
* **T... items**,  {% include w3api/param_description.html metodo=_dato parametro="T... items" %}

## Clase Padre
[ComboBoxListCell](/Java/ComboBoxListCell/)

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
