---
title: TableView.TableViewSelectionModel.isSelected()
permalink: /Java/TableView/TableViewSelectionModel/isSelected/
date: 2021-01-11
key: Java.T.TableView.TableViewSelectionModel
category: Java
tags: ['java se', 'javafx.scene.control', 'javafx.controls', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TableView.TableViewSelectionModel.metodos valor="isSelected" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean isSelected(int index)
public abstract boolean isSelected(int row, TableColumn<S,?> column)
~~~

## Parámetros
* **?&gt; column**,  {% include w3api/param_description.html metodo=_dato parametro="?> column" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}
* **TableColumn&lt;S**,  {% include w3api/param_description.html metodo=_dato parametro="TableColumn<S" %}
* **int row**,  {% include w3api/param_description.html metodo=_dato parametro="int row" %}

## Clase Padre
[TableView.TableViewSelectionModel](/Java/TableView/TableViewSelectionModel/)

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
