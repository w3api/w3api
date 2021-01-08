---
title: CheckBoxTreeCell.CheckBoxTreeCell()
permalink: Java/CheckBoxTreeCell/CheckBoxTreeCell
date: 2021-01-04
key: JavaJava.C.CheckBoxTreeCell
category: java
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
* **Callback&lt;TreeItem&lt;T&gt;**,  {% include w3api/param_description.html metodo=_data parametro="Callback<TreeItem<T>" %}
* **ObservableValue&lt;Boolean&gt;&gt; getSelectedProperty**,  {% include w3api/param_description.html metodo=_data parametro="ObservableValue<Boolean>> getSelectedProperty" %}
* **StringConverter&lt;TreeItem&lt;T&gt;&gt; converter**,  {% include w3api/param_description.html metodo=_data parametro="StringConverter<TreeItem<T>> converter" %}

## Clase Padre
[CheckBoxTreeCell](/Java/CheckBoxTreeCell/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CheckBoxTreeCell.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
