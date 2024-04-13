---
title: IndexedPropertyChangeEvent.IndexedPropertyChangeEvent()
permalink: /Java/IndexedPropertyChangeEvent/IndexedPropertyChangeEvent/
date: 2021-01-11
key: Java.I.IndexedPropertyChangeEvent
category: Java
tags: ['java se', 'java.beans', 'java.desktop', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IndexedPropertyChangeEvent.constructores valor="IndexedPropertyChangeEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public IndexedPropertyChangeEvent(Object source, String propertyName, Object oldValue, Object newValue, int index)
~~~

## Parámetros
* **Object oldValue**,  {% include w3api/param_description.html metodo=_dato parametro="Object oldValue" %}
* **Object newValue**,  {% include w3api/param_description.html metodo=_dato parametro="Object newValue" %}
* **Object source**,  {% include w3api/param_description.html metodo=_dato parametro="Object source" %}
* **String propertyName**,  {% include w3api/param_description.html metodo=_dato parametro="String propertyName" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}

## Clase Padre
[IndexedPropertyChangeEvent](/Java/IndexedPropertyChangeEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
