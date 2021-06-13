---
title: CheckBoxListCell.CheckBoxListCell()
permalink: /Java/CheckBoxListCell/CheckBoxListCell/
date: 2021-01-11
key: Java.C.CheckBoxListCell
category: Java
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
* **Callback&lt;T**,  {% include w3api/param_description.html metodo=_dato parametro="Callback<T" %}
* **StringConverter&lt;T&gt; converter**,  {% include w3api/param_description.html metodo=_dato parametro="StringConverter<T> converter" %}
* **ObservableValue&lt;Boolean&gt;&gt; getSelectedProperty**,  {% include w3api/param_description.html metodo=_dato parametro="ObservableValue<Boolean>> getSelectedProperty" %}

## Clase Padre
[CheckBoxListCell](/Java/CheckBoxListCell/)

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
