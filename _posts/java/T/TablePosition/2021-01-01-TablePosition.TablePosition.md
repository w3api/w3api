---
title: TablePosition.TablePosition()
permalink: /Java/TablePosition/TablePosition/
date: 2021-01-11
key: Java.T.TablePosition
category: Java
tags: ['java se', 'javafx.scene.control', 'javafx.controls', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TablePosition.constructores valor="TablePosition" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public TablePosition(TableView<S> tableView, int row, TableColumn<S,T> tableColumn)
~~~

## Parámetros
* **T&gt; tableColumn**,  {% include w3api/param_description.html metodo=_dato parametro="T> tableColumn" %}
* **TableView&lt;S&gt; tableView**,  {% include w3api/param_description.html metodo=_dato parametro="TableView<S> tableView" %}
* **TableColumn&lt;S**,  {% include w3api/param_description.html metodo=_dato parametro="TableColumn<S" %}
* **int row**,  {% include w3api/param_description.html metodo=_dato parametro="int row" %}

## Clase Padre
[TablePosition](/Java/TablePosition/)

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
