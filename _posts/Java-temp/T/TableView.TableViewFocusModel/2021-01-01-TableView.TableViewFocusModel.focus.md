---
title: TableView.TableViewFocusModel.focus()
permalink: /Java/TableView/TableViewFocusModel/focus/
date: 2021-01-11
key: Java.T.TableView.TableViewFocusModel
category: Java
tags: ['java se', 'javafx.scene.control', 'javafx.controls', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TableView.TableViewFocusModel.metodos valor="focus" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void focus(int index)
public void focus(int row, TableColumn<S,?> column)
public void focus(TablePosition pos)
~~~

## Parámetros
* **?&gt; column**,  {% include w3api/param_description.html metodo=_dato parametro="?> column" %}
* **TableColumn&lt;S**,  {% include w3api/param_description.html metodo=_dato parametro="TableColumn<S" %}
* **int row**,  {% include w3api/param_description.html metodo=_dato parametro="int row" %}
* **TablePosition pos**,  {% include w3api/param_description.html metodo=_dato parametro="TablePosition pos" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}

## Clase Padre
[TableView.TableViewFocusModel](/Java/TableView/TableViewFocusModel/)

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
