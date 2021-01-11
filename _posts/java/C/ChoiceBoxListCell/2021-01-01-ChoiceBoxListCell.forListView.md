---
title: ChoiceBoxListCell.forListView()
permalink: Java/ChoiceBoxListCell/forListView
date: 2021-01-11
key: JavaJava.C.ChoiceBoxListCell
category: java
tags: ['java se', 'javafx.scene.control.cell', 'javafx.controls', 'metodo java', 'JavaFX 2.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ChoiceBoxListCell.metodos valor="forListView" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T> Callback<ListView<T>,ListCell<T>> forListView(ObservableList<T> items)
static <T> Callback<ListView<T>,ListCell<T>> forListView(StringConverter<T> converter, ObservableList<T> items)
static <T> Callback<ListView<T>,ListCell<T>> forListView(StringConverter<T> converter, T... items)
static <T> Callback<ListView<T>,ListCell<T>> forListView(T... items)
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
