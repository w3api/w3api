---
title: TableColumn.setCellValueFactory()
permalink: Java/TableColumn-javafx-scene-control/setCellValueFactory
date: 2021-01-04
key: JavaJava.T.TableColumn-javafx-scene-control
category: java
tags: ['java se', 'javafx.scene.control', 'javafx.controls', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TableColumn-javafx-scene-control.metodos valor="setCellValueFactory" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final void setCellValueFactory(Callback<TableColumn.CellDataFeatures<S,T>,ObservableValue<T>> value)
~~~

## Parámetros
* **ObservableValue&lt;T&gt;&gt; value**,  {% include w3api/param_description.html metodo=_data parametro="ObservableValue<T>> value" %}
* **Callback&lt;TableColumn.CellDataFeatures&lt;S**,  {% include w3api/param_description.html metodo=_data parametro="Callback<TableColumn.CellDataFeatures<S" %}
* **T&gt;**,  {% include w3api/param_description.html metodo=_data parametro="T>" %}

## Clase Padre
[TableColumn](/Java/TableColumn-javafx-scene-control/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TableColumn-javafx-scene-control.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
