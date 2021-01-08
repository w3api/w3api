---
title: TableView.TableViewFocusModel.focus()
permalink: Java/TableView/TableViewFocusModel/focus
date: 2021-01-04
key: JavaJava.T.TableView.TableViewFocusModel
category: java
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
* **?&gt; column**,  {% include w3api/param_description.html metodo=_data parametro="?> column" %}
* **TableColumn&lt;S**,  {% include w3api/param_description.html metodo=_data parametro="TableColumn<S" %}
* **TablePosition pos**,  {% include w3api/param_description.html metodo=_data parametro="TablePosition pos" %}
* **int row**,  {% include w3api/param_description.html metodo=_data parametro="int row" %}
* **int index**,  {% include w3api/param_description.html metodo=_data parametro="int index" %}

## Clase Padre
[TableView.TableViewFocusModel](/Java/TableView/TableViewFocusModel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TableView.TableViewFocusModel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
