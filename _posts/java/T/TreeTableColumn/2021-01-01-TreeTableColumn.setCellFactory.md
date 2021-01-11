---
title: TreeTableColumn.setCellFactory()
permalink: Java/TreeTableColumn/setCellFactory
date: 2021-01-11
key: JavaJava.T.TreeTableColumn
category: java
tags: ['java se', 'javafx.scene.control', 'javafx.controls', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TreeTableColumn.metodos valor="setCellFactory" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final void setCellFactory(Callback<TreeTableColumn<S,T>,TreeTableCell<S,T>> value)
~~~

## Parámetros
* **Callback&lt;TreeTableColumn&lt;S**,  {% include w3api/param_description.html metodo=_dato parametro="Callback<TreeTableColumn<S" %}
* **TreeTableCell&lt;S**,  {% include w3api/param_description.html metodo=_dato parametro="TreeTableCell<S" %}
* **T&gt;&gt; value**,  {% include w3api/param_description.html metodo=_dato parametro="T>> value" %}
* **T&gt;**,  {% include w3api/param_description.html metodo=_dato parametro="T>" %}

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
