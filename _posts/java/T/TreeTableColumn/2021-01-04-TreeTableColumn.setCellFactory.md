---
title: TreeTableColumn.setCellFactory()
permalink: Java/TreeTableColumn/setCellFactory
date: 2021-01-04
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
* **TreeTableCell&lt;S**,  {% include w3api/param_description.html metodo=_data parametro="TreeTableCell<S" %}
* **T&gt;&gt; value**,  {% include w3api/param_description.html metodo=_data parametro="T>> value" %}
* **Callback&lt;TreeTableColumn&lt;S**,  {% include w3api/param_description.html metodo=_data parametro="Callback<TreeTableColumn<S" %}
* **T&gt;**,  {% include w3api/param_description.html metodo=_data parametro="T>" %}

## Clase Padre
[TreeTableColumn](/Java/TreeTableColumn/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TreeTableColumn.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
