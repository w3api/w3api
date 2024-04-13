---
title: CheckBoxTableCell.CheckBoxTableCell()
permalink: /Java/CheckBoxTableCell/CheckBoxTableCell/
date: 2021-01-11
key: Java.C.CheckBoxTableCell
category: Java
tags: ['java se', 'javafx.scene.control.cell', 'javafx.controls', 'metodo java', 'JavaFX 2.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CheckBoxTableCell.constructores valor="CheckBoxTableCell" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public CheckBoxTableCell()
public CheckBoxTableCell(Callback<Integer,ObservableValue<Boolean>> getSelectedProperty)
public CheckBoxTableCell(Callback<Integer,ObservableValue<Boolean>> getSelectedProperty, StringConverter<T> converter)
~~~

## Parámetros
* **Callback&lt;Integer**,  {% include w3api/param_description.html metodo=_dato parametro="Callback<Integer" %}
* **StringConverter&lt;T&gt; converter**,  {% include w3api/param_description.html metodo=_dato parametro="StringConverter<T> converter" %}
* **ObservableValue&lt;Boolean&gt;&gt; getSelectedProperty**,  {% include w3api/param_description.html metodo=_dato parametro="ObservableValue<Boolean>> getSelectedProperty" %}

## Clase Padre
[CheckBoxTableCell](/Java/CheckBoxTableCell/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
