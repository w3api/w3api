---
title: CheckBoxTreeCell.setSelectedStateCallback()
permalink: /Java/CheckBoxTreeCell/setSelectedStateCallback/
date: 2021-01-11
key: Java.C.CheckBoxTreeCell
category: Java
tags: ['java se', 'javafx.scene.control.cell', 'javafx.controls', 'metodo java', 'JavaFX 2.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CheckBoxTreeCell.metodos valor="setSelectedStateCallback" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final void setSelectedStateCallback(Callback<TreeItem<T>,ObservableValue<Boolean>> value)
~~~

## Parámetros
* **ObservableValue&lt;Boolean&gt;&gt; value**,  {% include w3api/param_description.html metodo=_dato parametro="ObservableValue<Boolean>> value" %}
* **Callback&lt;TreeItem&lt;T&gt;**,  {% include w3api/param_description.html metodo=_dato parametro="Callback<TreeItem<T>" %}

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
