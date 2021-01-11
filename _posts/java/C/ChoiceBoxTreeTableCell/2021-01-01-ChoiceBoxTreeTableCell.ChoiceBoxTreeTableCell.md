---
title: ChoiceBoxTreeTableCell.ChoiceBoxTreeTableCell()
permalink: Java/ChoiceBoxTreeTableCell/ChoiceBoxTreeTableCell
date: 2021-01-11
key: JavaJava.C.ChoiceBoxTreeTableCell
category: java
tags: ['java se', 'javafx.scene.control.cell', 'javafx.controls', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ChoiceBoxTreeTableCell.constructores valor="ChoiceBoxTreeTableCell" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ChoiceBoxTreeTableCell()
public ChoiceBoxTreeTableCell(ObservableList<T> items)
public ChoiceBoxTreeTableCell(StringConverter<T> converter, ObservableList<T> items)
@SafeVarargs public ChoiceBoxTreeTableCell(StringConverter<T> converter, T... items)
@SafeVarargs public ChoiceBoxTreeTableCell(T... items)
~~~

## Parámetros
* **StringConverter&lt;T&gt; converter**,  {% include w3api/param_description.html metodo=_dato parametro="StringConverter<T> converter" %}
* **ObservableList&lt;T&gt; items**,  {% include w3api/param_description.html metodo=_dato parametro="ObservableList<T> items" %}
* **T... items**,  {% include w3api/param_description.html metodo=_dato parametro="T... items" %}

## Clase Padre
[ChoiceBoxTreeTableCell](/Java/ChoiceBoxTreeTableCell/)

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
