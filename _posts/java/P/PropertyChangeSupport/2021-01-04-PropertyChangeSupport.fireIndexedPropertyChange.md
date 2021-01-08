---
title: PropertyChangeSupport.fireIndexedPropertyChange()
permalink: Java/PropertyChangeSupport/fireIndexedPropertyChange
date: 2021-01-04
key: JavaJava.P.PropertyChangeSupport
category: java
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
* **int newValue**,  {% include w3api/param_description.html metodo=_data parametro="int newValue" %}
* **String propertyName**,  {% include w3api/param_description.html metodo=_data parametro="String propertyName" %}
* **boolean oldValue**,  {% include w3api/param_description.html metodo=_data parametro="boolean oldValue" %}
* **Object oldValue**,  {% include w3api/param_description.html metodo=_data parametro="Object oldValue" %}
* **Object newValue**,  {% include w3api/param_description.html metodo=_data parametro="Object newValue" %}
* **boolean newValue**,  {% include w3api/param_description.html metodo=_data parametro="boolean newValue" %}
* **int index**,  {% include w3api/param_description.html metodo=_data parametro="int index" %}
* **int oldValue**,  {% include w3api/param_description.html metodo=_data parametro="int oldValue" %}

## Clase Padre
[PropertyChangeSupport](/Java/PropertyChangeSupport/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PropertyChangeSupport.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
