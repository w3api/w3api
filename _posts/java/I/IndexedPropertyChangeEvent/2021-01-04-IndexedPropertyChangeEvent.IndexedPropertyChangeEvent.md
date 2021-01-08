---
title: IndexedPropertyChangeEvent.IndexedPropertyChangeEvent()
permalink: Java/IndexedPropertyChangeEvent/IndexedPropertyChangeEvent
date: 2021-01-04
key: JavaJava.I.IndexedPropertyChangeEvent
category: java
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
* **String propertyName**,  {% include w3api/param_description.html metodo=_data parametro="String propertyName" %}
* **Object oldValue**,  {% include w3api/param_description.html metodo=_data parametro="Object oldValue" %}
* **Object newValue**,  {% include w3api/param_description.html metodo=_data parametro="Object newValue" %}
* **Object source**,  {% include w3api/param_description.html metodo=_data parametro="Object source" %}
* **int index**,  {% include w3api/param_description.html metodo=_data parametro="int index" %}

## Clase Padre
[IndexedPropertyChangeEvent](/Java/IndexedPropertyChangeEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.IndexedPropertyChangeEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
