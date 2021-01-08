---
title: ListSelectionEvent.ListSelectionEvent()
permalink: Java/ListSelectionEvent/ListSelectionEvent
date: 2021-01-04
key: JavaJava.L.ListSelectionEvent
category: java
tags: ['java se', 'javax.swing.event', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.ListSelectionEvent.constructores valor="ListSelectionEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ListSelectionEvent(Object source, int firstIndex, int lastIndex, boolean isAdjusting)
~~~

## Parámetros
* **int firstIndex**,  {% include w3api/param_description.html metodo=_data parametro="int firstIndex" %}
* **boolean isAdjusting**,  {% include w3api/param_description.html metodo=_data parametro="boolean isAdjusting" %}
* **int lastIndex**,  {% include w3api/param_description.html metodo=_data parametro="int lastIndex" %}
* **Object source**,  {% include w3api/param_description.html metodo=_data parametro="Object source" %}

## Clase Padre
[ListSelectionEvent](/Java/ListSelectionEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.ListSelectionEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
