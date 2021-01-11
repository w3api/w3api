---
title: ChoiceBoxTreeCell.ChoiceBoxTreeCell()
permalink: Java/ChoiceBoxTreeCell/ChoiceBoxTreeCell
date: 2021-01-11
key: JavaJava.C.ChoiceBoxTreeCell
category: java
tags: ['java se', 'javafx.scene.control.cell', 'javafx.controls', 'metodo java', 'JavaFX 2.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ChoiceBoxTreeCell.constructores valor="ChoiceBoxTreeCell" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ChoiceBoxTreeCell()
public ChoiceBoxTreeCell(ObservableList<T> items)
public ChoiceBoxTreeCell(StringConverter<T> converter, ObservableList<T> items)
@SafeVarargs public ChoiceBoxTreeCell(StringConverter<T> converter, T... items)
@SafeVarargs public ChoiceBoxTreeCell(T... items)
~~~

## Parámetros
* **StringConverter&lt;T&gt; converter**,  {% include w3api/param_description.html metodo=_dato parametro="StringConverter<T> converter" %}
* **ObservableList&lt;T&gt; items**,  {% include w3api/param_description.html metodo=_dato parametro="ObservableList<T> items" %}
* **T... items**,  {% include w3api/param_description.html metodo=_dato parametro="T... items" %}

## Clase Padre
[ChoiceBoxTreeCell](/Java/ChoiceBoxTreeCell/)

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
