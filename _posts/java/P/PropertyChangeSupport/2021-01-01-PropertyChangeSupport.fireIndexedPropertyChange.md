---
title: PropertyChangeSupport.fireIndexedPropertyChange()
permalink: /Java/PropertyChangeSupport/fireIndexedPropertyChange/
date: 2021-01-11
key: Java.P.PropertyChangeSupport
category: Java
tags: ['java se', 'java.beans', 'java.desktop', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PropertyChangeSupport.metodos valor="fireIndexedPropertyChange" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void fireIndexedPropertyChange(String propertyName, int index, boolean oldValue, boolean newValue)
public void fireIndexedPropertyChange(String propertyName, int index, int oldValue, int newValue)
public void fireIndexedPropertyChange(String propertyName, int index, Object oldValue, Object newValue)
~~~

## Parámetros
* **Object oldValue**,  {% include w3api/param_description.html metodo=_dato parametro="Object oldValue" %}
* **Object newValue**,  {% include w3api/param_description.html metodo=_dato parametro="Object newValue" %}
* **String propertyName**,  {% include w3api/param_description.html metodo=_dato parametro="String propertyName" %}
* **boolean newValue**,  {% include w3api/param_description.html metodo=_dato parametro="boolean newValue" %}
* **int newValue**,  {% include w3api/param_description.html metodo=_dato parametro="int newValue" %}
* **int oldValue**,  {% include w3api/param_description.html metodo=_dato parametro="int oldValue" %}
* **boolean oldValue**,  {% include w3api/param_description.html metodo=_dato parametro="boolean oldValue" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}

## Clase Padre
[PropertyChangeSupport](/Java/PropertyChangeSupport/)

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
