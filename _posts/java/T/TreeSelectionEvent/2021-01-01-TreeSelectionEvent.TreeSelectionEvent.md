---
title: TreeSelectionEvent.TreeSelectionEvent()
permalink: Java/TreeSelectionEvent/TreeSelectionEvent
date: 2021-01-11
key: JavaJava.T.TreeSelectionEvent
category: java
tags: ['java se', 'javax.swing.event', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TreeSelectionEvent.constructores valor="TreeSelectionEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public TreeSelectionEvent(Object source, TreePath[] paths, boolean[] areNew, TreePath oldLeadSelectionPath, TreePath newLeadSelectionPath)
public TreeSelectionEvent(Object source, TreePath path, boolean isNew, TreePath oldLeadSelectionPath, TreePath newLeadSelectionPath)
~~~

## Parámetros
* **TreePath newLeadSelectionPath**,  {% include w3api/param_description.html metodo=_dato parametro="TreePath newLeadSelectionPath" %}
* **TreePath oldLeadSelectionPath**,  {% include w3api/param_description.html metodo=_dato parametro="TreePath oldLeadSelectionPath" %}
* **Object source**,  {% include w3api/param_description.html metodo=_dato parametro="Object source" %}
* **TreePath path**,  {% include w3api/param_description.html metodo=_dato parametro="TreePath path" %}
* **boolean[] areNew**,  {% include w3api/param_description.html metodo=_dato parametro="boolean[] areNew" %}
* **TreePath[] paths**,  {% include w3api/param_description.html metodo=_dato parametro="TreePath[] paths" %}
* **boolean isNew**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isNew" %}

## Clase Padre
[TreeSelectionEvent](/Java/TreeSelectionEvent/)

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
