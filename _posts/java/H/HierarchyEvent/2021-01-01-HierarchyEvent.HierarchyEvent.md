---
title: HierarchyEvent.HierarchyEvent()
permalink: Java/HierarchyEvent/HierarchyEvent
date: 2021-01-11
key: JavaJava.H.HierarchyEvent
category: java
tags: ['java se', 'java.awt.event', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HierarchyEvent.constructores valor="HierarchyEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public HierarchyEvent(Component source, int id, Component changed, Container changedParent)
public HierarchyEvent(Component source, int id, Component changed, Container changedParent, long changeFlags)
~~~

## Parámetros
* **int id**,  {% include w3api/param_description.html metodo=_dato parametro="int id" %}
* **Container changedParent**,  {% include w3api/param_description.html metodo=_dato parametro="Container changedParent" %}
* **Component changed**,  {% include w3api/param_description.html metodo=_dato parametro="Component changed" %}
* **long changeFlags**,  {% include w3api/param_description.html metodo=_dato parametro="long changeFlags" %}
* **Component source**,  {% include w3api/param_description.html metodo=_dato parametro="Component source" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[HierarchyEvent](/Java/HierarchyEvent/)

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
