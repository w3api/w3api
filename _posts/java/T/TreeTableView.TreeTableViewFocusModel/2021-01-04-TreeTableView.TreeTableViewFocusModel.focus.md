---
title: TreeTableView.TreeTableViewFocusModel.focus()
permalink: Java/TreeTableView/TreeTableViewFocusModel/focus
date: 2021-01-04
key: JavaJava.T.TreeTableView.TreeTableViewFocusModel
category: java
tags: ['java se', 'javafx.scene.control', 'javafx.controls', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TreeTableView.TreeTableViewFocusModel.metodos valor="focus" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void focus(int index)
public void focus(int row, TreeTableColumn<S,?> column)
public void focus(TreeTablePosition<S,?> pos)
~~~

## Parámetros
* **?&gt; column**,  {% include w3api/param_description.html metodo=_data parametro="?> column" %}
* **TreeTablePosition&lt;S**,  {% include w3api/param_description.html metodo=_data parametro="TreeTablePosition<S" %}
* **int row**,  {% include w3api/param_description.html metodo=_data parametro="int row" %}
* **TreeTableColumn&lt;S**,  {% include w3api/param_description.html metodo=_data parametro="TreeTableColumn<S" %}
* **int index**,  {% include w3api/param_description.html metodo=_data parametro="int index" %}
* **?&gt; pos**,  {% include w3api/param_description.html metodo=_data parametro="?> pos" %}

## Clase Padre
[TreeTableView.TreeTableViewFocusModel](/Java/TreeTableView/TreeTableViewFocusModel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TreeTableView.TreeTableViewFocusModel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
