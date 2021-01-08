---
title: HierarchyEvent.HierarchyEvent()
permalink: Java/HierarchyEvent/HierarchyEvent
date: 2021-01-04
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
* **Container changedParent**,  {% include w3api/param_description.html metodo=_data parametro="Container changedParent" %}
* **int id**,  {% include w3api/param_description.html metodo=_data parametro="int id" %}
* **Component source**,  {% include w3api/param_description.html metodo=_data parametro="Component source" %}
* **Component changed**,  {% include w3api/param_description.html metodo=_data parametro="Component changed" %}
* **long changeFlags**,  {% include w3api/param_description.html metodo=_data parametro="long changeFlags" %}

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
{%- for _ldc in site.data.Java.H.HierarchyEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
