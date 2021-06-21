---
title: CheckBoxTreeCell.forTreeView()
permalink: /Java/CheckBoxTreeCell/forTreeView/
date: 2021-01-11
key: Java.C.CheckBoxTreeCell
category: Java
tags: ['java se', 'javafx.scene.control.cell', 'javafx.controls', 'metodo java', 'JavaFX 2.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CheckBoxTreeCell.metodos valor="forTreeView" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T> Callback<TreeView<T>,TreeCell<T>> forTreeView()
static <T> Callback<TreeView<T>,TreeCell<T>> forTreeView(Callback<TreeItem<T>,ObservableValue<Boolean>> getSelectedProperty)
static <T> Callback<TreeView<T>,TreeCell<T>> forTreeView(Callback<TreeItem<T>,ObservableValue<Boolean>> getSelectedProperty, StringConverter<TreeItem<T>> converter)
~~~

## Parámetros
* **StringConverter&lt;TreeItem&lt;T&gt;&gt; converter**,  {% include w3api/param_description.html metodo=_dato parametro="StringConverter<TreeItem<T>> converter" %}
* **Callback&lt;TreeItem&lt;T&gt;**,  {% include w3api/param_description.html metodo=_dato parametro="Callback<TreeItem<T>" %}
* **ObservableValue&lt;Boolean&gt;&gt; getSelectedProperty**,  {% include w3api/param_description.html metodo=_dato parametro="ObservableValue<Boolean>> getSelectedProperty" %}

## Clase Padre
[CheckBoxTreeCell](/Java/CheckBoxTreeCell/)

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
