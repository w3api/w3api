---
title: CheckBoxListCell.CheckBoxListCell()
permalink: Java/CheckBoxListCell/CheckBoxListCell
date: 2021-01-04
key: JavaJava.C.CheckBoxListCell
category: java
tags: ['java se', 'javafx.scene.control.cell', 'javafx.controls', 'metodo java', 'JavaFX 2.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CheckBoxListCell.constructores valor="CheckBoxListCell" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public CheckBoxListCell()
public CheckBoxListCell(Callback<T,ObservableValue<Boolean>> getSelectedProperty)
public CheckBoxListCell(Callback<T,ObservableValue<Boolean>> getSelectedProperty, StringConverter<T> converter)
~~~

## Parámetros
* **ObservableValue&lt;Boolean&gt;&gt; getSelectedProperty**,  {% include w3api/param_description.html metodo=_data parametro="ObservableValue<Boolean>> getSelectedProperty" %}
* **StringConverter&lt;T&gt; converter**,  {% include w3api/param_description.html metodo=_data parametro="StringConverter<T> converter" %}
* **Callback&lt;T**,  {% include w3api/param_description.html metodo=_data parametro="Callback<T" %}

## Clase Padre
[CheckBoxListCell](/Java/CheckBoxListCell/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CheckBoxListCell.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
