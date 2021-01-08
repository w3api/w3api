---
title: TreeTableView.EditEvent.TreeTableView.EditEvent()
permalink: Java/TreeTableView/EditEvent/TreeTableView/EditEvent
date: 2021-01-04
key: JavaJava.T.TreeTableView.EditEvent
category: java
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
* **S newValue**,  {% include w3api/param_description.html metodo=_data parametro="S newValue" %}
* **TreeTableView&lt;S&gt; source**,  {% include w3api/param_description.html metodo=_data parametro="TreeTableView<S> source" %}
* **S oldValue**,  {% include w3api/param_description.html metodo=_data parametro="S oldValue" %}
* **TreeItem&lt;S&gt; treeItem**,  {% include w3api/param_description.html metodo=_data parametro="TreeItem<S> treeItem" %}
* **EventType&lt;? extends TreeTableView.EditEvent&gt; eventType**,  {% include w3api/param_description.html metodo=_data parametro="EventType<? extends TreeTableView.EditEvent> eventType" %}

## Clase Padre
[TreeTableView.EditEvent](/Java/TreeTableView/EditEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TreeTableView.EditEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
