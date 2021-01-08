---
title: PropertyChangeEvent.PropertyChangeEvent()
permalink: Java/PropertyChangeEvent/PropertyChangeEvent
date: 2021-01-04
key: JavaJava.P.PropertyChangeEvent
category: java
tags: ['java se', 'java.beans', 'java.desktop', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PropertyChangeEvent.constructores valor="PropertyChangeEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PropertyChangeEvent(Object source, String propertyName, Object oldValue, Object newValue)
~~~

## Parámetros
* **Object oldValue**,  {% include w3api/param_description.html metodo=_data parametro="Object oldValue" %}
* **Object newValue**,  {% include w3api/param_description.html metodo=_data parametro="Object newValue" %}
* **String propertyName**,  {% include w3api/param_description.html metodo=_data parametro="String propertyName" %}
* **Object source**,  {% include w3api/param_description.html metodo=_data parametro="Object source" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[PropertyChangeEvent](/Java/PropertyChangeEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PropertyChangeEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
