---
title: TableSelectionModel.select()
permalink: Java/TableSelectionModel/select
date: 2021-01-04
key: JavaJava.T.TableSelectionModel
category: java
tags: ['java se', 'javafx.scene.control', 'javafx.controls', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TableSelectionModel.metodos valor="select" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void select(int row)
public void select(T obj)
public abstract void select(int row, TableColumnBase<T,?> column)
~~~

## Parámetros
* **TableColumnBase&lt;T**,  {% include w3api/param_description.html metodo=_data parametro="TableColumnBase<T" %}
* **?&gt; column**,  {% include w3api/param_description.html metodo=_data parametro="?> column" %}
* **int row**,  {% include w3api/param_description.html metodo=_data parametro="int row" %}
* **T obj**,  {% include w3api/param_description.html metodo=_data parametro="T obj" %}

## Clase Padre
[TableSelectionModel](/Java/TableSelectionModel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TableSelectionModel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
