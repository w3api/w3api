---
title: CheckBoxTreeTableCell.CheckBoxTreeTableCell()
permalink: /Java/CheckBoxTreeTableCell/CheckBoxTreeTableCell/
date: 2021-01-11
key: Java.C.CheckBoxTreeTableCell
category: Java
tags: ['java se', 'javafx.scene.control.cell', 'javafx.controls', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CheckBoxTreeTableCell.constructores valor="CheckBoxTreeTableCell" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public CheckBoxTreeTableCell()
public CheckBoxTreeTableCell(Callback<Integer,ObservableValue<Boolean>> getSelectedProperty)
public CheckBoxTreeTableCell(Callback<Integer,ObservableValue<Boolean>> getSelectedProperty, StringConverter<T> converter)
~~~

## Parámetros
* **Callback&lt;Integer**,  {% include w3api/param_description.html metodo=_dato parametro="Callback<Integer" %}
* **StringConverter&lt;T&gt; converter**,  {% include w3api/param_description.html metodo=_dato parametro="StringConverter<T> converter" %}
* **ObservableValue&lt;Boolean&gt;&gt; getSelectedProperty**,  {% include w3api/param_description.html metodo=_dato parametro="ObservableValue<Boolean>> getSelectedProperty" %}

## Clase Padre
[CheckBoxTreeTableCell](/Java/CheckBoxTreeTableCell/)

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
