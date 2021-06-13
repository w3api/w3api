---
title: TreeTableView.EditEvent.TreeTableView.EditEvent()
permalink: /Java/TreeTableView/EditEvent/TreeTableView/EditEvent/
date: 2021-01-11
key: Java.T.TreeTableView.EditEvent
category: Java
tags: ['java se', 'javafx.scene.control', 'javafx.controls', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TreeTableView.EditEvent.constructores valor="TreeTableView.EditEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public EditEvent(TreeTableView<S> source, EventType<? extends TreeTableView.EditEvent> eventType, TreeItem<S> treeItem, S oldValue, S newValue)
~~~

## Parámetros
* **TreeItem&lt;S&gt; treeItem**,  {% include w3api/param_description.html metodo=_dato parametro="TreeItem<S> treeItem" %}
* **S newValue**,  {% include w3api/param_description.html metodo=_dato parametro="S newValue" %}
* **TreeTableView&lt;S&gt; source**,  {% include w3api/param_description.html metodo=_dato parametro="TreeTableView<S> source" %}
* **EventType&lt;? extends TreeTableView.EditEvent&gt; eventType**,  {% include w3api/param_description.html metodo=_dato parametro="EventType<? extends TreeTableView.EditEvent> eventType" %}
* **S oldValue**,  {% include w3api/param_description.html metodo=_dato parametro="S oldValue" %}

## Clase Padre
[TreeTableView.EditEvent](/Java/TreeTableView/EditEvent/)

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
