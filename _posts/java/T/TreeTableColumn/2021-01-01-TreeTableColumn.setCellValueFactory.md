---
title: TreeTableColumn.setCellValueFactory()
permalink: /Java/TreeTableColumn/setCellValueFactory/
date: 2021-01-11
key: Java.T.TreeTableColumn
category: Java
tags: ['java se', 'javafx.scene.control', 'javafx.controls', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TreeTableColumn.metodos valor="setCellValueFactory" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final void setCellValueFactory(Callback<TreeTableColumn.CellDataFeatures<S,T>,ObservableValue<T>> value)
~~~

## Parámetros
* **T&gt;**,  {% include w3api/param_description.html metodo=_dato parametro="T>" %}
* **ObservableValue&lt;T&gt;&gt; value**,  {% include w3api/param_description.html metodo=_dato parametro="ObservableValue<T>> value" %}
* **Callback&lt;TreeTableColumn.CellDataFeatures&lt;S**,  {% include w3api/param_description.html metodo=_dato parametro="Callback<TreeTableColumn.CellDataFeatures<S" %}

## Clase Padre
[TreeTableColumn](/Java/TreeTableColumn/)

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
