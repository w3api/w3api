---
title: ChoiceBoxListCell.ChoiceBoxListCell()
permalink: /Java/ChoiceBoxListCell/ChoiceBoxListCell/
date: 2021-01-11
key: Java.C.ChoiceBoxListCell
category: Java
tags: ['java se', 'javafx.scene.control.cell', 'javafx.controls', 'metodo java', 'JavaFX 2.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ChoiceBoxListCell.constructores valor="ChoiceBoxListCell" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ChoiceBoxListCell()
public ChoiceBoxListCell(ObservableList<T> items)
public ChoiceBoxListCell(StringConverter<T> converter, ObservableList<T> items)
@SafeVarargs public ChoiceBoxListCell(StringConverter<T> converter, T... items)
@SafeVarargs public ChoiceBoxListCell(T... items)
~~~

## Parámetros
* **StringConverter&lt;T&gt; converter**,  {% include w3api/param_description.html metodo=_dato parametro="StringConverter<T> converter" %}
* **ObservableList&lt;T&gt; items**,  {% include w3api/param_description.html metodo=_dato parametro="ObservableList<T> items" %}
* **T... items**,  {% include w3api/param_description.html metodo=_dato parametro="T... items" %}

## Clase Padre
[ChoiceBoxListCell](/Java/ChoiceBoxListCell/)

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
