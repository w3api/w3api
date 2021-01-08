---
title: TableView.TableViewSelectionModel.isSelected()
permalink: Java/TableView/TableViewSelectionModel/isSelected
date: 2021-01-04
key: JavaJava.T.TableView.TableViewSelectionModel
category: java
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
* **int index**,  {% include w3api/param_description.html metodo=_data parametro="int index" %}
* **int row**,  {% include w3api/param_description.html metodo=_data parametro="int row" %}
* **?&gt; column**,  {% include w3api/param_description.html metodo=_data parametro="?> column" %}
* **TableColumn&lt;S**,  {% include w3api/param_description.html metodo=_data parametro="TableColumn<S" %}

## Clase Padre
[TableView.TableViewSelectionModel](/Java/TableView/TableViewSelectionModel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TableView.TableViewSelectionModel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
