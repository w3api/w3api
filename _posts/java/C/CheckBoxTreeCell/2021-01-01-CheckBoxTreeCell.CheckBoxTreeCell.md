---
title: CheckBoxTreeCell.CheckBoxTreeCell()
permalink: /Java/CheckBoxTreeCell/CheckBoxTreeCell/
date: 2021-01-11
key: Java.C.CheckBoxTreeCell
category: Java
tags: ['java se', 'javafx.scene.control.cell', 'javafx.controls', 'metodo java', 'JavaFX 2.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CheckBoxTreeCell.constructores valor="CheckBoxTreeCell" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public CheckBoxTreeCell()
public CheckBoxTreeCell(Callback<TreeItem<T>,ObservableValue<Boolean>> getSelectedProperty)
public CheckBoxTreeCell(Callback<TreeItem<T>,ObservableValue<Boolean>> getSelectedProperty, StringConverter<TreeItem<T>> converter)
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

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
