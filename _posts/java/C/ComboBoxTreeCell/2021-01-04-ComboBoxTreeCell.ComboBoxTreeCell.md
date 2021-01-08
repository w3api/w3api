---
title: ComboBoxTreeCell.ComboBoxTreeCell()
permalink: Java/ComboBoxTreeCell/ComboBoxTreeCell
date: 2021-01-04
key: JavaJava.C.ComboBoxTreeCell
category: java
tags: ['java se', 'javafx.scene.control.cell', 'javafx.controls', 'metodo java', 'JavaFX 2.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ComboBoxTreeCell.constructores valor="ComboBoxTreeCell" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ComboBoxTreeCell()
public ComboBoxTreeCell(ObservableList<T> items)
public ComboBoxTreeCell(StringConverter<T> converter, ObservableList<T> items)
@SafeVarargs public ComboBoxTreeCell(StringConverter<T> converter, T... items)
@SafeVarargs public ComboBoxTreeCell(T... items)
~~~

## Parámetros
* **StringConverter&lt;T&gt; converter**,  {% include w3api/param_description.html metodo=_data parametro="StringConverter<T> converter" %}
* **ObservableList&lt;T&gt; items**,  {% include w3api/param_description.html metodo=_data parametro="ObservableList<T> items" %}
* **T... items**,  {% include w3api/param_description.html metodo=_data parametro="T... items" %}

## Clase Padre
[ComboBoxTreeCell](/Java/ComboBoxTreeCell/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ComboBoxTreeCell.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
