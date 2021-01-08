---
title: CheckBoxTableCell.CheckBoxTableCell()
permalink: Java/CheckBoxTableCell/CheckBoxTableCell
date: 2021-01-04
key: JavaJava.C.CheckBoxTableCell
category: java
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
* **ObservableValue&lt;Boolean&gt;&gt; getSelectedProperty**,  {% include w3api/param_description.html metodo=_data parametro="ObservableValue<Boolean>> getSelectedProperty" %}
* **StringConverter&lt;T&gt; converter**,  {% include w3api/param_description.html metodo=_data parametro="StringConverter<T> converter" %}
* **Callback&lt;Integer**,  {% include w3api/param_description.html metodo=_data parametro="Callback<Integer" %}

## Clase Padre
[CheckBoxTableCell](/Java/CheckBoxTableCell/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CheckBoxTableCell.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
