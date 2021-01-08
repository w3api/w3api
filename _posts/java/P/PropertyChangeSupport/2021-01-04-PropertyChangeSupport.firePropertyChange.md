---
title: PropertyChangeSupport.firePropertyChange()
permalink: Java/PropertyChangeSupport/firePropertyChange
date: 2021-01-04
key: JavaJava.P.PropertyChangeSupport
category: java
tags: ['java se', 'java.beans', 'java.desktop', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PropertyChangeSupport.metodos valor="firePropertyChange" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void firePropertyChange(PropertyChangeEvent event)
public void firePropertyChange(String propertyName, boolean oldValue, boolean newValue)
public void firePropertyChange(String propertyName, int oldValue, int newValue)
public void firePropertyChange(String propertyName, Object oldValue, Object newValue)
~~~

## Parámetros
* **String propertyName**,  {% include w3api/param_description.html metodo=_data parametro="String propertyName" %}
* **boolean oldValue**,  {% include w3api/param_description.html metodo=_data parametro="boolean oldValue" %}
* **Object oldValue**,  {% include w3api/param_description.html metodo=_data parametro="Object oldValue" %}
* **Object newValue**,  {% include w3api/param_description.html metodo=_data parametro="Object newValue" %}
* **boolean newValue**,  {% include w3api/param_description.html metodo=_data parametro="boolean newValue" %}
* **int newValue**,  {% include w3api/param_description.html metodo=_data parametro="int newValue" %}
* **int oldValue**,  {% include w3api/param_description.html metodo=_data parametro="int oldValue" %}
* **PropertyChangeEvent event**,  {% include w3api/param_description.html metodo=_data parametro="PropertyChangeEvent event" %}

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
